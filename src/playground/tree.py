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

    >>> BinarySearchTree(1, left=BinarySearchTree(2))
    Traceback (most recent call last):
        ...
    ValueError: Unsorted BinarySearchTree: 2 cannot be to the left of 1

    By default, it is iterated in depth-first in-order:

    >>> tuple(
    ...     BinarySearchTree(2, left=BinarySearchTree(1), right=BinarySearchTree(3))
    ... )
    (1, 2, 3)

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
        self._validate()

    def _validate(
        self,
        lower_bound: T | None = None,
        upper_bound: T | None = None,
    ) -> None:
        if lower_bound is not None and self.val < lower_bound:
            raise ValueError(
                "Unsorted BinarySearchTree: "
                f"{self.val} cannot be to the right of {lower_bound}"
            )
        if upper_bound is not None and self.val > upper_bound:
            raise ValueError(
                "Unsorted BinarySearchTree: "
                f"{self.val} cannot be to the left of {upper_bound}"
            )
        if self._left is not None:
            self._left._validate(
                lower_bound=lower_bound,
                upper_bound=self.val,
            )
        if self._right is not None:
            self._right._validate(
                lower_bound=self.val,
                upper_bound=upper_bound,
            )

    def __contains__(self, x: object) -> bool:
        if not isinstance(x, self.val.__class__):
            return False
        return self._contains_type_safe(x)

    def _contains_type_safe(self, x: T) -> bool:
        if x == self.val:
            return True
        if x < self.val:
            if self._left is None:
                return False
            return self._left._contains_type_safe(x)
        if self._right is None:
            return False
        return self._right._contains_type_safe(x)

    def __iter__(self) -> Iterator[T]:
        return self.depth_first_in_order_iterator()

    def __len__(self) -> int:
        length = 1
        if self._left is not None:
            length += len(self._left)
        if self._right is not None:
            length += len(self._right)
        return length

    def breadth_first_iterator(self) -> Iterator[T]:
        raise NotImplementedError

    def depth_first_pre_order_iterator(self) -> Iterator[T]:
        yield self.val
        if self._left is not None:
            yield from self._left.depth_first_pre_order_iterator()
        if self._right is not None:
            yield from self._right.depth_first_pre_order_iterator()

    def depth_first_in_order_iterator(self) -> Iterator[T]:
        if self._left is not None:
            yield from self._left.depth_first_in_order_iterator()
        yield self.val
        if self._right is not None:
            yield from self._right.depth_first_in_order_iterator()

    def depth_first_post_order_iterator(self) -> Iterator[T]:
        if self._left is not None:
            yield from self._left.depth_first_post_order_iterator()
        if self._right is not None:
            yield from self._right.depth_first_post_order_iterator()
        yield self.val

    @property
    def height(self) -> int:
        raise NotImplementedError
