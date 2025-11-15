# -*- coding: utf-8 -*-
"""
Vectorized Monte Carlo estimation of the integral of
f(x) = 0.5*exp(x) + 1 on [a, b]

Author: Aubin RAZAFIMARO
"""

import numpy as np
from numpy import exp
from math import sqrt

def func(x):
    """Function to integrate."""
    return 0.5 * exp(x) + 1

def monte_carlo_integral(a=0.5, b=1.5, N=100_000, seed=None):
    """Estimate integral using vectorized Monte Carlo."""
    if seed is not None:
        np.random.seed(seed)
    
    # Compute max of function
    x_vals = np.linspace(a, b, 2000)
    y_vals = func(x_vals)
    Ymax = y_vals.max()

    # Generate random points
    x_random = a + np.random.rand(N) * (b - a)
    y_random = np.random.rand(N) * Ymax

    # Count points under curve
    count_under = (y_random < func(x_random)).sum()

    # Monte Carlo estimation
    area_rect = (b - a) * Ymax
    integral_est = (count_under / N) * area_rect

    return integral_est, Ymax

def primitive_func(x):
    """Exact primitive of f(x) = 0.5*exp(x) + 1."""
    return 0.5 * exp(x) + x

def exact_integral(a=0.5, b=1.5):
    return primitive_func(b) - primitive_func(a)

if __name__ == "__main__":
    a, b = 0.5, 1.5
    N = 100_000
    integral_est, Ymax = monte_carlo_integral(a, b, N, seed=42)
    integral_exact = exact_integral(a, b)
    error_rel = (integral_est - integral_exact) / integral_exact

    print(f"Monte Carlo estimate: {integral_est:.6f}")
    print(f"Exact integral      : {integral_exact:.6f}")
    print(f"Relative error      : {error_rel*100:.3f}%")
    print(f"Ymax used           : {Ymax:.6f}")
    print(f"Theoretical 1/sqrt(N): {100/sqrt(N):.3f}%")
