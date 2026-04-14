# Part 2 - Automation

This branch contains automation for two high-value Dashboard scenarios from `test-plan.md`:

1. Slot input validation
2. Prevent duplicate slot assignment

Why these were chosen:
- Both are directly tied to critical/major Dashboard risks from Part 1.
- Both protect core parking integrity and reduce regression risk.
- Both provide meaningful value in repeated CI/local runs.

## Stack

- Python
- Pytest
- Playwright

## Setup

1. Start the application locally:

```bash
docker pull --platform linux/amd64 doringber/parking-manager:3.1.0
docker run --platform linux/amd64 -d -p 5000:5000 --name parking-manager doringber/parking-manager:3.1.0
```

2. Install test dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m playwright install
```

## Run tests

```bash
pytest
```

## Configuration

Environment variables:
- `BASE_URL` (default: `http://localhost:5000`)
- `APP_USERNAME` (default: `admin`)
- `APP_PASSWORD` (default: `password`)

Example:

```bash
BASE_URL=http://localhost:5000 APP_USERNAME=admin APP_PASSWORD=password pytest
```

## Reliability and maintainability notes

- Reusable helpers are placed in `tests/conftest.py` for login and selector fallbacks.
- Tests use multiple selector candidates to reduce breakage from minor UI changes.
- Assertions use user-visible validation/error patterns for behavior-level confidence.
- Each test is independent and focused on one business rule.
- Both tests are marked `xfail` because they encode expected product behavior for known Part 1 defects; this keeps the suite stable while still tracking regression targets.
