from main import draw_bars


def test_draw_bars_empty():
    assert draw_bars([]) == ""


def test_draw_bars_equal_values():
    s = draw_bars([3, 3, 3], width=30)
    parts = s.split()
    assert len(parts) == 3
    assert parts[0] == parts[1] == parts[2]


def test_draw_bars_negative_values():
    s = draw_bars([-5, 0, 5], width=30)
    parts = s.split()
    assert len(parts) == 3
    # ensure non-empty bars
    assert all(len(p) >= 1 for p in parts)


def test_draw_bars_scaling():
    short = draw_bars([1, 2, 3], width=10)
    long = draw_bars([1, 2, 3], width=80)
    assert len(long) > len(short)
