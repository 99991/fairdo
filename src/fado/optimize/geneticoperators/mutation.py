import numpy as np


def mutate(offspring, mutation_rate=0.05):
    """
    Mutates the given offspring by flipping a percentage of random bits for each offspring.

    Parameters
    ----------
    offspring: ndarray, shape (n, d)
        The offspring to be mutated. Each row represents an offspring, and each column represents a bit.
    mutation_rate: float, optional
        The percentage of random bits to flip for each offspring. Default is 0.05.

    Returns
    -------
    offspring: ndarray, shape (n, d)
        The mutated offspring. Each row represents an offspring, and each column represents a bit.
    """
    num_mutation = int(mutation_rate * offspring.shape[1])
    for idx in range(offspring.shape[0]):
        # select the random bits to flip
        mutation_bits = np.random.choice(np.arange(offspring.shape[1]),
                                         num_mutation,
                                         replace=False)
        # flip the bits
        offspring[idx, mutation_bits] = 1 - offspring[idx, mutation_bits]
    return offspring


def bit_flip_mutation(offspring, mutation_rate=0.05):
    """
    Mutates the given offspring by flipping each bit with a certain probability.

    Parameters
    ----------
    offspring: ndarray, shape (n, d)
        The offspring to be mutated. Each row represents an offspring, and each column represents a bit.
    mutation_rate: float, optional
        The probability of flipping each bit. Default is 0.05.

    Returns
    -------
    offspring: ndarray, shape (n, d)
        The mutated offspring. Each row represents an offspring, and each column represents a bit.
    """
    mutation_mask = np.random.rand(*offspring.shape) < mutation_rate
    offspring[mutation_mask] = 1 - offspring[mutation_mask]
    return offspring


def swap_mutation(offspring):
    """
    Mutates the given offspring by randomly selecting two bits and swapping their values.

    Parameters
    ----------
    offspring: ndarray, shape (n, d)
        The offspring to be mutated. Each row represents an offspring, and each column represents a bit.

    Returns
    -------
    offspring: ndarray, shape (n, d)
        The mutated offspring. Each row represents an offspring, and each column represents a bit.
    """
    for idx in range(offspring.shape[0]):
        # select two random bits
        bit1, bit2 = np.random.choice(np.arange(offspring.shape[1]), 2, replace=False)
        # swap the bits
        offspring[idx, bit1], offspring[idx, bit2] = offspring[idx, bit2], offspring[idx, bit1]
    return offspring

