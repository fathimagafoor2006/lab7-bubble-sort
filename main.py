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
import argparse


def bubble_sort(arr: List[int]) -> None:
    """In-place bubble sort that sorts `arr` in ascending order."""
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break


def bubble_sort_with_trace(arr: List[int]) -> None:
    """Bubble sort that prints the array after every swap for learning."""
    n = len(arr)
    for i in range(n):
        swapped = False
        print(f"Pass {i + 1} start: {arr}")
        for j in range(0, n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                print(f"  Swapped positions {j} and {j+1}: {arr}")
        if not swapped:
            print("  No swaps — list is sorted early.")
            break
        print(f"Pass {i + 1} end: {arr}\n")


def parse_args() -> dict:
    """Parse command-line arguments or return defaults."""
    parser = argparse.ArgumentParser(description="Bubble Sort Application")
    parser.add_argument(
        "--arr",
        type=str,
        help="Comma-separated list of numbers, e.g. 5,2,9,1,5",
    )
    parser.add_argument(
        "--trace",
        action="store_true",
        help="Enable verbose tracing mode",
    )
    parser.add_argument(
        "--example",
        action="store_true",
        help="Run a built-in example list",
    )

    args = parser.parse_args()

    arr = None
    if args.arr:
        try:
            arr = [int(x.strip()) for x in args.arr.split(",")]
        except ValueError:
            raise ValueError("Invalid number in --arr input.")

    return {"arr": arr, "trace": args.trace, "example": args.example}


def main() -> None:
    """Main entrypoint for the bubble sort app."""
    args = parse_args()
    arr = args.get("arr")

    if args.get("example"):
        arr = [5, 2, 9, 1, 5]

    if arr is None:
        arr = [5, 2, 9, 1, 5]  # fallback default

    print("Original:", arr)

    if args.get("trace"):
        bubble_sort_with_trace(arr)
    else:
        bubble_sort(arr)

    print("Sorted result:", arr)


if __name__ == "__main__":
    main()