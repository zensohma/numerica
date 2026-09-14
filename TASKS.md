# Numerica Development Tasks

This document tracks implementation, review, validation, and completion tasks for the Numerica project.

A task may only be marked `DONE` after all relevant requirements, acceptance criteria, and Definition of Done items have been satisfied.

---

# Phase 0 - Foundation

## TASK-001: Initialize Python Project

Status: DONE

### Requirements

- Create `src/numerica/`
- Create `src/numerica/__init__.py`
- Create `tests/`
- Create `examples/`
- Create `docs/`
- Create `pyproject.toml`
- Configure Python >= 3.10
- Configure NumPy as runtime dependency
- Configure pytest
- Configure Ruff
- Configure MyPy
- Configure build tooling

### Acceptance Criteria

- Project follows src layout
- Package can be imported
- Development dependencies are documented
- `pytest` runs successfully
- `ruff check .` runs successfully
- `mypy src` runs successfully

---

## TASK-002: Project Documentation

Status: DONE

### Requirements

- Create `README.md`
- Document project purpose
- Document installation
- Document basic usage
- Document development commands
- Document project structure

### Acceptance Criteria

- README clearly explains Numerica
- Installation instructions are present
- Example usage is present

---

# Phase 1 - Root Finding

## TASK-003: Implement Bisection Method

Status: DONE

### Public API

```python
bisection(
    f,
    a,
    b,
    tol=1e-6,
    max_iter=100,
)
```

### Requirements

- Use type hints
- Support callable functions returning Python or NumPy scalar values
- Validate interval
- Validate tolerance
- Validate maximum iterations
- Handle roots at interval endpoints
- Verify that the interval brackets a root
- Use a numerically safe sign comparison
- Use an overflow-safe midpoint calculation
- Detect NaN function values
- Implement a clear stopping criterion
- Return a plain Python `float`
- Add NumPy-style docstring
- Add unit tests
- Add edge-case tests

### Test Coverage

Tests include:

- `x**2 - 2`
- root at left endpoint
- root at right endpoint
- invalid interval
- equal endpoints
- interval that does not bracket a root
- invalid tolerance
- invalid `max_iter`
- NaN function output
- NumPy scalar output
- non-convergence
- Python `float` return type
- numerical accuracy

### Acceptance Criteria

- Implementation is mathematically correct
- Tests pass
- Ruff passes
- MyPy passes
- Public API is documented
- No unnecessary dependencies introduced

---

## TASK-004: Review Bisection Implementation

Status: DONE

### Review Scope

Review:

- mathematical correctness
- stopping criterion
- floating-point behavior
- endpoint handling
- bracketing logic
- midpoint calculation
- NaN handling
- non-convergence behavior
- API design
- error messages
- test coverage
- code readability

### Acceptance Criteria

- Mathematical implementation verified
- Numerical behavior reviewed
- Edge cases covered
- NumPy scalar compatibility verified
- No unnecessary changes introduced
- `pytest` passes
- `ruff check .` passes
- `mypy src` passes

---

## TASK-005: Implement Newton-Raphson Method

Status: DONE

### Public API

```python
newton_raphson(
    f,
    df,
    x0,
    tol=1e-6,
    max_iter=100,
)
```

### Mathematical Definition

Newton-Raphson iteration:

```text
x_next = x - f(x) / df(x)
```

or mathematically:

```text
x_(n+1) = x_n - f(x_n) / f'(x_n)
```

### Requirements

- Use type hints
- Add NumPy-style docstring
- Implement Newton-Raphson iteration
- Validate tolerance
- Validate maximum iterations
- Handle an exact root at the initial guess
- Detect zero derivative before division
- Detect NaN values returned by `f`
- Detect NaN values returned by `df`
- Use successive-iterate convergence criterion
- Handle non-convergence
- Support NumPy scalar outputs
- Return a plain Python `float`
- Add unit tests
- Add edge-case tests

### Test Coverage

Tests include:

- `x**2 - 2`
- exact root at initial guess
- invalid tolerance
- invalid `max_iter`
- zero derivative
- NaN from `f`
- NaN from `df`
- NumPy scalar outputs
- non-convergence
- Python `float` return type
- numerical accuracy

### Acceptance Criteria

- Newton-Raphson iteration is mathematically correct
- Zero derivative is handled safely
- Convergence behavior is verified
- Tests pass
- Ruff passes
- MyPy passes
- Public API is documented
- No unrelated changes introduced

---

## TASK-006: Implement Secant Method

Status: DONE

### Public API

```python
secant(
    f,
    x0,
    x1,
    tol=1e-6,
    max_iter=100,
)
```

### Mathematical Definition

Secant iteration:

```text
x_next = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
```

### Requirements

- Use type hints
- Add NumPy-style docstring
- Implement Secant iteration
- Validate tolerance
- Validate maximum iterations
- Handle roots at either initial guess
- Protect against zero secant denominator
- Detect NaN function values
- Use successive-iterate convergence criterion
- Handle non-convergence
- Support NumPy scalar outputs
- Return a plain Python `float`
- Add unit tests
- Add edge-case tests

### Test Coverage

Tests include:

- `x**2 - 2`
- exact root at `x0`
- exact root at `x1`
- invalid tolerance
- invalid `max_iter`
- zero secant denominator
- NaN function output
- NumPy scalar output
- non-convergence
- Python `float` return type
- numerical accuracy

### Acceptance Criteria

- Secant iteration is mathematically correct
- Division-by-zero case is handled
- Convergence behavior is verified
- Tests pass
- Ruff passes
- MyPy passes
- Public API is documented
- No unrelated changes introduced

---

# Phase 2 - Numerical Integration

## TASK-007: Implement Composite Trapezoidal Rule

Status: TODO

### Public API

```python
trapezoidal(
    f,
    a,
    b,
    n=100,
)
```

### Mathematical Definition

For

```text
h = (b - a) / n
```

the composite trapezoidal approximation is

```text
integral ≈ h * (
    (f(a) + f(b)) / 2
    + sum(f(a + i*h), i=1,...,n-1)
)
```

Equivalent mathematical form:

```text
∫[a,b] f(x) dx ≈
h [
    1/2 f(a)
    + Σ f(a + i h)
    + 1/2 f(b)
]
```

for

```text
i = 1, 2, ..., n-1
```

### Requirements

- Implement in `src/numerica/integration.py`
- Export from `src/numerica/__init__.py`
- Use type hints
- Use `Callable` from `collections.abc`
- Add NumPy-style docstring
- Validate `n`
- Require `n >= 1`
- Reject non-integer `n`
- Support `a < b`
- Support `a > b`
- Return `0.0` when `a == b`
- Compute step size correctly
- Evaluate endpoint contributions clearly
- Evaluate interior points correctly
- Detect NaN function values
- Support NumPy scalar function outputs
- Return a plain Python `float`
- Add unit tests
- Add edge-case tests
- Do not add adaptive integration
- Do not add vectorized APIs
- Do not modify root-finding algorithms

### Test Coverage

Tests should include:

- `f(x) = x` on `[0, 1]`
- `f(x) = x**2` on `[0, 1]`
- constant function
- reversed interval
- zero-width interval
- `n = 1`
- `n = 0`
- negative `n`
- non-integer `n`
- NaN function output
- NumPy scalar output
- Python `float` return type
- numerical accuracy with sufficiently large `n`

### Acceptance Criteria

- Composite Trapezoidal Rule is mathematically correct
- Step-size calculation is correct
- Endpoint weighting is correct
- Interior summation is correct
- Interval orientation is handled correctly
- Input validation is complete
- Tests pass
- Ruff passes
- MyPy passes
- Public API is documented
- Existing root-finding behavior remains unchanged
- No unnecessary dependencies introduced
- No unrelated changes introduced

---

## TASK-008: Review Trapezoidal Implementation

Status: TODO

### Review Scope

Review:

- mathematical formula
- step-size calculation
- endpoint weighting
- interior summation
- reversed interval behavior
- zero-width interval behavior
- handling of `n`
- floating-point behavior
- NaN handling
- NumPy scalar compatibility
- API consistency
- error messages
- test coverage
- code readability

### Acceptance Criteria

- Mathematical implementation verified
- Numerical behavior reviewed
- Edge cases covered
- NumPy scalar compatibility verified
- Existing root-finding tests remain passing
- `pytest` passes
- `ruff check .` passes
- `mypy src` passes
- No unrelated functionality introduced

---

## TASK-009: Implement Composite Simpson's Rule

Status: TODO

### Public API

```python
simpson(
    f,
    a,
    b,
    n=100,
)
```

### Mathematical Definition

For an even integer `n`,

```text
h = (b - a) / n
```

the composite Simpson approximation is

```text
integral ≈ h/3 * [
    f(a)
    + f(b)
    + 4 * sum(f(a + i*h), odd i)
    + 2 * sum(f(a + i*h), even i)
]
```

Equivalent mathematical form:

```text
∫[a,b] f(x) dx ≈
h/3 [
    f(x0)
    + 4f(x1)
    + 2f(x2)
    + 4f(x3)
    + ...
    + 2f(x_(n-2))
    + 4f(x_(n-1))
    + f(x_n)
]
```

where

```text
x_i = a + i h
```

### Requirements

- Implement in `src/numerica/integration.py`
- Export from `src/numerica/__init__.py`
- Use type hints
- Use `Callable` from `collections.abc`
- Add NumPy-style docstring
- Validate `n`
- Require `n >= 2`
- Require `n` to be even
- Reject non-integer `n`
- Support `a < b`
- Support reversed intervals
- Return `0.0` when `a == b`
- Apply correct Simpson weights
- Detect NaN function values
- Support NumPy scalar outputs
- Return a plain Python `float`
- Add unit tests
- Add edge-case tests
- Do not implement adaptive Simpson integration
- Do not modify existing numerical methods

### Test Coverage

Tests should include:

- linear function
- quadratic function
- cubic function
- constant function
- reversed interval
- zero-width interval
- minimum valid `n`
- odd `n`
- zero `n`
- negative `n`
- non-integer `n`
- NaN function output
- NumPy scalar output
- Python `float` return type
- numerical accuracy

### Acceptance Criteria

- Composite Simpson's Rule is mathematically correct
- Step-size calculation is correct
- Simpson weights are applied correctly
- Even-`n` requirement is enforced
- Reversed interval behavior is correct
- Input validation is complete
- Tests pass
- Ruff passes
- MyPy passes
- Public API is documented
- Existing numerical methods remain unchanged
- No unnecessary dependencies introduced
- No unrelated changes introduced

---

## TASK-010: Review Simpson Implementation

Status: TODO

### Review Scope

Review:

- mathematical formula
- step-size calculation
- endpoint weighting
- Simpson weights
- odd-index weighting
- even-index weighting
- even-`n` requirement
- reversed interval behavior
- zero-width interval behavior
- floating-point behavior
- NaN handling
- NumPy scalar compatibility
- API consistency
- error messages
- test coverage
- code readability

### Acceptance Criteria

- Mathematical implementation verified
- Simpson weighting verified
- Input validation reviewed
- Numerical behavior reviewed
- Edge cases covered
- NumPy scalar compatibility verified
- Existing tests remain passing
- `pytest` passes
- `ruff check .` passes
- `mypy src` passes
- No unrelated functionality introduced

---

---

# Phase 3 - Ordinary Differential Equations

## TASK-011: Implement Euler Method

Status: TODO

### Public API

```python
euler(
    f,
    t0,
    y0,
    h,
    n,
)
```

### Mathematical Definition

For the initial value problem

```text
y'(t) = f(t, y)
y(t0) = y0
```

Euler's method uses

```text
t_(k+1) = t_k + h
y_(k+1) = y_k + h * f(t_k, y_k)
```

for

```text
k = 0, 1, ..., n-1
```

### Requirements

- Implement in `src/numerica/ode.py`
- Export from `src/numerica/__init__.py`
- Use modern Python type hints
- Use `Callable` from `collections.abc`
- Add NumPy-style docstring
- Support scalar first-order ODEs only
- Validate `h`
- Reject `h == 0`
- Support positive step size
- Support negative step size
- Validate `n`
- Require `n` to be an integer
- Require `n >= 1`
- Preserve the initial condition
- Evaluate `f(t, y)` once per iteration
- Detect NaN derivative values
- Support NumPy scalar outputs from `f`
- Return two sequences: `t_values` and `y_values`
- Include the initial condition in the output
- Return exactly `n + 1` points
- Add unit tests
- Add edge-case tests
- Do not implement systems of ODEs yet
- Do not add adaptive step sizing
- Do not implement RK4 yet
- Do not modify existing numerical methods

### Return Design

For `n` steps:

```text
len(t_values) == n + 1
len(y_values) == n + 1
```

The initial entries must satisfy:

```text
t_values[0] == t0
y_values[0] == y0
```

Euler and RK4 must use the same return structure.

### Test Coverage

Tests should include:

- `y' = y`, `y(0) = 1`
- constant derivative
- zero derivative
- initial values preserved
- correct number of output points
- known manually computed Euler steps
- positive `h`
- negative `h`
- `h == 0`
- `n == 0`
- negative `n`
- non-integer `n`
- NaN derivative output
- NumPy scalar derivative output
- numerical approximation against analytical solution

### Acceptance Criteria

- Euler recurrence is mathematically correct
- Time grid is correct
- Initial condition is preserved
- Output contains exactly `n + 1` points
- Positive and negative step sizes behave correctly
- Input validation is complete
- NaN handling is correct
- NumPy scalar compatibility is verified
- Tests pass
- Ruff passes
- MyPy passes
- Public API is documented
- Existing numerical methods remain unchanged
- No unnecessary dependencies introduced
- No unrelated changes introduced

---

## TASK-012: Review Euler Method

Status: TODO

### Review Scope

Review:

- mathematical Euler recurrence
- time-step calculation
- initial condition handling
- iteration indexing
- number of returned points
- output API
- positive step behavior
- negative step behavior
- scalar ODE assumptions
- NaN handling
- NumPy scalar compatibility
- API consistency
- error messages
- floating-point behavior
- test coverage
- code readability

### Acceptance Criteria

- Mathematical implementation verified
- Euler recurrence verified
- Time stepping verified
- Initial condition behavior verified
- Output shape verified
- Positive and negative step behavior verified
- Edge cases covered
- NumPy scalar compatibility verified
- Existing tests remain passing
- `pytest` passes
- `ruff check .` passes
- `mypy src` passes
- No unrelated functionality introduced

---

## TASK-013: Implement Runge-Kutta 4 Method

Status: TODO

### Public API

```python
rk4(
    f,
    t0,
    y0,
    h,
    n,
)
```

### Mathematical Definition

For

```text
y'(t) = f(t, y)
```

compute

```text
k1 = f(t, y)

k2 = f(
    t + h/2,
    y + h*k1/2,
)

k3 = f(
    t + h/2,
    y + h*k2/2,
)

k4 = f(
    t + h,
    y + h*k3,
)
```

then

```text
y_next = y + h/6 * (
    k1
    + 2*k2
    + 2*k3
    + k4
)

t_next = t + h
```

### Requirements

- Implement in `src/numerica/ode.py`
- Export from `src/numerica/__init__.py`
- Use modern Python type hints
- Use `Callable` from `collections.abc`
- Add NumPy-style docstring
- Support scalar first-order ODEs only
- Validate `h`
- Reject `h == 0`
- Support positive step size
- Support negative step size
- Validate `n`
- Require `n` to be an integer
- Require `n >= 1`
- Implement all four RK4 stages correctly
- Evaluate stages at the correct time and state locations
- Detect NaN derivative values at any stage
- Support NumPy scalar derivative outputs
- Return the same output structure as Euler
- Preserve the initial condition
- Return exactly `n + 1` points
- Add unit tests
- Add edge-case tests
- Do not add adaptive Runge-Kutta methods
- Do not add systems of ODEs yet
- Do not modify Euler or existing numerical methods

### Test Coverage

Tests should include:

- `y' = y`, `y(0) = 1`
- constant derivative
- zero derivative
- initial condition preservation
- correct number of points
- positive step size
- negative step size
- `h == 0`
- `n == 0`
- negative `n`
- non-integer `n`
- NaN derivative at RK stages
- NumPy scalar derivative output
- manually verified single RK4 step
- numerical accuracy against analytical solution
- RK4 accuracy compared with Euler for the same step size

### Acceptance Criteria

- RK4 stages are mathematically correct
- Stage time locations are correct
- Stage state values are correct
- RK4 `1, 2, 2, 1` weighting is correct
- Time stepping is correct
- Initial condition is preserved
- Output contains exactly `n + 1` points
- Positive and negative step sizes behave correctly
- Input validation is complete
- NaN handling is correct
- NumPy scalar compatibility is verified
- Tests pass
- Ruff passes
- MyPy passes
- Public API is documented
- Existing numerical methods remain unchanged
- No unnecessary dependencies introduced
- No unrelated changes introduced

---

## TASK-014: Review Runge-Kutta 4 Method

Status: TODO

### Review Scope

Review:

- mathematical RK4 formula
- `k1`
- `k2`
- `k3`
- `k4`
- stage time locations
- stage state values
- final `1, 2, 2, 1` weighting
- time stepping
- initial condition handling
- number of returned points
- output API consistency with Euler
- positive step behavior
- negative step behavior
- NaN handling
- NumPy scalar compatibility
- API consistency
- numerical accuracy
- test coverage
- code readability

### Acceptance Criteria

- All RK4 stages verified
- Stage locations verified
- RK4 weights verified
- Numerical accuracy reviewed
- Initial condition behavior verified
- Output shape verified
- Positive and negative step behavior verified
- Edge cases covered
- NumPy scalar compatibility verified
- Existing tests remain passing
- `pytest` passes
- `ruff check .` passes
- `mypy src` passes
- No unrelated functionality introduced

# Development Rules

Only work on tasks whose status is `TODO` and which are explicitly requested.

Do not implement future tasks automatically.

Do not combine multiple tasks unless explicitly requested.

Do not modify completed numerical methods unless required to fix a verified problem.

Do not introduce unrelated refactoring while implementing a task.

Do not introduce new runtime dependencies unless explicitly approved.

Do not create Git commits unless explicitly requested.

Each task should be implemented, tested, reviewed, and approved before moving to the next task.

A task should only be marked `DONE` when all relevant acceptance criteria and Definition of Done requirements are satisfied.

---

# Development Workflow

The expected development workflow is:

```text
Requirements
    ↓
Mathematical Design
    ↓
Implementation
    ↓
Unit Tests
    ↓
Edge-Case Tests
    ↓
Code Review
    ↓
pytest
    ↓
Ruff
    ↓
MyPy
    ↓
Git Diff Review
    ↓
Task Approval
    ↓
Commit
```

For numerical algorithms, mathematical correctness must be reviewed before a task is considered complete.

---

# Numerical Implementation Principles

All numerical algorithms should prioritize:

1. Mathematical correctness
2. Numerical stability
3. Clear stopping criteria
4. Explicit input validation
5. Predictable error handling
6. API consistency
7. Type safety
8. Testability
9. Readability
10. Maintainability

Avoid unnecessary abstractions and premature optimization.

The simplest mathematically correct implementation should be preferred.

---

# Testing Principles

Each public numerical function should be tested for:

- normal usage
- mathematical correctness
- expected numerical accuracy
- boundary conditions
- invalid input
- algorithm-specific failure cases
- NumPy scalar compatibility where appropriate
- plain Python return types
- regression against existing functionality

Tests should verify mathematical behavior rather than implementation details whenever possible.

---

# Definition of Done

A task is `DONE` when all applicable items below are satisfied:

- [ ] Implementation complete
- [ ] Mathematical correctness verified
- [ ] Type hints complete
- [ ] Docstring complete
- [ ] Input validation complete
- [ ] Unit tests added
- [ ] Edge cases tested
- [ ] Numerical failure cases tested where appropriate
- [ ] NumPy scalar compatibility tested where appropriate
- [ ] Public API exported where appropriate
- [ ] Documentation added
- [ ] Example added where appropriate
- [ ] `pytest` passes
- [ ] `ruff check .` passes
- [ ] `mypy src` passes
- [ ] Existing functionality remains passing
- [ ] No unnecessary dependencies introduced
- [ ] No unrelated changes introduced
- [ ] Git diff reviewed
- [ ] Task reviewed and approved
