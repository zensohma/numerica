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


def newton_raphson(
    f: Callable[[float], float],
    df: Callable[[float], float],
    x0: float,
    tol: float = 1e-6,
    max_iter: int = 100,
) -> float:
    """Find a root of ``f`` using the Newton-Raphson method.

    Given a differentiable function ``f`` and its derivative ``df``,
    the Newton-Raphson method iterates

        x_{n+1} = x_n - f(x_n) / df(x_n)

    starting from an initial guess ``x0``. Each step follows the
    tangent line of ``f`` at ``x_n`` to its intersection with the
    x-axis. Near a simple root the method converges quadratically,
    but convergence is not guaranteed for arbitrary initial guesses.

    Parameters
    ----------
    f : Callable[[float], float]
        A differentiable function whose root is sought. It must be
        defined (and not return NaN) at every point sampled by the
        algorithm.
    df : Callable[[float], float]
        The derivative of ``f``. It must be defined (and not return
        NaN, inf, or zero) at every point sampled by the algorithm.
    x0 : float
        Initial guess for the root.
    tol : float, optional
        Desired stopping tolerance on the difference between successive
        iterates. Convergence is declared once
        ``abs(x_next - x) <= tol``. Must be positive. Default is
        ``1e-6``.
    max_iter : int, optional
        Maximum number of Newton iterations to perform. Must be at
        least 1. ``RuntimeError`` is raised if the stopping criterion is
        not reached within this many iterations. Default is ``100``.

    Returns
    -------
    float
        An approximation to a root of ``f``. The returned value is a
        plain Python ``float``.

    Raises
    ------
    ValueError
        If ``tol <= 0``.
        If ``max_iter < 1``.
        If ``df(x)`` is zero at any iterate, so that the iteration
        would divide by zero.
        If ``f`` or ``df`` returns NaN at any sampled point.
    RuntimeError
        If ``max_iter`` is reached without satisfying the stopping
        criterion.

    Notes
    -----
    The stopping criterion is based on successive iterates: iteration
    stops once ``abs(x_next - x) <= tol``. If ``f(x) == 0`` exactly at
    any visited point, that point is returned immediately. The
    derivative is evaluated and checked for zero before division.

    Examples
    --------
    >>> from numerica import newton_raphson
    >>> root = newton_raphson(lambda x: x**2 - 2, lambda x: 2 * x, 1.5)
    >>> abs(root - 2**0.5) < 1e-6
    True
    """
    if tol <= 0:
        raise ValueError("tol must be positive.")
    if max_iter < 1:
        raise ValueError("max_iter must be at least 1.")

    x = float(x0)
    fx = float(f(x))

    if math.isnan(fx):
        raise ValueError("f returned NaN at the initial guess.")

    if fx == 0:
        return x

    for _ in range(max_iter):
        dfx = float(df(x))

        if math.isnan(dfx):
            raise ValueError("df returned NaN; cannot continue iteration.")

        if dfx == 0:
            raise ValueError("df(x) is zero; Newton's method cannot divide by zero.")

        x_next = x - fx / dfx
        fx_next = float(f(x_next))

        if math.isnan(fx_next):
            raise ValueError("f returned NaN; cannot continue iteration.")

        if fx_next == 0:
            return float(x_next)

        if abs(x_next - x) <= tol:
            return float(x_next)

        x = x_next
        fx = fx_next

    raise RuntimeError(
        f"newton_raphson did not converge to tolerance {tol} within "
        f"{max_iter} iterations (max_iter)."
    )


def secant(
    f: Callable[[float], float],
    x0: float,
    x1: float,
    tol: float = 1e-6,
    max_iter: int = 100,
) -> float:
    """Find a root of ``f`` using the secant method.

    The secant method approximates the derivative of ``f`` by the
    slope of the secant line through the last two iterates and updates

        x_next = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))

    starting from two initial guesses ``x0`` and ``x1``. It does not
    require a derivative of ``f``. Near a simple root the method
    converges superlinearly (order approximately 1.618), but
    convergence is not guaranteed for arbitrary initial guesses.

    Parameters
    ----------
    f : Callable[[float], float]
        A continuous function whose root is sought. It must be defined
        (and not return NaN) at every point sampled by the algorithm.
    x0 : float
        First initial guess for the root.
    x1 : float
        Second initial guess for the root.
    tol : float, optional
        Desired stopping tolerance on the difference between successive
        iterates. Convergence is declared once
        ``abs(x_next - x1) <= tol``. Must be positive. Default is
        ``1e-6``.
    max_iter : int, optional
        Maximum number of secant iterations to perform. Must be at
        least 1. ``RuntimeError`` is raised if the stopping criterion
        is not reached within this many iterations. Default is ``100``.

    Returns
    -------
    float
        An approximation to a root of ``f``. The returned value is a
        plain Python ``float``.

    Raises
    ------
    ValueError
        If ``tol <= 0``.
        If ``max_iter < 1``.
        If ``f(x1) - f(x0) == 0`` at any iteration, so that the secant
        update would divide by zero.
        If ``f`` returns NaN at any sampled point.
    RuntimeError
        If ``max_iter`` is reached without satisfying the stopping
        criterion.

    Notes
    -----
    The stopping criterion is based on successive iterates: iteration
    stops once ``abs(x_next - x1) <= tol``. If ``f`` is exactly zero at
    any visited point, that point is returned immediately. The secant
    denominator is checked for zero before division.

    Examples
    --------
    >>> from numerica import secant
    >>> root = secant(lambda x: x**2 - 2, 0, 2)
    >>> abs(root - 2**0.5) < 1e-6
    True
    """
    if tol <= 0:
        raise ValueError("tol must be positive.")
    if max_iter < 1:
        raise ValueError("max_iter must be at least 1.")

    x0 = float(x0)
    x1 = float(x1)

    f0 = float(f(x0))
    if math.isnan(f0):
        raise ValueError("f returned NaN at x0.")

    if f0 == 0:
        return x0

    f1 = float(f(x1))
    if math.isnan(f1):
        raise ValueError("f returned NaN at x1.")

    if f1 == 0:
        return x1

    for _ in range(max_iter):
        if f1 == f0:
            raise ValueError(
                "f(x1) - f(x0) is zero; the secant method cannot divide by zero."
            )

        x_next = x1 - f1 * (x1 - x0) / (f1 - f0)
        f_next = float(f(x_next))

        if math.isnan(f_next):
            raise ValueError("f returned NaN; cannot continue iteration.")

        if f_next == 0:
            return float(x_next)

        if abs(x_next - x1) <= tol:
            return float(x_next)

        x0 = x1
        f0 = f1
        x1 = x_next
        f1 = f_next

    raise RuntimeError(
        f"secant did not converge to tolerance {tol} within "
        f"{max_iter} iterations (max_iter)."
    )
