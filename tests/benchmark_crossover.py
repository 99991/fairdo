import numpy as np
import time
from fairdo.optimize.geneticoperators import kpoint_crossover,\
    uniform_crossover

def benchmark(func, repeats=10):
    """
    Benchmark the execution time of a function.

    Parameters
    ----------
    func: callable
        The function to benchmark.
    repeats: int, optional
        The number of times to repeat the benchmark.

    Returns
    -------
    float
        The average execution time in seconds.
    """
    total_time = 0
    for _ in range(repeats):
        start_time = time.time()
        func()
        end_time = time.time()
        total_time += (end_time - start_time)
    return total_time / repeats


def test1():
    parents = np.ones((2, 1000))

    offspring = uniform_crossover(parents, 1000, p=0.5)

def test2():
    parents = np.ones((2, 1000))

    offspring = kpoint_crossover(parents, 1000, k=1)


if __name__ == "__main__":
    avg_time = benchmark(test1, repeats=10)
    print(f"Average execution time over 10 runs: {avg_time:.4f} seconds")
    avg_time = benchmark(test2, repeats=10)
    print(f"Average execution time over 10 runs: {avg_time:.4f} seconds")

