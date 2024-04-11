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


def test_can_not_create_unsorted_tree_from_the_root():
    with pytest.raises(ValueError):
        BinarySearchTree(
            1,
            left=BinarySearchTree(
                # Is larger and to the left of the root
                2
            ),
        )
    with pytest.raises(ValueError):
        BinarySearchTree(
            2,
            right=BinarySearchTree(
                # Is smaller and to the right of the root
                1
            ),
        )
    with pytest.raises(ValueError):
        BinarySearchTree(
            2,
            left=BinarySearchTree(1),
            right=BinarySearchTree(
                # Is smaller and to the right of the root
                1
            ),
        )


def test_can_not_create_unsorted_tree_from_its_parent():
    with pytest.raises(ValueError):
        BinarySearchTree(
            2,
            left=BinarySearchTree(1),
            right=BinarySearchTree(
                3,
                left=BinarySearchTree(
                    # Is larger and to the left of its parent
                    4
                ),
            ),
        )
    with pytest.raises(ValueError):
        BinarySearchTree(
            3,
            left=BinarySearchTree(2),
            right=BinarySearchTree(
                5,
                right=BinarySearchTree(
                    # Is smaller and to the right of its parent
                    4
                ),
            ),
        )


@pytest.mark.xfail
def test_can_not_create_unsorted_tree_from_the_root_in_a_higher_level():
    with pytest.raises(ValueError):
        BinarySearchTree(
            3,
            left=BinarySearchTree(2),
            right=BinarySearchTree(
                4,
                left=BinarySearchTree(
                    # Is smaller and to the left of the root
                    1
                ),
            ),
        )
    with pytest.raises(ValueError):
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
                    left=BinarySearchTree(
                        # Is smaller and to the right of the root
                        8
                    ),
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
        )
