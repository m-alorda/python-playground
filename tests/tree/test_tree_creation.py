"""Binary Search Tree module to test tree creation"""

import pytest

from playground.tree import BinarySearchTree, BinaryTreeNode


def test_can_create_empty_tree():
    BinarySearchTree()


def test_can_create_sorted_tree():
    BinarySearchTree(
        BinaryTreeNode(
            5,
            left=BinaryTreeNode(
                3,
                left=BinaryTreeNode(
                    2,
                    left=BinaryTreeNode(1),
                ),
                right=BinaryTreeNode(4),
            ),
            right=BinaryTreeNode(
                7,
                left=BinaryTreeNode(6),
                right=BinaryTreeNode(
                    8,
                    right=BinaryTreeNode(9),
                ),
            ),
        ),
    )


def test_can_create_tree_with_duplicates():
    BinarySearchTree(BinaryTreeNode(1, left=BinaryTreeNode(1), right=BinaryTreeNode(1)))


def test_can_not_create_unsorted_tree_from_the_root():
    with pytest.raises(ValueError):
        BinarySearchTree(
            BinaryTreeNode(
                1,
                left=BinaryTreeNode(
                    # Is larger and to the left of the root
                    2
                ),
            ),
        )
    with pytest.raises(ValueError):
        BinarySearchTree(
            BinaryTreeNode(
                2,
                right=BinaryTreeNode(
                    # Is smaller and to the right of the root
                    1
                ),
            ),
        )
    with pytest.raises(ValueError):
        BinarySearchTree(
            BinaryTreeNode(
                2,
                left=BinaryTreeNode(1),
                right=BinaryTreeNode(
                    # Is smaller and to the right of the root
                    1
                ),
            ),
        )


def test_can_not_create_unsorted_tree_from_its_parent():
    with pytest.raises(ValueError):
        BinarySearchTree(
            BinaryTreeNode(
                2,
                left=BinaryTreeNode(1),
                right=BinaryTreeNode(
                    3,
                    left=BinaryTreeNode(
                        # Is larger and to the left of its parent
                        4
                    ),
                ),
            ),
        )
    with pytest.raises(ValueError):
        BinarySearchTree(
            BinaryTreeNode(
                3,
                left=BinaryTreeNode(2),
                right=BinaryTreeNode(
                    5,
                    right=BinaryTreeNode(
                        # Is smaller and to the right of its parent
                        4
                    ),
                ),
            ),
        )


def test_can_not_create_unsorted_tree_from_the_root_in_a_higher_level():
    with pytest.raises(ValueError):
        BinarySearchTree(
            BinaryTreeNode(
                3,
                left=BinaryTreeNode(2),
                right=BinaryTreeNode(
                    4,
                    left=BinaryTreeNode(
                        # Is smaller and to the left of the root
                        1
                    ),
                ),
            ),
        )
    with pytest.raises(ValueError):
        BinarySearchTree(
            BinaryTreeNode(
                50,
                left=BinaryTreeNode(
                    20,
                    left=BinaryTreeNode(
                        10,
                        right=BinaryTreeNode(
                            # Is larger and to the left 20
                            30
                        ),
                    ),
                ),
                right=BinaryTreeNode(80),
            ),
        )
    with pytest.raises(ValueError):
        BinarySearchTree(
            BinaryTreeNode(
                40,
                left=BinaryTreeNode(
                    20,
                    right=BinaryTreeNode(
                        30,
                        left=BinaryTreeNode(
                            # Is smaller and to the right 20
                            10,
                            right=BinaryTreeNode(24),
                        ),
                    ),
                ),
            ),
        )
    with pytest.raises(ValueError):
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
                        left=BinaryTreeNode(
                            # Is smaller and to the right of the root
                            8
                        ),
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
        )
