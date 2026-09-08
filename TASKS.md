# Tasks

# Numerica Development Tasks

## Phase 0 - Foundation

### TASK-001: Initialize Python Project

Status: DONE

Requirements:

* Create `src/numerica/`
* Create `src/numerica/__init__.py`
* Create `tests/`
* Create `examples/`
* Create `docs/`
* Create `pyproject.toml`
* Configure Python >= 3.10
* Configure NumPy as runtime dependency
* Configure pytest
* Configure Ruff
* Configure MyPy
* Configure build tooling

Acceptance Criteria:

* Project follows src layout
* Package can be imported
* Development dependencies are documented
* `pytest` runs successfully
* `ruff check .` runs successfully
* `mypy src` runs successfully

---

### TASK-002: Project Documentation

Status: DONE

Requirements:

* Create README.md
* Document project purpose
* Document installation
* Document basic usage
* Document development commands
* Document project structure

Acceptance Criteria:

* README clearly explains Numerica
* Installation instructions are present
* Example usage is present

---

# Phase 1 - Root Finding

### TASK-003: Implement Bisection Method

Status: TODO

Requirements:

Implement:

```python
bisection(
    f,
    a,
    b,
    tol=1e-6,
    max_iter=100,
)
```

Requirements:

* Use type hints
* Add NumPy-compatible callable support where appropriate
* Validate input
* Handle endpoint roots
* Validate tolerance
* Validate maximum iterations
* Verify that the interval brackets a root
* Implement a clear stopping criterion
* Document the mathematical method
* Add unit tests
* Add edge-case tests

Test cases should include:

* `x² - 2`
* root at left endpoint
* root at right endpoint
* invalid interval
* invalid tolerance
* invalid max_iter
* convergence behavior

Acceptance Criteria:

* Implementation is mathematically correct
* Tests pass
* Ruff passes
* MyPy passes
* Public API is documented
* No unnecessary dependencies are introduced

---

### TASK-004: Review Bisection Implementation

Status: TODO

Review:

* mathematical correctness
* stopping criterion
* floating-point behavior
* edge cases
* API design
* error messages
* test coverage
* code readability

Do not add new functionality unless required to fix a problem.

---

### TASK-005: Implement Newton-Raphson

Status: TODO

Implement:

```python
newton_raphson(
    f,
    df,
    x0,
    tol=1e-6,
    max_iter=100,
)
```

Requirements:

* type hints
* docstring
* derivative handling
* convergence criterion
* zero derivative handling
* max iteration handling
* unit tests
* edge-case tests
* documentation
* example

---

### TASK-006: Implement Secant Method

Status: TODO

Implement:

```python
secant(
    f,
    x0,
    x1,
    tol=1e-6,
    max_iter=100,
)
```

Requirements:

* type hints
* docstring
* convergence criterion
* division-by-zero protection
* max iteration handling
* unit tests
* edge-case tests
* documentation
* example

---

# Development Rule

Only work on tasks whose status is `TODO` and explicitly requested.

Do not implement future tasks automatically.

A task should only be marked complete when all acceptance criteria are satisfied.

---

# Definition of Done

A task is DONE when:

* [ ] Implementation complete
* [ ] Mathematical correctness verified
* [ ] Type hints complete
* [ ] Docstring complete
* [ ] Unit tests added
* [ ] Edge cases tested
* [ ] Documentation added
* [ ] Example added where appropriate
* [ ] `pytest` passes
* [ ] `ruff check .` passes
* [ ] `mypy src` passes
* [ ] No unrelated changes introduced
