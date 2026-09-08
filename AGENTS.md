# AGENTS.md

## Project

Numerica is a Python library for numerical methods in applied mathematics.

The goal is to provide numerical algorithms that are:

* mathematically correct
* easy to understand
* easy to use
* well tested
* type-safe
* well documented
* maintainable
* suitable for students, researchers, engineers, and developers

---

## Role

Act as a senior Python software engineer and numerical analyst.

When implementing mathematical algorithms, prioritize:

1. Mathematical correctness
2. Numerical stability
3. API consistency
4. Testability
5. Type safety
6. Readability
7. Documentation
8. Maintainability

Do not optimize prematurely.

---

## Project Documents

Before making significant changes, read:

* `PRD.md`
* `ARCHITECTURE.md`
* `ROADMAP.md`
* `TASKS.md`

These files define the project requirements and development direction.

Do not contradict decisions defined in these documents without explaining why.

---

## Scope Control

Only implement the task currently being worked on.

Do not:

* implement future roadmap features
* introduce unnecessary abstractions
* add unnecessary dependencies
* rewrite unrelated code
* modify APIs without justification
* create features that were not requested

If a task is ambiguous, inspect the project documentation first.

If ambiguity remains, explain the ambiguity before making a major architectural decision.

---

## Mathematical Implementation

For every numerical algorithm:

1. Understand the mathematical definition.
2. Identify assumptions and conditions.
3. Define the stopping criterion.
4. Consider numerical precision and floating-point behavior.
5. Handle important edge cases.
6. Implement the algorithm clearly.
7. Write tests against known mathematical results.

Do not blindly translate pseudocode into Python.

---

## Python Standards

Use modern Python.

Target Python version:

Python 3.10+

Use:

* type hints
* clear function names
* descriptive docstrings
* `collections.abc` where appropriate
* small, focused functions
* explicit error handling

Avoid:

* unnecessary classes
* global mutable state
* unnecessary dependencies
* overly clever code
* premature optimization

---

## Public API

Every public function must have:

* type hints
* docstring
* clear parameters
* clear return value
* documented exceptions where applicable
* unit tests

Public APIs should remain simple and consistent.

---

## Testing

Every implementation must include tests.

Tests should cover:

* normal cases
* mathematical correctness
* boundary cases
* invalid input
* convergence behavior
* failure conditions where applicable

Run tests after implementation.

Preferred command:

```bash
pytest
```

---

## Code Quality

Before considering a task complete, run:

```bash
pytest
ruff check .
mypy src
```

Fix relevant errors before marking the task complete.

Do not silence errors without understanding their cause.

---

## Documentation

Numerical algorithms should be documented with:

1. Mathematical definition
2. Intuition
3. Algorithm
4. Parameters
5. Return value
6. Example
7. Important limitations

Keep documentation understandable to mathematics and engineering students.

---

## Git

Use small, meaningful commits.

Commit messages should follow:

```text
feat: add bisection method
fix: handle zero endpoint in bisection
test: add bisection edge cases
docs: document bisection method
refactor: simplify root finding validation
```

Do not create commits unless explicitly requested.

---

## Dependency Policy

Do not add a dependency unless it provides clear value.

Initial runtime dependency:

* NumPy

Development dependencies may include:

* pytest
* ruff
* mypy
* build

---

## Important Rule

Do not assume that more code is better.

Prefer the smallest correct implementation that satisfies the current task.
