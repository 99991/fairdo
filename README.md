# Fairness-Agnostic Data Optimization
**FairDo** is a Python package for mitigating bias in data.
The approaches, which are _fairness-agnostic_, enable optimization of diverse
fairness criteria quantifying discrimination within datasets,
leading to the generation of biased-reduced datasets.
Our framework is able to deal with non-binary protected attributes
such as nationality, race, and gender that naturally arise in many
applications.
Due to the possibility to choose between any of the available fairness metrics,
it is possible to aim for the least fortunate group
(Rawls' A Theory of Justice [2]) or the general utility of all groups
(Utilitarianism).

## Installation

### Dependencies
Python (>=3.8, <4), numpy, pandas, scikit-learn, copulas

### Manual Installation

```bash
python setup.py install
```

### Development

```python
pip install -e.
```

## Example Usage

### Genetic Algorithms
In the following example, we use the COMPAS [1] dataset.
The protected attribute is race and the label is recidivism.
Here, we deploy a genetic algorithm to remove discriminatory samples
of the merged original and synthetic dataset:

```python
# Standard library
from functools import partial

# Related third-party imports
from sdv.tabular import GaussianCopula
import pandas as pd

# fairdo package
from fairdo.utils.dataset import load_data
from fairdo.preprocessing import HeuristicWrapper
from fairdo.optimize.geneticalgorithm import genetic_algorithm
from fairdo.metrics import statistical_parity_abs_diff_max

# Loading a sample database and encoding for appropriate usage
# data is a pandas dataframe
data, label, protected_attributes = load_data('compas')

# Create synthetic data
gc = GaussianCopula()
gc.fit(data)
data_syn = gc.sample(data.shape[0])

# Merge/concat original and synthetic data
data = pd.concat([data, data_syn.copy()], axis=0)

# Initial settings for the Genetic Algorithm
ga = partial(genetic_algorithm,
             pop_size=100,
             num_generations=100)
             
# Optimization step
preprocessor = HeuristicWrapper(heuristic=ga,
                                protected_attribute=protected_attributes[0],
                                label=label,
                                disc=statistical_parity_abs_diff_max)
data_fair = preprocessor.fit_transform(dataset=data,
                                       approach='remove')                                
```

### MetricOptimizer
In the following example, we use the COMPAS [1] dataset.
The protected attribute is race and the label is recidivism.
Here, we use the package's own heuristic to yield for fair data.
25% synthetic data is added to reduce bias in this example:

```python
# Imports
from fairdo.preprocessing import MetricOptimizer
from fairdo.utils.dataset import load_data

# Loading a sample database and encoding for appropriate usage
# data is a pandas dataframe
data, label, protected_attributes = load_data('compas')

# Initialize MetricOptimizer
preproc = MetricOptimizer(frac=1.25,
                          protected_attribute=protected_attributes[0],
                          label='label')
                          
data_fair = preproc.fit_transform(data)
```

More ``jupyter notebooks`` examples can be viewed in ``tutorials/``.


## Evaluation

As the evaluation script depends on other algorithms, it is necessary to install
the appropriate packages by:

```bash
cd evaluation
pip install -r requirements.txt
```

### Evaluate Heuristics for Non-Binary Protected Attribute Fairness

To evaluate the heuristics for non-binary protected attributes, run the
following command:
```bash
python evaluation/nonbinary/quick_eval.py
```
Experiments on tuning population size and number of generations
as well as comparing different operators and heuristics can all be done
in `quick_eval.py`. Modify the function `run_and_save_experiment` by
renaming the appropriate settings function
`setup_experiment`/`setup_experiment_hyperparameter`.
Although the experiments make use of multiprocessing,
it runs through all settings, heuristics, datasets, trials and can
therefore take a while.

After the results are exported, plots can be created by running:
```bash
python evaluation/nonbinary/create_plots.py
```

### Evaluate MetricOptimizer

To evaluate MetricOptimizer, run the following command:

```bash
python evaluation/run_evaluation.py
```
The results are saved under ``evaluation/results/...``.

Create plots from results
```bash
python evaluation/create_plots.py
```
The plots are stored in the same directory as their corresponding .csv file.

To modify or change several settings (datasets, metrics, #runs) in the
evaluation, change the file ``evaluation/settings.py``.

## References
[1] Larson, J., Angwin, J., Mattu, S.,  Kirchner, L.: Machine
bias (May 2016),
https://www.propublica.org/article/machine-bias-risk-assessments-in-criminal-sentencing
[2] Rawls, J.: A Theory of Justice (1971), Belknap Press, ISBN: 978-0-674-00078-0
