"""Numerical integration algorithms."""

from __future__ import annotations

import math
from collections.abc import Callable


def trapezoidal(
    f: Callable[[float], float],
    a: float,
    b: float,
    n: int = 100,
) -> float:
    """Approximate the definite integral of ``f`` from ``a`` to ``b``.

    The composite trapezoidal rule divides the integration interval
    into ``n`` sub-intervals of equal width ``h = (b - a) / n`` and
    approximates the integral by

        h * [(f(a) + f(b)) / 2 + sum_{i=1}^{n-1} f(a + i * h)].

    Geometrically, each sub-interval is approximated by the area under
    the line segment that connects the function values at its endpoints,
    and the rule sums these trapezoid areas. It is exact for functions
    that are piecewise linear over the grid, and its error decreases
    like O(h^2) for sufficiently smooth integrands.

    Parameters
    ----------
    f : Callable[[float], float]
        A continuous function to integrate. It must be defined (and not
        return NaN) at every grid point sampled by the rule.
    a : float
        Lower limit of integration.
    b : float
        Upper limit of integration. May be less than ``a``, in which
        case the signed integral is returned. If ``a == b``, the result
        is ``0.0``.
    n : int, optional
        Number of sub-intervals of uniform width. Must be at least 1.
        Default is ``100``.

    Returns
    -------
    float
        An approximation to the definite integral of ``f`` from ``a``
        to ``b``. The returned value is a plain Python ``float``.

    Raises
    ------
    TypeError
        If ``n`` is not an integer.
    ValueError
        If ``n < 1``.
        If ``f`` returns NaN at any sampled point.

    Notes
    -----
    The step size is computed as ``h = (b - a) / n``. The endpoint
    values ``f(a)`` and ``f(b)`` are evaluated once and enter the sum
    with weight ``1/2``; each interior value ``f(a + i * h)`` for
    ``i = 1, ..., n - 1`` is evaluated once with weight ``1``.

    The rule is signed: reversing the integration interval negates the
    result, and a zero-width interval (``a == b``) returns ``0.0``
    without evaluating ``f``.

    Examples
    --------
    >>> from numerica import trapezoidal
    >>> result = trapezoidal(lambda x: x, 0, 1, n=1000)
    >>> abs(result - 0.5) < 1e-12
    True
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")
    if n < 1:
        raise ValueError("n must be at least 1.")

    a = float(a)
    b = float(b)

    if a == b:
        return 0.0

    h = (b - a) / n

    fa = float(f(a))
    fb = float(f(b))
    if math.isnan(fa) or math.isnan(fb):
        raise ValueError("f returned NaN at an endpoint; cannot integrate.")

    total = (fa + fb) / 2.0
    for i in range(1, n):
        fi = float(f(a + i * h))
        if math.isnan(fi):
            raise ValueError(
                "f returned NaN at an interior point; cannot integrate."
            )
        total += fi

    return float(total * h)


def simpson(
    f: Callable[[float], float],
    a: float,
    b: float,
    n: int = 100,
) -> float:
    """Approximate the definite integral of ``f`` from ``a`` to ``b``.

    The composite Simpson's rule divides the integration interval into
    an even number ``n`` of sub-intervals of equal width
    ``h = (b - a) / n`` and approximates the integral by

        h/3 * [f(a) + f(b) + 4*sum(f(a + i*h), i odd) + 2*sum(f(a + i*h), i even)].

    Geometrically, each pair of adjacent sub-intervals is approximated
    by the area under the parabola that passes through the function
    values at its three nodes, and the rule sums these parabolic areas.
    It is exact for polynomials of degree no greater than three, and its
    error decreases like O(h^4) for sufficiently smooth integrands.

    Parameters
    ----------
    f : Callable[[float], float]
        A continuous function to integrate. It must be defined (and not
        return NaN) at every grid point sampled by the rule.
    a : float
        Lower limit of integration.
    b : float
        Upper limit of integration. May be less than ``a``, in which
        case the signed integral is returned. If ``a == b``, the result
        is ``0.0``.
    n : int, optional
        Number of sub-intervals of uniform width. Must be an even
        integer at least 2. Default is ``100``.

    Returns
    -------
    float
        An approximation to the definite integral of ``f`` from ``a``
        to ``b``. The returned value is a plain Python ``float``.

    Raises
    ------
    TypeError
        If ``n`` is not an integer.
    ValueError
        If ``n < 2``.
        If ``n`` is odd.
        If ``f`` returns NaN at any sampled point.

    Notes
    -----
    The step size is computed as ``h = (b - a) / n``. The endpoint
    values ``f(a)`` and ``f(b)`` are evaluated once with weight ``1``;
    each interior value ``f(a + i * h)`` for ``i = 1, ..., n - 1`` is
    evaluated once, with weight ``2`` when ``i`` is even and ``4`` when
    ``i`` is odd.

    The rule is signed: reversing the integration interval negates the
    result, and a zero-width interval (``a == b``) returns ``0.0``
    without evaluating ``f``.

    Examples
    --------
    >>> from numerica import simpson
    >>> result = simpson(lambda x: x**3, 0, 1)
    >>> abs(result - 0.25) < 1e-12
    True
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")
    if n < 2:
        raise ValueError("n must be at least 2.")
    if n % 2 != 0:
        raise ValueError("n must be even.")

    a = float(a)
    b = float(b)

    if a == b:
        return 0.0

    h = (b - a) / n

    fa = float(f(a))
    fb = float(f(b))
    if math.isnan(fa) or math.isnan(fb):
        raise ValueError("f returned NaN at an endpoint; cannot integrate.")

    total = fa + fb
    for i in range(1, n):
        fi = float(f(a + i * h))
        if math.isnan(fi):
            raise ValueError(
                "f returned NaN at an interior point; cannot integrate."
            )
        total += 4.0 * fi if i % 2 != 0 else 2.0 * fi

    return float(total * h / 3.0)