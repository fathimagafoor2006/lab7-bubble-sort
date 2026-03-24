"""
Skeleton Bubble Sort Application

This file provides a minimal, well-documented skeleton for a bubble sort
application. All functions are stubs with TODOs telling you what to implement.

How to use:
- Fill in the TODOs below.
- Run the script with `python main.py` for a simple interactive demo once
  `main()` is implemented.
"""

from typing import List


def bubble_sort(arr: List[int]) -> None:
	"""In-place bubble sort that sorts `arr` in ascending order.

	TODOs:
	- Implement the standard bubble sort algorithm with an early-exit
	  optimization (stop when a pass makes no swaps).
	- Keep it stable (don't reorder equal elements).
	- Add type checks or assertions if desired.

	Args:
		arr: list of integers to sort (modified in place).
	"""
	# TODO: implement the sorting logic below
	pass


def bubble_sort_with_trace(arr: List[int]) -> None:
	"""Bubble sort that prints the array after every swap for learning.

	TODOs:
	- Call this from `main()` when user asks for verbose/debug mode.
	- Use the same sorting logic as `bubble_sort` but print intermediate
	  states so the learner can follow swaps and passes.
	"""
	# TODO: implement the tracing variant (use prints or logging)
	pass


def parse_args() -> dict:
	"""Parse command-line arguments or return defaults.

	TODOs:
	- Use `argparse` to support: input list (as comma-separated numbers),
	  `--trace` to enable `bubble_sort_with_trace`, and `--example` to run
	  a built-in example.
	- Return a simple dict with keys like `arr`, `trace`, `example`.
	"""
	# TODO: implement argument parsing and return a dict
	return {"arr": None, "trace": False, "example": False}


def main() -> None:
	"""Main entrypoint for the bubble sort app.

	Suggested flow (implement these TODOs):
	1. Call `parse_args()` to get inputs.
	2. If `example` was requested, set `arr` to a demo list.
	3. If `trace` is True, call `bubble_sort_with_trace(arr)`; else call
	   `bubble_sort(arr)`.
	4. Print the sorted result.
	5. Add error handling for invalid input.
	"""
	# TODO: implement the main flow using functions above
	args = parse_args()
	arr = args.get("arr")
	if arr is None:
		# TODO: replace with real input handling or example data
		arr = [5, 2, 9, 1, 5]

	if args.get("trace"):
		bubble_sort_with_trace(arr)
	else:
		bubble_sort(arr)

	print("Sorted result:", arr)


if __name__ == "__main__":
	main()

