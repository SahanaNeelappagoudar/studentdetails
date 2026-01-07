import pytest
from studentdetails import calculate_average, assign_grade


# -------------------------------
# Test calculate_average function
# -------------------------------

def test_calculate_average_normal():
    assert calculate_average(80, 90, 100) == pytest.approx(90.0)


def test_calculate_average_zero():
    assert calculate_average(0, 0, 0) == 0


def test_calculate_average_decimal():
    assert calculate_average(75.5, 80.5, 84) == pytest.approx(80.0)


# -------------------------------
# Test assign_grade function
# -------------------------------

def test_grade_S():
    assert assign_grade(95) == "S"


def test_grade_A():
    assert assign_grade(85) == "A"


def test_grade_B():
    assert assign_grade(70) == "B"


def test_grade_C():
    assert assign_grade(55) == "C"


def test_grade_D():
    assert assign_grade(45) == "D"


def test_grade_F():
    assert assign_grade(30) == "F"


# -------------------------------
# Boundary value testing
# -------------------------------

def test_boundary_values():
    assert assign_grade(90) == "S"
    assert assign_grade(80) == "A"
    assert assign_grade(65) == "B"
    assert assign_grade(50) == "C"
    assert assign_grade(40) == "D"