"""Root-finding algorithms."""

from __future__ import annotations

import math
from collections.abc import Callable


def bisection(
    f: Callable[[float], float],
    a: float,
    b: float,
    tol: float = 1e-6,
    max_iter: int = 100,
) -> float:
    """Find a root of ``f`` in the interval ``[a, b]`` using the bisection method.

    The bisection method repeatedly halves the interval ``[a, b]``,
    keeping the sub-interval that still brackets a root of ``f``. It is
    robust (it always converges when the initial interval brackets a
    root) but converges only linearly.

    Parameters
    ----------
    f : Callable[[float], float]
        A continuous function whose root is sought. It must be defined
        (and return a finite numerical value) at every point sampled by
        the algorithm.
    a : float
        Left endpoint of the initial interval. Must satisfy ``a < b``.
    b : float
        Right endpoint of the initial interval. Must satisfy ``a < b``.
    tol : float, optional
        Desired stopping tolerance on the interval width. Convergence is
        declared once ``abs(b - a) <= tol``. Must be positive.
        Default is ``1e-6``.
    max_iter : int, optional
        Maximum number of bisection iterations to perform. Must be at
        least 1. ``RuntimeError`` is raised if the stopping criterion is
        not reached within this many iterations. Default is ``100``.

    Returns
    -------
    float
        An approximation to a root of ``f`` within the interval
        ``[a, b]``. The returned value is a plain Python ``float``.

    Raises
    ------
    ValueError
        If ``a >= b``.
        If ``tol <= 0``.
        If ``max_iter < 1``.
        If the interval ``[a, b]`` does not bracket a root of ``f``
        (that is, if ``f(a)`` and ``f(b)`` have the same sign).
        If ``f`` returns a NaN at any sampled point.
    RuntimeError
        If ``max_iter`` is reached without satisfying the stopping
        criterion.

    Notes
    -----
    The stopping criterion is the interval width: iteration continues
    until ``abs(b - a) <= tol``. Because the true root always remains
    inside the current interval, this provides a guaranteed error bound
    on the returned approximation.

    If ``f(a) == 0`` or ``f(b) == 0``, the corresponding endpoint is
    returned immediately, before the bracketing check. The midpoint is
    computed as ``a + (b - a) / 2`` to avoid overflow when ``a`` and
    ``b`` are large and of similar magnitude.

    Examples
    --------
    >>> from numerica import bisection
    >>> root = bisection(lambda x: x**2 - 2, 0, 2)
    >>> abs(root - 2**0.5) < 2e-6
    True
    """
    if a >= b:
        raise ValueError("a must be strictly less than b.")
    if tol <= 0:
        raise ValueError("tol must be positive.")
    if max_iter < 1:
        raise ValueError("max_iter must be at least 1.")

    fa = float(f(a))
    if fa == 0:
        return a

    fb = float(f(b))
    if fb == 0:
        return b

    if math.isnan(fa) or math.isnan(fb):
        raise ValueError("f returned NaN; cannot bracket a root.")

    if (fa < 0) == (fb < 0):
        raise ValueError("f(a) and f(b) must have opposite signs.")

    for _ in range(max_iter):
        c = a + (b - a) / 2
        fc = float(f(c))

        if math.isnan(fc):
            raise ValueError("f returned NaN; cannot continue iteration.")

        if fc == 0:
            return c

        if (fa < 0) != (fc < 0):
            b = c
            fb = fc
        else:
            a = c
            fa = fc

        if abs(b - a) <= tol:
            return float(a + (b - a) / 2)

    raise RuntimeError(
        f"bisection did not converge to tolerance {tol} within "
        f"{max_iter} iterations (max_iter)."
    )
