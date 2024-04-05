"""Dummy module tests"""

from math import isclose, inf, isnan

import pytest

from playground import dummy


@pytest.mark.parametrize(
    ("x", "y", "expected"),
    (
        (3, 4, 7),
        (2, 8, 10),
        (-1, -2, -3),
        (-1, 7, 6),
        (-1, 1, 0),
    ),
)
def test_add_integers(x, y, expected):
    assert dummy.add(x, y) == expected


@pytest.mark.parametrize(
    ("x", "y", "expected"),
    (
        (1.5, 1.15, 2.65),
        (4.777, 0.223, 5.0),
        (-1.5, 2.7, 1.2),
        (-4.5, 1.15, -3.35),
        (-14.8, 14.8, 0.0),
    ),
)
def test_add_floats(x, y, expected):
    assert isclose(dummy.add(x, y), expected)


@pytest.mark.parametrize(
    ("x", "y", "expected"),
    (
        (1, 1.5, 2.5),
        (6.2223, -2, 4.2223),
        (0.00001, 1000, 1000.00001),
        (-1.0, 1, 0),
    ),
)
def test_add_integers_and_floats(x, y, expected):
    assert isclose(dummy.add(x, y), expected)


@pytest.mark.parametrize(
    ("x", "y", "expected"),
    (
        (inf, 1, inf),
        (-inf, 1, -inf),
        (inf, inf, inf),
        (-inf, -inf, -inf),
    ),
)
def test_add_inf(x, y, expected):
    assert dummy.add(x, y) == expected


def test_nan():
    assert isnan(dummy.add(-inf, inf))
