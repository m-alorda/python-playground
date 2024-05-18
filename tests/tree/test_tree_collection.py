"""Binary Search Tree module to test the Collection behavior"""

import pytest

from playground.tree import BinarySearchTree, BinaryTreeNode


@pytest.mark.parametrize(
    ("value", "tree"),
    (
        (
            1,
            BinarySearchTree(BinaryTreeNode(1)),
        ),
        (
            3,
            BinarySearchTree(
                BinaryTreeNode(
                    2,
                    left=BinaryTreeNode(1),
                    right=BinaryTreeNode(3),
                )
            ),
        ),
        (
            6,
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
            0,
            BinarySearchTree(),
        ),
        (
            2,
            BinarySearchTree(BinaryTreeNode(1)),
        ),
        (
            5,
            BinarySearchTree(
                BinaryTreeNode(
                    2,
                    left=BinaryTreeNode(1),
                    right=BinaryTreeNode(3),
                ),
            ),
        ),
        (
            -1,
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
                )
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
    assert "1" not in BinarySearchTree(BinaryTreeNode(1))  # type: ignore


def test_cannot_contain_none():
    assert None not in BinarySearchTree()
    assert None not in BinarySearchTree(BinaryTreeNode(1))


@pytest.mark.parametrize(
    ("expected_length", "tree"),
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
            2,
            BinarySearchTree(
                BinaryTreeNode(
                    2,
                    left=BinaryTreeNode(1),
                ),
            ),
        ),
        (
            3,
            BinarySearchTree(
                BinaryTreeNode(
                    2,
                    left=BinaryTreeNode(1),
                    right=BinaryTreeNode(3),
                ),
            ),
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
                    3,
                    left=BinaryTreeNode(2),
                    right=BinaryTreeNode(
                        5,
                        left=BinaryTreeNode(4),
                        right=BinaryTreeNode(6),
                    ),
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
