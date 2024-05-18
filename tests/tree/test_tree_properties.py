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


@pytest.mark.parametrize(
    ("expected_height", "tree"),
    (
        (
            # An empty tree is already at minimum height
            0,
            BinarySearchTree(),
        ),
        (
            # A tree with one node is already at minimum height
            1,
            BinarySearchTree(BinaryTreeNode(1)),
        ),
        (
            # A tree with two nodes is already at minimum height
            2,
            BinarySearchTree(
                BinaryTreeNode(
                    1,
                    left=BinaryTreeNode(-1),
                ),
            ),
        ),
        (
            # A tree with two nodes is already at minimum height
            2,
            BinarySearchTree(
                BinaryTreeNode(
                    1,
                    left=BinaryTreeNode(-1),
                ),
            ),
        ),
        (
            # Skewed tree
            2,
            BinarySearchTree(
                BinaryTreeNode(
                    1,
                    left=BinaryTreeNode(
                        -1,
                        left=BinaryTreeNode(-2),
                    ),
                ),
            ),
        ),
        (
            # Already balanced tree
            3,
            BinarySearchTree(
                BinaryTreeNode(
                    4,
                    left=BinaryTreeNode(
                        2,
                        left=BinaryTreeNode(1),
                        right=BinaryTreeNode(3),
                    ),
                    right=BinaryTreeNode(
                        6,
                        left=BinaryTreeNode(5),
                        right=BinaryTreeNode(7),
                    ),
                ),
            ),
        ),
        (
            # Tree with 8 nodes
            3,
            BinarySearchTree(
                BinaryTreeNode(
                    4,
                    left=BinaryTreeNode(
                        3,
                        left=BinaryTreeNode(
                            2,
                            left=BinaryTreeNode(1),
                        ),
                    ),
                    right=BinaryTreeNode(
                        5,
                        right=BinaryTreeNode(
                            6,
                            right=BinaryTreeNode(
                                7,
                            ),
                        ),
                    ),
                ),
            ),
        ),
        (
            # Tree with 9 nodes
            4,
            BinarySearchTree(
                BinaryTreeNode(
                    4,
                    left=BinaryTreeNode(
                        3,
                        left=BinaryTreeNode(
                            2,
                            left=BinaryTreeNode(1),
                        ),
                    ),
                    right=BinaryTreeNode(
                        5,
                        right=BinaryTreeNode(
                            6,
                            right=BinaryTreeNode(
                                7,
                                right=BinaryTreeNode(8),
                            ),
                        ),
                    ),
                ),
            ),
        ),
        (
            # Tree with 16 nodes
            4,
            BinarySearchTree(
                BinaryTreeNode(
                    4,
                    left=BinaryTreeNode(
                        3,
                        left=BinaryTreeNode(
                            2,
                            left=BinaryTreeNode(1),
                        ),
                    ),
                    right=BinaryTreeNode(
                        5,
                        right=BinaryTreeNode(
                            10,
                            right=BinaryTreeNode(
                                15,
                                left=BinaryTreeNode(
                                    14,
                                    left=BinaryTreeNode(
                                        13,
                                        left=BinaryTreeNode(
                                            11,
                                            right=BinaryTreeNode(12),
                                        ),
                                    ),
                                ),
                            ),
                            left=BinaryTreeNode(
                                8,
                                left=BinaryTreeNode(
                                    6,
                                    right=BinaryTreeNode(7),
                                ),
                                right=BinaryTreeNode(9),
                            ),
                        ),
                    ),
                ),
            ),
        ),
        (
            # Tree with 17 nodes
            5,
            BinarySearchTree(
                BinaryTreeNode(
                    4,
                    left=BinaryTreeNode(
                        3,
                        left=BinaryTreeNode(
                            2,
                            left=BinaryTreeNode(1),
                        ),
                    ),
                    right=BinaryTreeNode(
                        5,
                        right=BinaryTreeNode(
                            10,
                            right=BinaryTreeNode(
                                15,
                                left=BinaryTreeNode(
                                    14,
                                    left=BinaryTreeNode(
                                        13,
                                        left=BinaryTreeNode(
                                            11,
                                            right=BinaryTreeNode(12),
                                        ),
                                    ),
                                ),
                                right=BinaryTreeNode(16),
                            ),
                            left=BinaryTreeNode(
                                8,
                                left=BinaryTreeNode(
                                    6,
                                    right=BinaryTreeNode(7),
                                ),
                                right=BinaryTreeNode(9),
                            ),
                        ),
                    ),
                ),
            ),
        ),
    ),
)
def test_balancing(
    expected_height: int,
    tree: BinarySearchTree[int],
):
    previous_length = len(tree)
    previous_elements = tuple(tree)
    tree.balance()
    assert len(tree) == previous_length
    assert tuple(tree) == previous_elements
    assert tree.height == expected_height
