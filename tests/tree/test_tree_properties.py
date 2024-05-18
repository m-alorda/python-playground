"""Binary Search Tree module to test properties not covered by other test suites"""

import pytest

from playground.tree import BinarySearchTree, BinaryTreeNode


@pytest.mark.parametrize(
    ("expected_height", "tree"),
    (
        (
            0,
            BinarySearchTree(),
        ),
        (
            1,
            BinarySearchTree(BinaryTreeNode(1)),
        ),
        (
            3,
            BinarySearchTree(
                BinaryTreeNode(
                    3,
                    left=BinaryTreeNode(
                        2,
                        left=BinaryTreeNode(1),
                    ),
                ),
            ),
        ),
        (
            5,
            BinarySearchTree(
                BinaryTreeNode(
                    10,
                    left=BinaryTreeNode(
                        6,
                        left=BinaryTreeNode(
                            3,
                            right=BinaryTreeNode(4),
                        ),
                    ),
                    right=BinaryTreeNode(
                        16,
                        left=BinaryTreeNode(
                            13,
                            left=BinaryTreeNode(12),
                            right=BinaryTreeNode(
                                14,
                                right=BinaryTreeNode(15),
                            ),
                        ),
                        right=BinaryTreeNode(
                            20,
                            right=BinaryTreeNode(23),
                        ),
                    ),
                ),
            ),
        ),
    ),
)
def test_tree_height(expected_height: int, tree: BinarySearchTree[int]):
    assert tree.height == expected_height
