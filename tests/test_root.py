"""Tests for the bisection method."""

import math

import numpy as np
import pytest

from numerica import bisection


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

    root = bisection(f, 0, 2)
    assert isinstance(root, float)
    assert abs(root - math.sqrt(2)) <= 1e-6


def test_returns_plain_python_float() -> None:
    root = bisection(lambda x: x**2 - 2, 0, 2)
    assert type(root) is float


def test_numerical_accuracy() -> None:
    root = bisection(lambda x: x**2 - 2, 0, 2, tol=1e-9, max_iter=200)
    assert abs(root - math.sqrt(2)) <= 1e-9
