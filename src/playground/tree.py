"""Simple Binary Tree implementation"""

from collections.abc import Collection, Iterator
from typing import Any, Generic, Protocol, TypeVar

T = TypeVar("T", bound="_Comparable")


class _Comparable(Protocol):
    def __eq__(self, other: Any, /) -> bool: ...
    def __lt__(self: T, other: T, /) -> bool: ...
    def __gt__(self: T, other: T, /) -> bool: ...
    def __le__(self: T, other: T, /) -> bool: ...
    def __ge__(self: T, other: T, /) -> bool: ...


class BinarySearchTree(Generic[T], Collection[T]):
    """Simple binary search tree implementation

    >>> BinarySearchTree(2, left=BinarySearchTree(1), right=BinarySearchTree(3))
    <playground.tree.BinarySearchTree object at ...>

    It allows duplicate values. For example:

    >>> BinarySearchTree(1, left=BinarySearchTree(1))
    <playground.tree.BinarySearchTree object at ...>

    It does not allow instantiating an unsorted tree. For example:

    >>> BinarySearchTree(1, left=BinarySearchTree(2)) # doctest: +SKIP
    Traceback (most recent call last):
        ...
    ValueError: Unsorted BinarySearchTree: 2 cannot be to the left of 1

    By default, it is iterated in breadth-first order:

    >>> tuple(BinarySearchTree(2, left=BinarySearchTree(1), right=BinarySearchTree(3))) # doctest: +SKIP
    (2, 1, 3)

    It has a 1-based height:

    >>> BinarySearchTree(1).height # doctest: +SKIP
    1

    >>> BinarySearchTree(2, left=BinarySearchTree(1)).height # doctest: +SKIP
    2
    """

    def __init__(
        self,
        val: T,
        *,
        left: "BinarySearchTree[T] | None" = None,
        right: "BinarySearchTree[T] | None" = None,
    ) -> None:
        self.val = val
        self._left = left
        self._right = right

    def __contains__(self, x: object) -> bool:
        raise NotImplementedError

    def __iter__(self) -> Iterator[T]:
        return self.breadth_first_iterator()

    def __len__(self) -> int:
        raise NotImplementedError

    def breadth_first_iterator(self) -> Iterator[T]:
        raise NotImplementedError

    def depth_first_pre_order_iterator(self) -> Iterator[T]:
        raise NotImplementedError

    def depth_first_in_order_iterator(self) -> Iterator[T]:
        raise NotImplementedError

    def depth_first_post_order_iterator(self) -> Iterator[T]:
        raise NotImplementedError

    @property
    def height(self) -> int:
        raise NotImplementedError
