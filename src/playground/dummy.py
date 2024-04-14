"""Dummy module"""


def add(x: int | float, y: int | float) -> int | float:
    """Add two integers or floats

    >>> add(3, 2)
    5
    >>> add(5.5, 1)
    6.5
    >>> add(-1, 6.7)
    5.7
    """
    return x+y