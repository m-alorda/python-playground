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
