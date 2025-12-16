# Playwright Automation Framework

## Tech Stack
- Python 3.11
- Pytest
- Playwright
- GitHub Actions

## Structure
project/
 ├─ pages/        # Page Object Model
 ├─ tests/ui/     # UI Test cases
 ├─ data/         # Test Data (JSON)
 ├─ screenshots/  # Screenshot on PASS/FAIL
 ├─ videos/       # Video records
 ├─ trace/        # Playwright trace

## Run tests
pytest tests/ui/

## CI/CD
Tests are executed automatically on push and pull request via GitHub Actions.
Artifacts (screenshots, videos, trace) are uploaded after each run.
