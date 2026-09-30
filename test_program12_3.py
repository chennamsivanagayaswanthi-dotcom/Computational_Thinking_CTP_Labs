import pytest


def calculate_total(
    mark1: float,
    mark2: float,
    mark3: float
) -> float:

    marks = [mark1, mark2, mark3]

    if any(mark < 0 or mark > 100 for mark in marks):
        raise ValueError("Invalid marks")

    return sum(marks)


def test_total():
    assert calculate_total(80, 90, 70) == 240


def test_invalid_marks():
    with pytest.raises(ValueError):
        calculate_total(80, 110, 70)