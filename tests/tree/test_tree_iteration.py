"""Binary Search Tree module to test non-default tree iteration"""

import pytest

from playground.tree import BinarySearchTree, BinaryTreeNode


@pytest.mark.parametrize(
    ("expected_elements", "tree"),
    (
        (
            (),
            BinarySearchTree(),
        ),
        (
            (1,),
            BinarySearchTree(BinaryTreeNode(1)),
        ),
        (
            (1, 2, 3),
            BinarySearchTree(
                BinaryTreeNode(
                    2,
                    left=BinaryTreeNode(1),
                    right=BinaryTreeNode(3),
                ),
            ),
        ),
        (
            (1, 3, 4, 5, 6, 7, 8),
            BinarySearchTree(
                BinaryTreeNode(
                    5,
                    left=BinaryTreeNode(
                        3,
                        left=BinaryTreeNode(1),
                        right=BinaryTreeNode(4),
                    ),
                    right=BinaryTreeNode(
                        7,
                        left=BinaryTreeNode(6),
                        right=BinaryTreeNode(8),
                    ),
                ),
            ),
        ),
        (
            (3, 4, 6, 10, 12, 13, 14, 15, 16, 20, 23),
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
def test_default_iteration_order(
    expected_elements: tuple[int, ...],
    tree: BinarySearchTree[int],
):
    assert tuple(tree) == expected_elements
    assert tuple(tree.depth_first_in_order_iterator()) == expected_elements


@pytest.mark.parametrize(
    ("expected_elements", "tree"),
    (
        (
            (),
            BinarySearchTree(),
        ),
        (
            (1,),
            BinarySearchTree(BinaryTreeNode(1)),
        ),
        (
            (2, 1, 3),
            BinarySearchTree(
                BinaryTreeNode(
                    2,
                    left=BinaryTreeNode(1),
                    right=BinaryTreeNode(3),
                ),
            ),
        ),
        (
            (5, 3, 7, 1, 4, 6, 8),
            BinarySearchTree(
                BinaryTreeNode(
                    5,
                    left=BinaryTreeNode(
                        3,
                        left=BinaryTreeNode(1),
                        right=BinaryTreeNode(4),
                    ),
                    right=BinaryTreeNode(
                        7,
                        left=BinaryTreeNode(6),
                        right=BinaryTreeNode(8),
                    ),
                ),
            ),
        ),
        (
            (10, 6, 16, 3, 13, 20, 4, 12, 14, 23, 15),
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
def test_breath_first_iteration(
    expected_elements: tuple[int, ...],
    tree: BinarySearchTree[int],
):
    assert tuple(tree.breadth_first_iterator()) == expected_elements


@pytest.mark.parametrize(
    ("expected_elements", "tree"),
    (
        (
            (),
            BinarySearchTree(),
        ),
        (
            (1,),
            BinarySearchTree(BinaryTreeNode(1)),
        ),
        (
            (2, 1, 3),
            BinarySearchTree(
                BinaryTreeNode(
                    2,
                    left=BinaryTreeNode(1),
                    right=BinaryTreeNode(3),
                ),
            ),
        ),
        (
            (5, 3, 1, 4, 7, 6, 8),
            BinarySearchTree(
                BinaryTreeNode(
                    5,
                    left=BinaryTreeNode(
                        3,
                        left=BinaryTreeNode(1),
                        right=BinaryTreeNode(4),
                    ),
                    right=BinaryTreeNode(
                        7,
                        left=BinaryTreeNode(6),
                        right=BinaryTreeNode(8),
                    ),
                ),
            ),
        ),
        (
            (10, 6, 3, 4, 16, 13, 12, 14, 15, 20, 23),
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
def test_pre_order_iteration(
    expected_elements: tuple[int, ...],
    tree: BinarySearchTree[int],
):
    assert tuple(tree.depth_first_pre_order_iterator()) == expected_elements


@pytest.mark.parametrize(
    ("expected_elements", "tree"),
    (
        (
            (),
            BinarySearchTree(),
        ),
        (
            (1,),
            BinarySearchTree(BinaryTreeNode(1)),
        ),
        (
            (1, 3, 2),
            BinarySearchTree(
                BinaryTreeNode(
                    2,
                    left=BinaryTreeNode(1),
                    right=BinaryTreeNode(3),
                ),
            ),
        ),
        (
            (1, 4, 3, 6, 8, 7, 5),
            BinarySearchTree(
                BinaryTreeNode(
                    5,
                    left=BinaryTreeNode(
                        3,
                        left=BinaryTreeNode(1),
                        right=BinaryTreeNode(4),
                    ),
                    right=BinaryTreeNode(
                        7,
                        left=BinaryTreeNode(6),
                        right=BinaryTreeNode(8),
                    ),
                ),
            ),
        ),
        (
            (4, 3, 6, 12, 15, 14, 13, 23, 20, 16, 10),
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
def test_post_order_iteration(
    expected_elements: tuple[int, ...],
    tree: BinarySearchTree[int],
):
    assert tuple(tree.depth_first_post_order_iterator()) == expected_elements
