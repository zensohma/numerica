# Architecture

# Numerica

## 1. Architecture Principles

Numerica follows these principles:

### Simple

The API should be easy to learn.

### Modular

Different mathematical domains should be separated into independent modules.

### Testable

Algorithms should be easy to test independently.

### Extensible

New numerical methods should be added without modifying unrelated modules.

### Mathematically Correct

Implementation decisions must respect the mathematical definition of each algorithm.

### Type Safe

Public APIs should use type hints.

---

## 2. Project Structure

```text
numerica/
│
├── src/
│   └── numerica/
│       ├── __init__.py
│       ├── root.py
│       ├── integration.py
│       └── ode.py
│
├── tests/
│   ├── test_root.py
│   ├── test_integration.py
│   └── test_ode.py
│
├── examples/
│   ├── root_finding.py
│   ├── integration.py
│   └── ode.py
│
├── docs/
│
├── PRD.md
├── ARCHITECTURE.md
├── ROADMAP.md
├── TASKS.md
├── AGENTS.md
│
├── README.md
├── LICENSE
├── pyproject.toml
└── .gitignore
```

---

## 3. Source Architecture

### root.py

Contains root-finding algorithms:

* Bisection
* Newton-Raphson
* Secant

### integration.py

Contains numerical integration algorithms:

* Trapezoidal Rule
* Simpson's Rule

### ode.py

Contains ordinary differential equation solvers:

* Euler
* RK4

---

## 4. API Design

Numerica v0.1 uses a functional API.

Example:

```python
from numerica import bisection

root = bisection(
    lambda x: x**2 - 2,
    0,
    2,
)
```

The API should remain lightweight.

Avoid introducing result classes or complex abstractions unless there is a demonstrated need.

---

## 5. Dependencies

Runtime:

```text
NumPy
```

Development:

```text
pytest
ruff
mypy
build
```

Avoid unnecessary dependencies.

---

## 6. Error Handling

Invalid mathematical conditions should raise clear exceptions.

Example:

```python
ValueError(
    "f(a) and f(b) must have opposite signs."
)
```

Error messages should explain what the user needs to fix.

---

## 7. Numerical Considerations

Implementations should consider:

* floating-point precision
* convergence criteria
* division by zero
* invalid intervals
* invalid step sizes
* maximum iterations
* numerical stability

Stopping criteria must be explicitly defined and documented.

---

## 8. Testing Architecture

Each public numerical method should have a corresponding test module.

Tests should verify:

```text
Mathematical correctness
        ↓
Boundary cases
        ↓
Invalid input
        ↓
Convergence
        ↓
Numerical behavior
```

Known analytical solutions should be used whenever possible.

---

## 9. Documentation Architecture

Each numerical method should eventually have:

```text
Definition
↓
Mathematical intuition
↓
Formula
↓
Algorithm
↓
Python API
↓
Example
↓
Limitations
```

---

## 10. Versioning

Numerica follows Semantic Versioning:

```text
MAJOR.MINOR.PATCH
```

Examples:

```text
0.1.0
0.2.0
1.0.0
```

Breaking API changes require an appropriate version increment.

---

## 11. Future Architecture

As the project grows:

```text
numerica/
│
├── root
├── integration
├── ode
├── linalg
├── interpolation
├── optimization
├── pde
├── probability
├── statistics
└── modeling
```

The architecture should evolve only when project complexity requires it.
