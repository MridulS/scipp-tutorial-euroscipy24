import matplotlib.pyplot as plt
import numpy as np


def plot(*x):
    """
    Useful plot function for 1d and 2d data
    """
    fig, ax = plt.subplots()
    for a in x:
        if a.ndim == 1:
            ax.plot(np.arange(len(a)), a)
        elif a.ndim == 2:
            cax = ax.imshow(a, origin="lower")
            fig.colorbar(cax, ax=ax)


def fill_up_container(container, seeds):
    random_seeds = np.random.choice(container.size, seeds.value, replace=False)
    coordinates = np.unravel_index(random_seeds, container.shape)
    container.values[coordinates] = 1
