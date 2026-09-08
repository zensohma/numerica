# Numerica

Numerica is a Python library for numerical methods in applied mathematics.

It aims to provide implementations of classical numerical algorithms through a
simple, consistent, and well-tested Python API. The focus is on educational
value, mathematical correctness, usability, and extensibility, making the
library suitable for students, researchers, engineers, and developers.

## Project Purpose

Students and practitioners often need numerical methods for solving
mathematical problems but encounter implementations that are inconsistent,
poorly documented, or difficult to validate. Numerica provides clean,
documented, and tested implementations of commonly used numerical methods in
one Python package.

## Status

- Version: `0.1.0` (pre-release)
- Phase 0 (project foundation) is complete.
- Planned methods for v0.1: bisection, Newton-Raphson, and secant (root
  finding); the trapezoidal rule and Simpson's rule (numerical integration);
  the Euler method and Runge-Kutta 4 (ordinary differential equations).
- None of the numerical methods are implemented yet. See `ROADMAP.md` for the
  development plan and `PRD.md` for the planned API.

## Installation

The package is not published to PyPI yet.

To install in development mode (during development):

```bash
python -m pip install -e ".[dev]"
```

To install the package without development dependencies:

```bash
python -m pip install -e .
```

## Basic Usage

The package is importable but currently provides no public API.

```python
import numerica
```

The planned API (from `PRD.md`) will look like this once the methods are
implemented:

```python
from numerica import bisection

root = bisection(
    lambda x: x**2 - 2,
    0,
    2,
)
```

## Development Setup

Requirements: Python 3.10+.

1. Create and activate a virtual environment.
2. Install the package with development dependencies:

   ```bash
   python -m pip install -e ".[dev]"
   ```

Development dependencies:

- `pytest` — test runner
- `ruff` — linter
- `mypy` — static type checker
- `build` — package build tooling

The runtime dependency is NumPy.

## Testing Commands

```bash
python -m pytest -q
python -m ruff check .
python -m mypy src
```

## Project Structure

```text
numerica/
├── src/
│   └── numerica/        # package source
│       └── __init__.py
├── tests/               # unit tests
├── examples/            # usage examples
├── docs/                # project documentation
├── AGENTS.md
├── PRD.md
├── ARCHITECTURE.md      # target layout and design decisions
├── ROADMAP.md
├── TASKS.md
├── README.md
├── LICENSE
├── pyproject.toml
└── .gitignore
```

## Roadmap Summary

- Phase 0: Project foundation (current). Complete.
- Phase 1: Root finding (bisection, Newton-Raphson, secant) targeting
  `v0.1.0-alpha`.
- Phase 2: Numerical integration (trapezoidal and Simpson's rules) targeting
  `v0.1.0-beta`.
- Phase 3: ODE solvers (Euler and Runge-Kutta 4) targeting `v0.1.0-rc`.
- Phase 4: Release preparation targeting `v0.1.0`.

Later phases cover linear algebra, interpolation, optimization, and PDEs. See
`ROADMAP.md` for details.

## License

MIT. See `LICENSE`.