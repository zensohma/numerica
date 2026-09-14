"""Numerical methods for ordinary differential equations."""

from __future__ import annotations

import math
from collections.abc import Callable


def euler(
    f: Callable[[float, float], float],
    t0: float,
    y0: float,
    h: float,
    n: int,
) -> tuple[list[float], list[float]]:
    """Solve the scalar initial value problem ``y' = f(t, y)`` with ``y(t0) = y0``.

    The explicit Euler method advances the solution with fixed step
    size ``h`` using the recurrence

        t_next = t + h
        y_next = y + h * f(t, y).

    Each step follows the tangent line of the exact solution at the
    current point. The method is first-order accurate, so the global
    error grows roughly like ``O(h)`` over the integration interval.

    Parameters
    ----------
    f : Callable[[float, float], float]
        Right-hand side of the ODE, ``f(t, y)``. It must be defined
        (and not return NaN) at every point visited by the scheme.
    t0 : float
        Initial value of the independent variable.
    y0 : float
        Initial value of the dependent variable.
    h : float
        Step size. May be positive (forward integration) or negative
        (backward integration), but must not be zero.
    n : int
        Number of Euler steps to take. Must be at least 1.

    Returns
    -------
    t_values : list[float]
        The ``n + 1`` time values ``t_i = t0 + i * h`` for
        ``i = 0, ..., n``. The first entry is ``t0``.
    y_values : list[float]
        The ``n + 1`` corresponding approximations to the solution of
        the initial value problem. The first entry is ``y0``. Both
        lists contain plain Python ``float`` values.

    Raises
    ------
    TypeError
        If ``n`` is not an integer.
    ValueError
        If ``h == 0``.
        If ``n < 1``.
        If ``f`` returns NaN at any step.

    Notes
    -----
    The right-hand side ``f`` is evaluated exactly once per step, and
    the initial condition is returned unchanged as the first entries of
    ``t_values`` and ``y_values``. The fixed-size two-sequence return
    structure is intended to be reused by higher-order explicit
    Runge-Kutta methods.

    The scheme supports backward integration with ``h < 0`` by stepping
    ``t`` toward earlier values while applying the same recurrence.

    Examples
    --------
    >>> from numerica import euler
    >>> t_values, y_values = euler(lambda t, y: y, 0.0, 1.0, 0.1, 2)
    >>> abs(y_values[-1] - 1.21) < 1e-12
    True
    """
    if h == 0:
        raise ValueError("h must be non-zero.")
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("n must be an integer.")
    if n < 1:
        raise ValueError("n must be at least 1.")

    t = float(t0)
    y = float(y0)
    h = float(h)

    t_values = [t]
    y_values = [y]

    for _ in range(n):
        fy = float(f(t, y))
        if math.isnan(fy):
            raise ValueError("f returned NaN; cannot continue integration.")
        y = y + h * fy
        t = t + h
        t_values.append(t)
        y_values.append(y)

    return t_values, y_values

