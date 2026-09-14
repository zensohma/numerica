"""Numerica: numerical methods for applied mathematics."""

from numerica.integration import simpson, trapezoidal
from numerica.ode import euler
from numerica.root import bisection, newton_raphson, secant

__all__: list[str] = [
    "bisection",
    "euler",
    "newton_raphson",
    "secant",
    "simpson",
    "trapezoidal",
]