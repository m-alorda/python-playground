"""Simple Binary Tree implementation"""

from collections.abc import Collection, Iterator, MutableSequence
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

    def breadth_first_iterator(
        self,
    ) -> Iterator[T]:
        """Iterate through all tree elements, layer by layer

        >>> tuple(
        ...     BinarySearchTree(
        ...         4,
        ...         left=BinarySearchTree(
        ...             2,
        ...             left=BinarySearchTree(1),
        ...             right=BinarySearchTree(3),
        ...         ),
        ...         right=BinarySearchTree(
        ...             6,
        ...             left=BinarySearchTree(5),
        ...             right=BinarySearchTree(7),
        ...         ),
        ...     ).breadth_first_iterator()
        ... )
        (4, 2, 6, 1, 3, 5, 7)
        """
        yield from self._breadth_first_iterator(tree_queue=list())

    def _breadth_first_iterator(
        self,
        tree_queue: MutableSequence["BinarySearchTree[T]"],
    ) -> Iterator[T]:
        yield self.val
        if self._left is not None:
            tree_queue.append(self._left)
        if self._right is not None:
            tree_queue.append(self._right)
        if len(tree_queue) > 0:
            yield from tree_queue.pop(0)._breadth_first_iterator(tree_queue)

    def depth_first_pre_order_iterator(self) -> Iterator[T]:
        """Iterate through all tree elements, in value-left-right order

        >>> tuple(
        ...     BinarySearchTree(
        ...         4,
        ...         left=BinarySearchTree(
        ...             2,
        ...             left=BinarySearchTree(1),
        ...             right=BinarySearchTree(3),
        ...         ),
        ...         right=BinarySearchTree(
        ...             6,
        ...             left=BinarySearchTree(5),
        ...             right=BinarySearchTree(7),
        ...         ),
        ...     ).depth_first_pre_order_iterator()
        ... )
        (4, 2, 1, 3, 6, 5, 7)
        """
        yield self.val
        if self._left is not None:
            yield from self._left.depth_first_pre_order_iterator()
        if self._right is not None:
            yield from self._right.depth_first_pre_order_iterator()

    def depth_first_in_order_iterator(self) -> Iterator[T]:
        """Iterate through all tree elements, in left-value-right order (sort order)

        >>> tuple(
        ...     BinarySearchTree(
        ...         4,
        ...         left=BinarySearchTree(
        ...             2,
        ...             left=BinarySearchTree(1),
        ...             right=BinarySearchTree(3),
        ...         ),
        ...         right=BinarySearchTree(
        ...             6,
        ...             left=BinarySearchTree(5),
        ...             right=BinarySearchTree(7),
        ...         ),
        ...     ).depth_first_in_order_iterator()
        ... )
        (1, 2, 3, 4, 5, 6, 7)
        """
        if self._left is not None:
            yield from self._left.depth_first_in_order_iterator()
        yield self.val
        if self._right is not None:
            yield from self._right.depth_first_in_order_iterator()

    def depth_first_post_order_iterator(self) -> Iterator[T]:
        """Iterate through all tree elements, in left-right-value order

        >>> tuple(
        ...     BinarySearchTree(
        ...         4,
        ...         left=BinarySearchTree(
        ...             2,
        ...             left=BinarySearchTree(1),
        ...             right=BinarySearchTree(3),
        ...         ),
        ...         right=BinarySearchTree(
        ...             6,
        ...             left=BinarySearchTree(5),
        ...             right=BinarySearchTree(7),
        ...         ),
        ...     ).depth_first_post_order_iterator()
        ... )
        (1, 3, 2, 5, 7, 6, 4)
        """
        if self._left is not None:
            yield from self._left.depth_first_post_order_iterator()
        if self._right is not None:
            yield from self._right.depth_first_post_order_iterator()
        yield self.val

    @property
    def height(self) -> int:
        """1-based height of the tree

        >>> BinarySearchTree(1).height
        1

        >>> BinarySearchTree(2, left=BinarySearchTree(1)).height
        2
        """
        left_height = self._left.height if self._left is not None else 0
        right_height = self._right.height if self._right is not None else 0
        return 1 + (left_height if left_height > right_height else right_height)
