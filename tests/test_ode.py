"""Tests for the Euler method."""

import math

import numpy as np
import pytest

from numerica import euler


def test_euler_exponential_known_steps() -> None:
    t_values, y_values = euler(lambda t, y: y, 0.0, 1.0, 0.1, 2)
    assert t_values == pytest.approx([0.0, 0.1, 0.2])
    assert y_values == pytest.approx([1.0, 1.1, 1.21])


def test_manual_recurrence() -> None:
    f = lambda t, y: y
    _, y_values = euler(f, 0.0, 1.0, 0.1, 2)
    assert y_values[1] == pytest.approx(1.0 + 0.1 * 1.0)
    assert y_values[2] == pytest.approx(1.1 + 0.1 * 1.1)


def test_constant_derivative() -> None:
    _, y_values = euler(lambda t, y: 2.0, 0.0, 1.0, 0.5, 4)
    expected = [1.0 + 2.0 * 0.5 * i for i in range(5)]
    assert y_values == pytest.approx(expected)


def test_zero_derivative() -> None:
    t_values, y_values = euler(lambda t, y: 0.0, 1.0, 3.5, 0.2, 5)
    assert t_values == pytest.approx([1.0 + 0.2 * i for i in range(6)])
    assert y_values == pytest.approx([3.5] * 6)


def test_initial_condition_preserved() -> None:
    t_values, y_values = euler(lambda t, y: y, 2.0, -1.5, 0.1, 3)
    assert t_values[0] == 2.0
    assert y_values[0] == -1.5


def test_output_lengths() -> None:
    for n in (1, 2, 10):
        t_values, y_values = euler(lambda t, y: y, 0.0, 1.0, 0.1, n)
        assert len(t_values) == n + 1
        assert len(y_values) == n + 1


def test_t_values_increase_by_h() -> None:
    t_values, _ = euler(lambda t, y: y, 0.0, 1.0, 0.25, 4)
    assert t_values == pytest.approx([0.0, 0.25, 0.5, 0.75, 1.0])


def test_positive_h() -> None:
    t_values, y_values = euler(lambda t, y: y, 0.0, 1.0, 0.1, 3)
    assert t_values[0] < t_values[-1]
    assert y_values[0] < y_values[-1]


def test_negative_h() -> None:
    t_values, y_values = euler(lambda t, y: y, 0.1, 1.0, -0.1, 3)
    assert t_values == pytest.approx([0.1, 0.0, -0.1, -0.2])
    assert y_values == pytest.approx([1.0, 0.9, 0.81, 0.729])


def test_invalid_h_zero() -> None:
    with pytest.raises(ValueError):
        euler(lambda t, y: y, 0.0, 1.0, 0.0, 3)


def test_invalid_n_zero() -> None:
    with pytest.raises(ValueError):
        euler(lambda t, y: y, 0.0, 1.0, 0.1, 0)


def test_invalid_n_negative() -> None:
    with pytest.raises(ValueError):
        euler(lambda t, y: y, 0.0, 1.0, 0.1, -3)


def test_invalid_n_non_integer() -> None:
    with pytest.raises(TypeError):
        euler(lambda t, y: y, 0.0, 1.0, 0.1, 2.5)


def test_invalid_n_bool_true() -> None:
    with pytest.raises(TypeError):
        euler(lambda t, y: y, 0.0, 1.0, 0.1, True)


def test_invalid_n_bool_false() -> None:
    with pytest.raises(TypeError):
        euler(lambda t, y: y, 0.0, 1.0, 0.1, False)


def test_function_returns_nan() -> None:
    def f(t: float, y: float) -> float:
        return math.nan

    with pytest.raises(ValueError):
        euler(f, 0.0, 1.0, 0.1, 3)


def test_np_float64_derivative_output() -> None:
    def f(t: float, y: float) -> float:
        return np.float64(y)

    assert type(f(0.0, 0.5)) is np.float64

    t_values, y_values = euler(f, 0.0, 1.0, 0.1, 2)
    assert y_values == pytest.approx([1.0, 1.1, 1.21])
    assert all(type(v) is float for v in t_values)
    assert all(type(v) is float for v in y_values)


def test_f_called_exactly_once_per_step() -> None:
    calls = 0

    def f(t: float, y: float) -> float:
        nonlocal calls
        calls += 1
        return y

    euler(f, 0.0, 1.0, 0.1, 5)
    assert calls == 5


def test_accuracy_exponential() -> None:
    _, y_values = euler(lambda t, y: y, 0.0, 1.0, 1e-4, 10000)
    assert abs(y_values[-1] - math.exp(1.0)) <= 1e-3