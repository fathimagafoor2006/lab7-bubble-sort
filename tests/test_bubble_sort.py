import pytest

from main import bubble_sort


def test_empty_list():
    arr = []
    bubble_sort(arr)
    assert arr == []


def test_single_element():
    arr = [1]
    bubble_sort(arr)
    assert arr == [1]


def test_already_sorted():
    arr = [1, 2, 3, 4]
    bubble_sort(arr)
    assert arr == [1, 2, 3, 4]


def test_reverse_sorted():
    arr = [4, 3, 2, 1]
    bubble_sort(arr)
    assert arr == [1, 2, 3, 4]


def test_duplicates():
    arr = [3, 1, 2, 3, 1]
    bubble_sort(arr)
    assert arr == [1, 1, 2, 3, 3]
