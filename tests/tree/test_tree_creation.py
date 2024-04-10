"""Binary Search Tree module to test tree creation"""

from collections.abc import Callable
import pytest

from playground.tree import BinarySearchTree


def test_can_create_sorted_tree():
    BinarySearchTree(
        5,
        left=BinarySearchTree(
            3,
            left=BinarySearchTree(
                2,
                left=BinarySearchTree(1),
            ),
            right=BinarySearchTree(4),
        ),
        right=BinarySearchTree(
            7,
            left=BinarySearchTree(6),
            right=BinarySearchTree(
                8,
                right=BinarySearchTree(9),
            ),
        ),
    )


def test_can_create_tree_with_duplicates():
    BinarySearchTree(1, left=BinarySearchTree(1), right=BinarySearchTree(1))


@pytest.mark.parametrize(
    ("tree_producer",),
    (
        (
            lambda: BinarySearchTree(
                1,
                left=BinarySearchTree(2),
            ),
        ),
        (
            lambda: BinarySearchTree(
                2,
                right=BinarySearchTree(1),
            ),
        ),
        (
            lambda: BinarySearchTree(
                2,
                left=BinarySearchTree(1),
                right=BinarySearchTree(1),
            ),
        ),
        (
            lambda: BinarySearchTree(
                2,
                left=BinarySearchTree(1),
                right=BinarySearchTree(
                    3,
                    left=BinarySearchTree(4),
                ),
            ),
        ),
        (
            lambda: BinarySearchTree(
                3,
                left=BinarySearchTree(2),
                right=BinarySearchTree(
                    5,
                    right=BinarySearchTree(4),
                ),
            ),
        ),
        (
            lambda: BinarySearchTree(
                3,
                left=BinarySearchTree(2),
                right=BinarySearchTree(
                    4,
                    left=BinarySearchTree(1),
                ),
            ),
        ),
    ),
)
@pytest.mark.xfail
def test_can_not_create_unsorted_tree(
    tree_producer: Callable[..., BinarySearchTree[int]],
):
    with pytest.raises(ValueError):
        tree_producer()
