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
    ("val", "expected_result", "tree"),
    (
        (
            1,
            (1,),
            BinarySearchTree(),
        ),
        (
            1,
            (1, 1),
            BinarySearchTree(BinaryTreeNode(1)),
        ),
        (
            1,
            (1, 2, 3, 4, 5, 6),
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
        (
            7,
            (2, 3, 4, 7, 8, 15),
            BinarySearchTree(
                BinaryTreeNode(
                    3,
                    left=BinaryTreeNode(2),
                    right=BinaryTreeNode(
                        8,
                        left=BinaryTreeNode(4),
                        right=BinaryTreeNode(15),
                    ),
                ),
            ),
        ),
    ),
)
def test_add(
    val: int,
    expected_result: tuple[int, ...],
    tree: BinarySearchTree[int],
):
    tree.add(val)
    assert tuple(tree) == expected_result


@pytest.mark.parametrize(
    ("val", "expected_result", "tree"),
    (
        (
            # Remove the only value in the tree
            1,
            (),
            BinarySearchTree(BinaryTreeNode(1)),
        ),
        (
            # Remove a left leaf node
            1,
            (2,),
            BinarySearchTree(
                BinaryTreeNode(2, left=BinaryTreeNode(1)),
            ),
        ),
        (
            # Remove a right leaf node
            2,
            (1,),
            BinarySearchTree(
                BinaryTreeNode(1, right=BinaryTreeNode(2)),
            ),
        ),
        (
            # Remove the root node with a left subtree
            2,
            (1,),
            BinarySearchTree(
                BinaryTreeNode(2, left=BinaryTreeNode(1)),
            ),
        ),
        (
            # Remove the root node with a right subtree
            1,
            (2,),
            BinarySearchTree(
                BinaryTreeNode(1, right=BinaryTreeNode(2)),
            ),
        ),
        (
            # Remove a duplicate value
            1,
            (1,),
            BinarySearchTree(
                BinaryTreeNode(1, right=BinaryTreeNode(1)),
            ),
        ),
        (
            # Remove a node with both a left and right subtree
            8,
            (2, 3, 4, 15),
            BinarySearchTree(
                BinaryTreeNode(
                    3,
                    left=BinaryTreeNode(2),
                    right=BinaryTreeNode(
                        8,
                        left=BinaryTreeNode(4),
                        right=BinaryTreeNode(15),
                    ),
                ),
            ),
        ),
        (
            # Remove a leaf node
            15,
            (2, 3, 4, 8),
            BinarySearchTree(
                BinaryTreeNode(
                    3,
                    left=BinaryTreeNode(2),
                    right=BinaryTreeNode(
                        8,
                        left=BinaryTreeNode(4),
                        right=BinaryTreeNode(15),
                    ),
                ),
            ),
        ),
    ),
)
def test_remove(
    val: int,
    expected_result: tuple[int, ...],
    tree: BinarySearchTree[int],
):
    tree.remove(val)
    assert tuple(tree) == expected_result


@pytest.mark.parametrize(
    ("val", "tree"),
    (
        (
            1,
            BinarySearchTree(),
        ),
        (
            1,
            BinarySearchTree(BinaryTreeNode(2)),
        ),
        (
            5,
            BinarySearchTree(
                BinaryTreeNode(
                    3,
                    left=BinaryTreeNode(2),
                    right=BinaryTreeNode(
                        8,
                        left=BinaryTreeNode(4),
                        right=BinaryTreeNode(15),
                    ),
                ),
            ),
        ),
    ),
)
def test_remove_not_present_value(
    val: int,
    tree: BinarySearchTree[int],
):
    with pytest.raises(ValueError):
        tree.remove(val)
