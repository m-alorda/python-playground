"""Binary Search Tree module to test the Collection behavior"""

import pytest

from playground.tree import BinarySearchTree


@pytest.mark.parametrize(
    ("value", "tree"),
    (
        (
            1,
            BinarySearchTree(1),
        ),
        (
            3,
            BinarySearchTree(
                2,
                left=BinarySearchTree(1),
                right=BinarySearchTree(3),
            ),
        ),
        (
            6,
            BinarySearchTree(
                4,
                left=BinarySearchTree(
                    2,
                    left=BinarySearchTree(1),
                    right=BinarySearchTree(3),
                ),
                right=BinarySearchTree(
                    6,
                    left=BinarySearchTree(5),
                    right=BinarySearchTree(7),
                ),
            ),
        ),
    ),
)
@pytest.mark.xfail
def test_contains(
    value: int,
    tree: BinarySearchTree[int],
):
    assert value in tree


@pytest.mark.parametrize(
    ("value", "tree"),
    (
        (
            2,
            BinarySearchTree(1),
        ),
        (
            5,
            BinarySearchTree(
                2,
                left=BinarySearchTree(1),
                right=BinarySearchTree(3),
            ),
        ),
        (
            -1,
            BinarySearchTree(
                4,
                left=BinarySearchTree(
                    2,
                    left=BinarySearchTree(1),
                    right=BinarySearchTree(3),
                ),
                right=BinarySearchTree(
                    6,
                    left=BinarySearchTree(5),
                    right=BinarySearchTree(7),
                ),
            ),
        ),
    ),
)
@pytest.mark.xfail
def test_not_contains(
    value: int,
    tree: BinarySearchTree[int],
):
    assert value not in tree


@pytest.mark.parametrize(
    ("expected_length", "tree"),
    (
        (
            1,
            BinarySearchTree(1),
        ),
        (
            2,
            BinarySearchTree(
                2,
                left=BinarySearchTree(1),
            ),
        ),
        (
            3,
            BinarySearchTree(
                2,
                left=BinarySearchTree(1),
                right=BinarySearchTree(3),
            ),
        ),
        (
            3,
            BinarySearchTree(
                3,
                left=BinarySearchTree(
                    2,
                    left=BinarySearchTree(1),
                ),
            ),
        ),
        (
            5,
            BinarySearchTree(
                3,
                left=BinarySearchTree(2),
                right=BinarySearchTree(
                    4,
                    left=BinarySearchTree(1),
                    right=BinarySearchTree(5),
                ),
            ),
        ),
    ),
)
@pytest.mark.xfail
def test_length(
    expected_length: int,
    tree: BinarySearchTree[int],
):
    assert len(tree) == expected_length


@pytest.mark.parametrize(
    ("expected_elements", "tree"),
    (
        (
            (1,),
            BinarySearchTree(1),
        ),
        (
            (2, 1, 3),
            BinarySearchTree(
                2,
                left=BinarySearchTree(1),
                right=BinarySearchTree(3),
            ),
        ),
        (
            (5, 3, 7, 1, 4, 6, 8),
            BinarySearchTree(
                5,
                left=BinarySearchTree(
                    3,
                    left=BinarySearchTree(1),
                    right=BinarySearchTree(4),
                ),
                right=BinarySearchTree(
                    7,
                    left=BinarySearchTree(6),
                    right=BinarySearchTree(8),
                ),
            ),
        ),
        (
            (10, 6, 16, 3, 14, 20, 4, 12, 13, 23, 14),
            BinarySearchTree(
                10,
                left=BinarySearchTree(
                    6,
                    left=BinarySearchTree(
                        3,
                        right=BinarySearchTree(4),
                    ),
                ),
                right=BinarySearchTree(
                    16,
                    left=BinarySearchTree(
                        14,
                        left=BinarySearchTree(12),
                        right=BinarySearchTree(
                            13,
                            right=BinarySearchTree(14),
                        ),
                    ),
                    right=BinarySearchTree(
                        20,
                        right=BinarySearchTree(23),
                    ),
                ),
            ),
        ),
    ),
)
@pytest.mark.xfail
def test_default_iteration_order(
    expected_elements: tuple[int, ...],
    tree: BinarySearchTree[int],
):
    assert tuple(tree) == expected_elements
    assert tuple(tree.breadth_first_iterator()) == expected_elements
