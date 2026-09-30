import pytest
from student import calculate_result


def test_calculate_result():
    result = calculate_result("Yaswanthi", 80, 90, 70)

    assert result["total"] == 240
    assert result["average"] == 80
    assert result["grade"] == "B"


def test_invalid_marks():
    with pytest.raises(ValueError):
        calculate_result("Yaswanthi", 110, 90, 70)


def test_zero_marks():
    result = calculate_result("Student", 0, 0, 0)

    assert result["total"] == 0
    assert result["average"] == 0
    assert result["grade"] == "F"