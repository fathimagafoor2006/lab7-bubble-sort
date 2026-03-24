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
import shutil
import sys
import time

# Optional Windows ANSI support
try:
    import colorama
    colorama.init()
except Exception:
    colorama = None


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


def draw_bars(arr: List[int], width: int | None = None) -> str:
    """Return a single-line ASCII/bar representation of `arr` for animation."""
    if not arr:
        return ""

    # Determine terminal width
    if width is None:
        width = shutil.get_terminal_size((80, 20)).columns

    max_val = max(arr)
    min_val = min(arr)
    span = max_val - min_val if max_val != min_val else 1

    # Reserve some columns for spacing and ensure at least one char per bar
    bar_width = max(1, width // (len(arr) * 2))

    bars = []
    for val in arr:
        norm = (val - min_val) / span
        bar_len = int(norm * (bar_width - 1)) + 1
        # Fallback ASCII character if terminal doesn't show block
        ch = "█"
        try:
            ch.encode(sys.stdout.encoding or "utf-8")
        except Exception:
            ch = "#"
        bars.append(ch * bar_len)

    return " ".join(bars)


def bubble_sort_visual(arr: List[int], delay: float = 0.06) -> None:
    """Animated, in-place redraw bubble sort (ASCII bars)."""
    n = len(arr)

    # Initial draw (clear line first to avoid leftover characters)
    sys.stdout.write("\x1b[2K\r")
    sys.stdout.write(draw_bars(arr))
    sys.stdout.flush()
    time.sleep(delay)

    for i in range(n):
        swapped = False
        for j in range(0, n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

                # Redraw
                sys.stdout.write("\x1b[2K\r")
                sys.stdout.write(draw_bars(arr))
                sys.stdout.flush()
                time.sleep(delay)

        if not swapped:
            break

    sys.stdout.write("\n")


def bubble_sort_pygame(arr: List[int], delay: float = 0.06) -> None:
    """Pygame-based 2D visualization of bubble sort.

    Controls:
    - Space: pause/resume
    - Right arrow: step one swap when paused
    - Esc or close window: exit

    This function imports `pygame` locally so the project can run without
    pygame installed unless this mode is used.
    """
    try:
        import pygame
    except Exception as e:
        print("Pygame is required for this visualization. Install with: pip install pygame")
        return

    pygame.init()
    width, height = 800, 400
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Bubble Sort Visualization")
    clock = pygame.time.Clock()

    n = len(arr)
    if n == 0:
        return

    def draw(highlight: tuple | None = None):
        screen.fill((30, 30, 30))
        maxv = max(arr)
        bar_w = max(1, width // n)
        for i, v in enumerate(arr):
            h = int((v / maxv) * (height - 40))
            x = i * bar_w
            y = height - h
            color = (200, 200, 200)
            if highlight and i in highlight:
                color = (220, 80, 80)
            pygame.draw.rect(screen, color, (x, y, bar_w - 1, h))
        pygame.display.flip()

    running = True
    paused = False
    step = False

    draw()

    for i in range(n):
        swapped = False
        for j in range(0, n - 1 - i):
            # Event handling
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    running = False
                elif ev.type == pygame.KEYDOWN:
                    if ev.key == pygame.K_SPACE:
                        paused = not paused
                    elif ev.key == pygame.K_RIGHT:
                        step = True
                    elif ev.key == pygame.K_ESCAPE:
                        running = False
            if not running:
                break

            while paused and not step and running:
                for ev in pygame.event.get():
                    if ev.type == pygame.QUIT:
                        running = False
                    elif ev.type == pygame.KEYDOWN:
                        if ev.key == pygame.K_SPACE:
                            paused = False
                        elif ev.key == pygame.K_RIGHT:
                            step = True
                        elif ev.key == pygame.K_ESCAPE:
                            running = False
                clock.tick(30)

            if not running:
                break

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                draw(highlight=(j, j + 1))
                # delay in milliseconds
                pygame.time.delay(max(1, int(delay * 1000)))

            clock.tick(60)

        if not running or not swapped:
            break

    # final draw and wait for user to close or press Esc
    draw()
    while running:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                running = False
            elif ev.type == pygame.KEYDOWN and ev.key == pygame.K_ESCAPE:
                running = False
        clock.tick(30)

    pygame.quit()


def parse_args() -> dict:
    """Parse command-line arguments or return defaults."""
    parser = argparse.ArgumentParser(description="Bubble Sort Application")
    parser.add_argument(
        "--arr",
        type=str,
        help="Comma-separated list of numbers, e.g. 5,2,9,1,5",
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "--trace",
        action="store_true",
        help="Enable verbose tracing mode",
    )
    group.add_argument(
        "--visual",
        action="store_true",
        help="Enable in-place ASCII visual animation (in-terminal)",
    )
    group.add_argument(
        "--py",
        "--pygame",
        action="store_true",
        dest="py",
        help="Enable Pygame-based 2D visualization (requires pygame)",
    )
    parser.add_argument(
        "--delay",
        type=float,
        default=0.06,
        help="Animation frame delay in seconds (visual mode)",
    )
    parser.add_argument(
        "--max-elements",
        type=int,
        default=200,
        help="Maximum elements allowed for visual mode (fallback: reject)",
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
            parser.error("Invalid number in --arr input. Provide comma-separated integers.")

    return {
    "arr": arr,
    "trace": args.trace,
    "example": args.example,
    "visual": args.visual,
    "py": args.py,
    "delay": args.delay,
    "max_elements": args.max_elements,
}


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
    elif args.get("visual"):
        # Limit visual mode for very large lists to keep animation readable
        max_visual = min(args.get("max_elements", 200), max(60, shutil.get_terminal_size((80, 20)).columns // 2))
        if len(arr) > max_visual:
            print(f"List too large for visual mode (>{max_visual} elements).")
            print("Run without --visual or provide a smaller list or increase --max-elements.")
        else:
            bubble_sort_visual(arr, delay=args.get("delay", 0.06))
    elif args.get("py"):
        # Pygame visualization mode
        max_visual = args.get("max_elements", 200)
        if len(arr) > max_visual:
            print(f"List too large for pygame visual mode (>{max_visual} elements).")
            print("Run without --py or provide a smaller list or increase --max-elements.")
        else:
            bubble_sort_pygame(arr, delay=args.get("delay", 0.06))
    else:
        bubble_sort(arr)

    print("Sorted result:", arr)


if __name__ == "__main__":
    main()
