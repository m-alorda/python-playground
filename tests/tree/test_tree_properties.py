"""Binary Search Tree module to test properties not covered by other test suites"""

import pytest

from playground.tree import BinarySearchTree


@pytest.mark.parametrize(
    ("expected_height", "tree"),
    (
        (
            1,
            BinarySearchTree(1),
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
def test_tree_height(expected_height: int, tree: BinarySearchTree[int]):
    assert tree.height == expected_height
