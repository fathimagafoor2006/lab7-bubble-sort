# Bubble Sort Learning App
[![Tests](https://github.com/fathimagafoor2006/lab7-bubble-sort/actions/workflows/python-tests.yml/badge.svg)](https://github.com/fathimagafoor2006/lab7-bubble-sort/actions)

A small, educational Python project demonstrating bubble sort with a
trace mode and simple CLI. The repository includes a skeleton implementation
in `main.py` and basic tests under `tests/`.

## Requirements

- Python 3.8+
- pytest (for running tests)

## Usage

- Run the built-in example:

  python main.py --example

- Provide a comma-separated list of integers:

  python main.py --arr 5,2,9,1,5

- Enable verbose tracing to see swaps and passes:

  python main.py --arr 5,2,9,1,5 --trace

## Running tests

Install pytest if needed and run tests from the project root:

```bash
python -m pip install -U pytest
python -m pytest -q
```

## Project structure

- `main.py` — bubble sort implementations and CLI.
- `tests/test_bubble_sort.py` — basic pytest tests (empty, single, sorted,
  reverse, duplicates).
- `JOURNAL.md` — project activity log automatically updated by the agent.

## Development notes

- `main.py` contains TODOs guiding incremental implementation: implement
  `bubble_sort()`, add the tracing variant, and refine CLI parsing.
- Consider adding unit tests for edge cases and CI for automated testing.
