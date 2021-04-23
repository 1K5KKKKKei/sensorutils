"""plot signals and cross spectral density.
"""
from typing import Iterable, Union
import numpy as np
import matplotlib.pyplot as plt

def CSD(x: Iterable, s1: np.ndarray, s2: np.ndarray, num_fft: int=256, sampling_rate: Union[float, int]=100):
    """plot the cross spectral density.

    Parameters
    ----------
    x: Iterable
        x_label

    s1: np.ndarray
        s1.shape = (len(x),)

    s2: np.ndarray
        s2.shape = (len(x),)

    num_fft: int
        the number of data points used in each block for the FFT.

    Returns
    -------
    fig: plt.figure() での返り値

    axs: ax のリスト
        0 -> 上の図, 1 -> 下の図
    """
    fig, axs = plt.subplots(2, 1)
    axs[0].plot(x, s1, x, s2)
    axs[0].set_ylabel('signal 1 and signal 2')

    cxy, f = axs[1].csd(s1, s2, num_fft, sampling_rate)
    axs[1].set_ylabel('CSD [dB]')
    return fig, axs