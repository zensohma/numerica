# Roadmap

# Numerica

## Phase 0 - Foundation

Goal: establish the project infrastructure.

* [x] Create repository
* [x] Initialize Git
* [x] Create Python project
* [x] Create src layout
* [x] Configure pyproject.toml
* [x] Configure development environment
* [x] Add AGENTS.md
* [x] Add PRD.md
* [x] Add ARCHITECTURE.md
* [x] Add ROADMAP.md
* [x] Add TASKS.md
* [x] Add README.md
* [x] Add LICENSE
* [x] Add .gitignore

---

# Phase 1 - Root Finding

Target: `v0.1.0-alpha`

Implement:

* [ ] Bisection
* [ ] Newton-Raphson
* [ ] Secant

For each method:

* [ ] Implementation
* [ ] Type hints
* [ ] Docstring
* [ ] Unit tests
* [ ] Edge-case tests
* [ ] Mathematical validation
* [ ] Documentation
* [ ] Example

---

# Phase 2 - Numerical Integration

Target: `v0.1.0-beta`

Implement:

* [ ] Trapezoidal Rule
* [ ] Simpson's Rule

Testing:

* [ ] Polynomial functions
* [ ] Trigonometric functions
* [ ] Known analytical integrals
* [ ] Invalid input
* [ ] Numerical accuracy

---

# Phase 3 - ODE

Target: `v0.1.0-rc`

Implement:

* [ ] Euler Method
* [ ] Runge-Kutta 4

Testing:

* [ ] Exponential equations
* [ ] Logistic equations
* [ ] Analytical solutions
* [ ] Step-size behavior

---

# Phase 4 - Release Preparation

Target: `v0.1.0`

* [ ] Complete documentation
* [ ] Complete examples
* [ ] Review public API
* [ ] Ruff
* [ ] MyPy
* [ ] Pytest
* [ ] GitHub Actions
* [ ] Build package
* [ ] Test source distribution
* [ ] Test wheel
* [ ] Test clean installation
* [ ] TestPyPI
* [ ] PyPI release

---

# Phase 5 - Linear Algebra

Target: `v0.2.0`

* [ ] Gaussian Elimination
* [ ] LU Decomposition
* [ ] QR Decomposition
* [ ] Jacobi Method
* [ ] Gauss-Seidel
* [ ] Power Iteration
* [ ] Eigenvalue Methods

---

# Phase 6 - Interpolation

Target: `v0.3.0`

* [ ] Lagrange Interpolation
* [ ] Newton Interpolation
* [ ] Polynomial Interpolation
* [ ] Spline Interpolation

---

# Phase 7 - Optimization

Target: `v0.4.0`

* [ ] Gradient Descent
* [ ] Newton Optimization
* [ ] Coordinate Descent
* [ ] Simulated Annealing
* [ ] Genetic Algorithm
* [ ] Constraint Optimization

---

# Phase 8 - PDE

Target: `v0.5.0+`

* [ ] Finite Difference
* [ ] Heat Equation
* [ ] Wave Equation
* [ ] Laplace Equation
* [ ] Poisson Equation
* [ ] Boundary Conditions

---

# Phase 9 - Production Quality

* [ ] Benchmark suite
* [ ] Performance profiling
* [ ] API stability
* [ ] Extended documentation
* [ ] Contribution guide
* [ ] Issue templates
* [ ] Pull request template
* [ ] Automated release
* [ ] Changelog automation

---

# Long-Term Vision

```text
Numerica
│
├── Numerical Analysis
├── Linear Algebra
├── Optimization
├── ODE
├── PDE
├── Probability
├── Statistics
└── Mathematical Modeling
```

The project should grow incrementally.

Do not implement future phases before the current phase is stable.
