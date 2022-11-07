from plot.helper import save_plots_over_models_datasets, save_plots_over_xy_axes
from settings import get_evaluation_config


x_axis_mapper = {'statistical_parity_absolute_difference': 'Statistical Parity Abs Diff',
                 'normalized_mutual_information': 'Normalized MI',
                 'consistency_score_objective': 'Consistency Obj',
                 'disparate_impact_ratio_objective': 'Disparate Impact Obj'}


def plot_all_datasets():
    # settings
    x_axes = ['Statistical Parity Abs Diff']
    y_axes = ['AUC']

    # iteration
    dataset_pro_attributes, models = get_evaluation_config(config='comparison_preprocessors',
                                                           plot=True)
    save_plots_over_xy_axes(x_axes, y_axes, models, dataset_pro_attributes)


def plot_all_datasets_metrics():
    # settings
    x_axes = ['Statistical Parity Abs Diff',
              'Normalized MI',
              'Average Odds Error']
    y_axes = ['AUC']

    # iteration
    dataset_pro_attributes, models = get_evaluation_config(config='comparison_preprocessors',
                                                           plot=True)
    save_plots_over_xy_axes(x_axes, y_axes, models, dataset_pro_attributes)


def plot_fairness_agnostic():
    # settings
    y_axis = 'AUC'

    # preprocess on multiple metrics
    dataset_pro_attributes, models, metrics = get_evaluation_config(config='fairness_agnostic',
                                                                    plot=True)
    x_axes = {k: x_axis_mapper[k] for k in metrics}

    for metric_path, metric_name in x_axes.items():
        save_plots_over_models_datasets(metric_name, y_axis, models, dataset_pro_attributes,
                                        filepath_prefix=f"results/{metric_path}")


def quick_plot():
    # settings
    x_axes = ['Disparate Impact Obj']
    y_axes = ['AUC']
    models = ['KNeighborsClassifier']

    dataset_pro_attributes = [('adult', 'sex')]

    save_plots_over_xy_axes(x_axes, y_axes, models, dataset_pro_attributes, show=True)


def main():
    experiments = {'quick_plot': quick_plot,
                   'plot_all_datasets': plot_all_datasets,
                   'plot_all_dataset_metrics': plot_all_datasets_metrics,
                   'plot_fairness_agnostic': plot_fairness_agnostic}

    pick = 'plot_fairness_agnostic'

    experiments[pick]()


if __name__ == '__main__':
    main()