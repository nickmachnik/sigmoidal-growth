#!/usr/bin/env python

import numpy as np
from scipy.optimize import curve_fit
from scipy.misc import derivative


def _center_data(data: array_like) -> array_like:
    """Center the input data around the median value between min and max.
    
    Args:
        data (array_like): Data with approximately sigmoidal shape.
    
    Returns:
        array_like: x-values of the centered data, centered around 0.
        array_like: Centered data.
    """
    # truncate at maximum
    data = data[:np.argmax(data) + 1]
    half_max = (data[-1] + np.min(data)) / 2
    len_upper_half = len(data) - (np.argmax(data > half_max))
    x = np.arange(-len_upper_half, len_upper_half)
    return x, data[-(len_upper_half*2):]


def max_growth_rate(y_data: array_like) -> (float, float):
    """Determine maximal slope in data by fitting a sigmoid function.
    
    Args:
        y_data (array_like): Population density, as measured sequentially in time.
    
    Returns:
        float: The maximum of the first derivative of the fitted sigmoid.
        float: The mean squared deviation from the y_data.
    """
    def sigmoid(x, b):
        y = A + ((L - A) / (1 + np.exp(-b*(x-a))))
        return y
    
    X, y_data = _center_data(y_data)
    A = np.min(y_data)
    L = np.max(y_data)
    a = 0
    popt, pcov = curve_fit(sigmoid, X, y_data)
    msd = np.mean((sigmoid(X, *popt) - y_data) ** 2)
    der1 = derivative(sigmoid, X, n=1, dx=1, args=popt)
    m = np.max(der1)
    
    return m, msd