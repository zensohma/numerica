"""Tests for the trapezoidal and Simpson's rules."""

import math

import numpy as np
import pytest

from numerica import simpson, trapezoidal


def test_linear_function() -> None:
    assert trapezoidal(lambda x: x, 0, 1) == pytest.approx(0.5)


def test_quadratic_function() -> None:
    result = trapezoidal(lambda x: x**2, 0, 1, n=10000)
    assert result == pytest.approx(1 / 3, abs=1e-8)


def test_constant_function() -> None:
    assert trapezoidal(lambda x: 3.0, 0, 2) == pytest.approx(6.0)


def test_reversed_interval() -> None:
    assert trapezoidal(lambda x: x, 1, 0) == pytest.approx(-0.5)
    assert trapezoidal(lambda x: x**2, 0, 1) == pytest.approx(
        -trapezoidal(lambda x: x**2, 1, 0), abs=1e-12
    )


def test_zero_width_interval() -> None:
    assert trapezoidal(lambda x: x**2, 1, 1) == 0.0


def test_single_subinterval() -> None:
    assert trapezoidal(lambda x: x, 0, 1, n=1) == pytest.approx(0.5)


def test_invalid_n_zero() -> None:
    with pytest.raises(ValueError):
        trapezoidal(lambda x: x, 0, 1, n=0)


def test_invalid_n_negative() -> None:
    with pytest.raises(ValueError):
        trapezoidal(lambda x: x, 0, 1, n=-1)


def test_invalid_n_non_integer() -> None:
    with pytest.raises(TypeError):
        trapezoidal(lambda x: x, 0, 1, n=2.5)


def test_function_returns_nan() -> None:
    def f(x: float) -> float:
        return math.nan

    with pytest.raises(ValueError):
        trapezoidal(f, 0, 2)


def test_function_returns_nan_at_interior_point() -> None:
    def f(x: float) -> float:
        if 0 < x < 1:
            return math.nan
        return 0.0

    with pytest.raises(ValueError):
        trapezoidal(f, 0, 1)


def test_numpy_scalar_function_output() -> None:
    def f(x: float) -> float:
        return np.float64(x**2)

    assert type(f(0.5)) is np.float64

    result = trapezoidal(f, 0, 1, n=10000)
    assert isinstance(result, float)
    assert result == pytest.approx(1 / 3, abs=1e-8)


def test_returns_plain_python_float() -> None:
    result = trapezoidal(lambda x: x**2, 0, 1)
    assert type(result) is float


def test_numerical_accuracy() -> None:
    result = trapezoidal(math.sin, 0, math.pi, n=100000)
    assert abs(result - 2.0) <= 1e-8


def test_simpson_constant_function() -> None:
    assert simpson(lambda x: 3.0, 0, 2) == pytest.approx(6.0)


def test_simpson_linear_function() -> None:
    assert simpson(lambda x: x, 0, 1) == pytest.approx(0.5)


def test_simpson_quadratic_function() -> None:
    result = simpson(lambda x: x**2, 0, 1)
    assert result == pytest.approx(1 / 3)


def test_simpson_cubic_function() -> None:
    result = simpson(lambda x: x**3, 0, 1)
    assert result == pytest.approx(0.25)


def test_simpson_reversed_interval() -> None:
    assert simpson(lambda x: x, 1, 0) == pytest.approx(-0.5)
    assert simpson(lambda x: x**2, 0, 1) == pytest.approx(
        -simpson(lambda x: x**2, 1, 0), abs=1e-12
    )


def test_simpson_zero_width_interval() -> None:
    assert simpson(lambda x: x**2, 1, 1) == 0.0


def test_simpson_minimum_valid_n() -> None:
    assert simpson(lambda x: x**3, 0, 1, n=2) == pytest.approx(0.25)


def test_simpson_invalid_n_odd() -> None:
    with pytest.raises(ValueError):
        simpson(lambda x: x, 0, 1, n=3)


def test_simpson_invalid_n_zero() -> None:
    with pytest.raises(ValueError):
        simpson(lambda x: x, 0, 1, n=0)


def test_simpson_invalid_n_negative() -> None:
    with pytest.raises(ValueError):
        simpson(lambda x: x, 0, 1, n=-2)


def test_simpson_invalid_n_non_integer() -> None:
    with pytest.raises(TypeError):
        simpson(lambda x: x, 0, 1, n=2.5)


def test_simpson_function_returns_nan() -> None:
    def f(x: float) -> float:
        return math.nan

    with pytest.raises(ValueError):
        simpson(f, 0, 2)


def test_simpson_function_returns_nan_at_interior_point() -> None:
    def f(x: float) -> float:
        if 0 < x < 1:
            return math.nan
        return 0.0

    with pytest.raises(ValueError):
        simpson(f, 0, 1)


def test_simpson_numpy_scalar_function_output() -> None:
    def f(x: float) -> float:
        return np.float64(x**3)

    assert type(f(0.5)) is np.float64

    result = simpson(f, 0, 1)
    assert isinstance(result, float)
    assert result == pytest.approx(0.25)


def test_simpson_returns_plain_python_float() -> None:
    result = simpson(lambda x: x**3, 0, 1)
    assert type(result) is float


def test_simpson_numerical_accuracy() -> None:
    result = simpson(math.sin, 0, math.pi, n=1000)
    assert abs(result - 2.0) <= 1e-8