# Part 2 - Automation

This part automates meaningful scenarios from `test-plan.md` with a focus on high and critical risk areas.

## Why These Scenarios

I prioritized scenarios that protect the core parking flow and catch high-impact regressions:

1. Slot input validation (BUG-02 / TC-07)
2. Duplicate slot assignment behavior (BUG-03 / TC-06)

I also included authentication smoke coverage to support stable test flow:

3. Valid login (TC-01)
4. Invalid login handling (TC-02)

## Tech Stack

- Python
- Pytest
- Playwright

## Project Structure

- `tests/test_dashboard_automation.py` - Dashboard automation scenarios
- `tests/test_authentication.py` - Authentication smoke scenarios
- `tests/pages/` - Page Objects (`base_page.py`, `login_page.py`, `dashboard_page.py`)
- `tests/data/test_data.py` - Shared test data/constants
- `tests/conftest.py` - Browser setup and reusable fixtures

## Setup

1) Start the app:

```bash
docker pull --platform linux/amd64 doringber/parking-manager:3.1.0
docker run --platform linux/amd64 -d -p 5000:5000 --name parking-manager doringber/parking-manager:3.1.0
```

2) Create and activate virtual environment, then install dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m playwright install
```

## Verify venv Before Running Tests

```bash
echo $VIRTUAL_ENV
which python
```

Expected:
- `$VIRTUAL_ENV` is not empty
- `which python` points to `.venv/bin/python`

If not active:

```bash
source .venv/bin/activate
```

## Run Tests (CLI / Headless)

Run all tests:

```bash
pytest -rA
```

Run only high + critical tests:

```bash
pytest -m "high and critical" -rA
```

## Run Tests in Browser (Headed)

```bash
HEADLESS=false pytest -rA -s
```

Optional debug mode:

```bash
PWDEBUG=1 HEADLESS=false pytest -s
```

## Configuration

- `BASE_URL` (default: `http://localhost:5000`)
- `APP_USERNAME` (default: `admin`)
- `APP_PASSWORD` (default: `password`)
- `HEADLESS` (default: `true`)

Example:

```bash
BASE_URL=http://localhost:5000 APP_USERNAME=admin APP_PASSWORD=password pytest -rA
```

## Reliability and Maintainability

- Page Object Model keeps selectors and UI actions out of tests.
- Shared fixtures reduce duplication and keep tests readable.
- Centralized test data makes scenarios easier to maintain.
- Selector fallback and controlled waits improve stability across UI changes.
