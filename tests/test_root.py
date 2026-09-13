"""Tests for the bisection method."""

import math

import numpy as np
import pytest

from numerica import bisection, newton_raphson, secant


def test_math_correctness() -> None:
    root = bisection(lambda x: x**2 - 2, 0, 2)
    assert abs(root - math.sqrt(2)) <= 1e-6


def test_root_exactly_at_a() -> None:
    assert bisection(lambda x: x, 0, 2) == 0


def test_root_exactly_at_b() -> None:
    assert bisection(lambda x: x - 1, 0, 1) == 1


def test_invalid_interval() -> None:
    with pytest.raises(ValueError):
        bisection(lambda x: x**2 - 2, 2, 0)


def test_equal_endpoints_is_invalid() -> None:
    with pytest.raises(ValueError):
        bisection(lambda x: x**2 - 2, 1, 1)


def test_interval_does_not_bracket_root() -> None:
    with pytest.raises(ValueError):
        bisection(lambda x: x**2 + 1, 0, 2)


def test_nonpositive_tolerance() -> None:
    with pytest.raises(ValueError):
        bisection(lambda x: x**2 - 2, 0, 2, tol=0)
    with pytest.raises(ValueError):
        bisection(lambda x: x**2 - 2, 0, 2, tol=-1)


def test_zero_max_iter() -> None:
    with pytest.raises(ValueError):
        bisection(lambda x: x**2 - 2, 0, 2, max_iter=0)


def test_max_iter_too_small_does_not_converge() -> None:
    with pytest.raises(RuntimeError) as exc:
        bisection(lambda x: x**2 - 2, 0, 2, tol=1e-12, max_iter=1)
    assert "max_iter" in str(exc.value)



def test_function_returns_nan() -> None:
    def f(x: float) -> float:
        return math.nan

    with pytest.raises(ValueError):
        bisection(f, 0, 2)


def test_numpy_scalar_function_output() -> None:
    def f(x: float) -> float:
        return np.float64(x**2 - 2)

    assert type(f(0)) is np.float64

    root = bisection(f, 0, 2)
    assert isinstance(root, float)
    assert abs(root - math.sqrt(2)) <= 1e-6


def test_returns_plain_python_float() -> None:
    root = bisection(lambda x: x**2 - 2, 0, 2)
    assert type(root) is float


def test_numerical_accuracy() -> None:
    root = bisection(lambda x: x**2 - 2, 0, 2, tol=1e-9, max_iter=200)
    assert abs(root - math.sqrt(2)) <= 1e-9


def test_newton_math_correctness() -> None:
    root = newton_raphson(lambda x: x**2 - 2, lambda x: 2 * x, 1.5)
    assert abs(root - math.sqrt(2)) <= 1e-6


def test_newton_exact_root_at_initial_guess() -> None:
    assert newton_raphson(lambda x: x, lambda x: 1, 0) == 0


def test_newton_nonpositive_tolerance() -> None:
    with pytest.raises(ValueError):
        newton_raphson(lambda x: x**2 - 2, lambda x: 2 * x, 1.5, tol=0)
    with pytest.raises(ValueError):
        newton_raphson(lambda x: x**2 - 2, lambda x: 2 * x, 1.5, tol=-1)


def test_newton_zero_max_iter() -> None:
    with pytest.raises(ValueError):
        newton_raphson(lambda x: x**2 - 2, lambda x: 2 * x, 1.5, max_iter=0)


def test_newton_zero_derivative() -> None:
    with pytest.raises(ValueError):
        newton_raphson(lambda x: x**2 + 1, lambda x: 2 * x, 0)


def test_newton_function_returns_nan() -> None:
    def f(x: float) -> float:
        return math.nan

    with pytest.raises(ValueError):
        newton_raphson(f, lambda x: 1.0, 0)


def test_newton_derivative_returns_nan() -> None:
    def df(x: float) -> float:
        return math.nan

    with pytest.raises(ValueError):
        newton_raphson(lambda x: x**2 - 2, df, 1.5)


def test_newton_numpy_scalar_function_output() -> None:
    def f(x: float) -> float:
        return np.float64(x**2 - 2)

    def df(x: float) -> float:
        return np.float64(2 * x)

    assert type(df(0)) is np.float64

    root = newton_raphson(f, df, 1.5)
    assert isinstance(root, float)
    assert abs(root - math.sqrt(2)) <= 1e-6


def test_newton_max_iter_too_small_does_not_converge() -> None:
    with pytest.raises(RuntimeError) as exc:
        newton_raphson(lambda x: x**2 - 2, lambda x: 2 * x, 1.5, tol=1e-12, max_iter=1)
    assert "max_iter" in str(exc.value)


def test_newton_returns_plain_python_float() -> None:
    root = newton_raphson(lambda x: x**2 - 2, lambda x: 2 * x, 1.5)
    assert type(root) is float


def test_newton_numerical_accuracy() -> None:
    root = newton_raphson(
        lambda x: x**2 - 2, lambda x: 2 * x, 1.5, tol=1e-10, max_iter=50
    )
    assert abs(root - math.sqrt(2)) <= 1e-10


def test_secant_math_correctness() -> None:
    root = secant(lambda x: x**2 - 2, 0, 2)
    assert abs(root - math.sqrt(2)) <= 1e-6


def test_secant_exact_root_at_x0() -> None:
    assert secant(lambda x: x, 0, 2) == 0


def test_secant_exact_root_at_x1() -> None:
    assert secant(lambda x: x - 1, 0, 1) == 1


def test_secant_nonpositive_tolerance() -> None:
    with pytest.raises(ValueError):
        secant(lambda x: x**2 - 2, 0, 2, tol=0)
    with pytest.raises(ValueError):
        secant(lambda x: x**2 - 2, 0, 2, tol=-1)


def test_secant_zero_max_iter() -> None:
    with pytest.raises(ValueError):
        secant(lambda x: x**2 - 2, 0, 2, max_iter=0)


def test_secant_zero_denominator() -> None:
    with pytest.raises(ValueError):
        secant(lambda x: 1.0, 0, 2)


def test_secant_function_returns_nan() -> None:
    def f(x: float) -> float:
        return math.nan

    with pytest.raises(ValueError):
        secant(f, 0, 2)


def test_secant_max_iter_too_small_does_not_converge() -> None:
    with pytest.raises(RuntimeError) as exc:
        secant(lambda x: x**2 - 2, 0, 2, tol=1e-12, max_iter=1)
    assert "max_iter" in str(exc.value)


def test_secant_numpy_scalar_function_output() -> None:
    def f(x: float) -> float:
        return np.float64(x**2 - 2)

    assert type(f(0)) is np.float64

    root = secant(f, 0, 2)
    assert isinstance(root, float)
    assert abs(root - math.sqrt(2)) <= 1e-6


def test_secant_returns_plain_python_float() -> None:
    root = secant(lambda x: x**2 - 2, 0, 2)
    assert type(root) is float


def test_secant_numerical_accuracy() -> None:
    root = secant(lambda x: x**2 - 2, 0, 2, tol=1e-10, max_iter=100)
    assert abs(root - math.sqrt(2)) <= 1e-10
