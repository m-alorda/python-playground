"""Binary Search Tree module to test non-default tree iteration"""

import pytest

from playground.tree import BinarySearchTree


@pytest.mark.parametrize(
    ("expected_elements", "tree"),
    (
        (
            (1,),
            BinarySearchTree(1),
        ),
        (
            (2, 1, 3),
            BinarySearchTree(
                2,
                left=BinarySearchTree(1),
                right=BinarySearchTree(3),
            ),
        ),
        (
            (5, 3, 7, 1, 4, 6, 8),
            BinarySearchTree(
                5,
                left=BinarySearchTree(
                    3,
                    left=BinarySearchTree(1),
                    right=BinarySearchTree(4),
                ),
                right=BinarySearchTree(
                    7,
                    left=BinarySearchTree(6),
                    right=BinarySearchTree(8),
                ),
            ),
        ),
        (
            (10, 6, 16, 3, 13, 20, 4, 12, 14, 23, 15),
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
@pytest.mark.xfail
def test_breath_first_iteration(
    expected_elements: tuple[int, ...],
    tree: BinarySearchTree[int],
):
    assert tuple(tree.breadth_first_iterator()) == expected_elements


@pytest.mark.parametrize(
    ("expected_elements", "tree"),
    (
        (
            (1,),
            BinarySearchTree(1),
        ),
        (
            (2, 1, 3),
            BinarySearchTree(
                2,
                left=BinarySearchTree(1),
                right=BinarySearchTree(3),
            ),
        ),
        (
            (5, 3, 1, 4, 7, 6, 8),
            BinarySearchTree(
                5,
                left=BinarySearchTree(
                    3,
                    left=BinarySearchTree(1),
                    right=BinarySearchTree(4),
                ),
                right=BinarySearchTree(
                    7,
                    left=BinarySearchTree(6),
                    right=BinarySearchTree(8),
                ),
            ),
        ),
        (
            (10, 6, 3, 4, 16, 13, 12, 14, 15, 20, 23),
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
def test_pre_order_iteration(
    expected_elements: tuple[int, ...],
    tree: BinarySearchTree[int],
):
    assert tuple(tree.depth_first_pre_order_iterator()) == expected_elements


@pytest.mark.parametrize(
    ("expected_elements", "tree"),
    (
        (
            (1,),
            BinarySearchTree(1),
        ),
        (
            (1, 3, 2),
            BinarySearchTree(
                2,
                left=BinarySearchTree(1),
                right=BinarySearchTree(3),
            ),
        ),
        (
            (1, 4, 3, 6, 8, 7, 5),
            BinarySearchTree(
                5,
                left=BinarySearchTree(
                    3,
                    left=BinarySearchTree(1),
                    right=BinarySearchTree(4),
                ),
                right=BinarySearchTree(
                    7,
                    left=BinarySearchTree(6),
                    right=BinarySearchTree(8),
                ),
            ),
        ),
        (
            (4, 3, 6, 12, 15, 14, 13, 23, 20, 16, 10),
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
def test_post_order_iteration(
    expected_elements: tuple[int, ...],
    tree: BinarySearchTree[int],
):
    assert tuple(tree.depth_first_post_order_iterator()) == expected_elements
