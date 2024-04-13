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
def test_not_contains(
    value: int,
    tree: BinarySearchTree[int],
):
    assert value not in tree


def test_cannot_contain_an_element_of_different_type():
    assert "1" not in BinarySearchTree(1)  # type: ignore


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
                    5,
                    left=BinarySearchTree(4),
                    right=BinarySearchTree(6),
                ),
            ),
        ),
    ),
)
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
            (1, 2, 3),
            BinarySearchTree(
                2,
                left=BinarySearchTree(1),
                right=BinarySearchTree(3),
            ),
        ),
        (
            (1, 3, 4, 5, 6, 7, 8),
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
            (3, 4, 6, 10, 12, 13, 14, 15, 16, 20, 23),
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
                        13,
                        left=BinarySearchTree(12),
                        right=BinarySearchTree(
                            14,
                            right=BinarySearchTree(15),
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
def test_default_iteration_order(
    expected_elements: tuple[int, ...],
    tree: BinarySearchTree[int],
):
    assert tuple(tree) == expected_elements
    assert tuple(tree.depth_first_in_order_iterator()) == expected_elements
