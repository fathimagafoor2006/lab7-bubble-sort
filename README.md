# Bubble Sort Learning App
[![Tests](https://github.com/fathimagafoor2006/lab7-bubble-sort/actions/workflows/python-tests.yml/badge.svg)](https://github.com/fathimagafoor2006/lab7-bubble-sort/actions)

A small, educational Python project demonstrating bubble sort with several
interactive modes and a simple CLI. Features implemented in `main.py` include
standard in-place bubble sort, a trace mode, an in-terminal ASCII visual
animation, an optional Pygame visualization, and an example mode. Basic
pytest tests are provided under `tests/`.

## Requirements

- Python 3.8+
- pytest (for running tests)
- `pygame` only if you intend to use the Pygame visualization mode

## Usage

- Run the built-in example:

  python main.py --example

- Provide a comma-separated list of integers:

  python main.py --arr 5,2,9,1,5

- Enable verbose tracing to see swaps and passes:

  python main.py --arr 5,2,9,1,5 --trace

- In-terminal ASCII animation mode:

  python main.py --arr 5,2,9,1,5 --visual --delay 0.06 --max-elements 200

- Pygame-based 2D visualization (requires `pygame`):

  python main.py --arr 5,2,9,1,5 --py

Notes:
- `--delay` controls the animation frame delay (seconds).
- `--max-elements` limits visual modes to prevent overly large animations.

## Running tests

Install pytest if needed and run tests from the project root:

```bash
python -m pip install -U pytest
python -m pytest -q
```

## Project structure

- `main.py` — bubble sort implementations and CLI (trace, visual, pygame).
- `tests/test_bubble_sort.py` — pytest tests for core sorting behavior and helpers.
- `JOURNAL.md` — project activity log.

## Development notes

- `main.py` implements `bubble_sort()`, `bubble_sort_with_trace()`, `bubble_sort_visual()`,
  `bubble_sort_pygame()`, `draw_bars()` and a CLI parser supporting the flags
  described above.
- Tests under `tests/` exercise sorting logic and helpers; add more edge-case
  tests or CI as desired.
