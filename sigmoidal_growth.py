#!/usr/bin/env python

import numpy as np
from scipy.optimize import curve_fit
from scipy.misc import derivative

def _center_data(data):
    """Summary
    
    Args:
        data (TYPE): Description
    
    Returns:
        TYPE: Description
    """
    half_max = (data[-1] + np.min(data)) / 2
    for index, num in enumerate(data):
        if num > half_max:
            return np.arange(-index, -index + len(data))

def _truncate_data(data):
    """
    Truncate data such that the halfmax value is the median.
    
    Args:
        data (TYPE): Description
    
    Returns:
        TYPE: Description
    """
    data = data[:np.argmax(data) + 1]
    x = center_data(data)
    return x[-x[-1] * 2:], data[-x[-1] * 2:]

def max_growth_rate(y_data):
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
    
    X, y_data = truncate_data(y_data)
    A = np.min(y_data)
    L = np.max(y_data)
    a = 0
    popt, pcov = curve_fit(sigmoid, X, y_data)
    msd = np.mean((sigmoid(X, *popt) - y_data) ** 2)
    der1 = derivative(sigmoid, X, n=1, dx=1, args=popt)
    m = np.max(der1)
    
    return m, msd