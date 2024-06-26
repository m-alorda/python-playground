"""Simple Binary Tree implementation"""

from collections import deque
from collections.abc import Collection, Iterator
from typing import Any, Generic, Protocol, TypeVar

T = TypeVar("T", bound="_Comparable")


class _Comparable(Protocol):
    def __eq__(self, other: Any, /) -> bool: ...
    def __lt__(self: T, other: T, /) -> bool: ...
    def __gt__(self: T, other: T, /) -> bool: ...
    def __le__(self: T, other: T, /) -> bool: ...
    def __ge__(self: T, other: T, /) -> bool: ...


class BinaryTreeNode(Generic[T]):
    def __init__(
        self,
        val: T,
        *,
        left: "BinaryTreeNode[T] | None" = None,
        right: "BinaryTreeNode[T] | None" = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


class BinarySearchTree(Generic[T], Collection[T]):
    """Simple binary search tree implementation

    >>> tree = BinarySearchTree()
    >>> tree.add(1)
    >>> tree.add(3)
    >>> tree.add(2)
    >>> tuple(tree)
    (1, 2, 3)

    It can be created from a binary tree represented by BinaryTreeNode:

    >>> BinarySearchTree(
    ...     BinaryTreeNode(
    ...         2,
    ...         left=BinaryTreeNode(1),
    ...         right=BinaryTreeNode(3),
    ...     )
    ... )
    <playground.tree.BinarySearchTree object at ...>

    It allows duplicate values. For example:

    >>> BinarySearchTree(BinaryTreeNode(1, left=BinaryTreeNode(1)))
    <playground.tree.BinarySearchTree object at ...>

    It does not allow instantiating an unsorted tree. For example:

    >>> BinarySearchTree(BinaryTreeNode(1, left=BinaryTreeNode(2)))
    Traceback (most recent call last):
        ...
    ValueError: Unsorted BinarySearchTree: 2 cannot be to the left of 1

    By default, it is iterated depth-first in-order:

    >>> tuple(
    ...     BinarySearchTree(
    ...         BinaryTreeNode(
    ...             2,
    ...             left=BinaryTreeNode(1),
    ...             right=BinaryTreeNode(3),
    ...         )
    ...     )
    ... )
    (1, 2, 3)
    """

    def __init__(
        self,
        root: BinaryTreeNode[T] | None = None,
    ) -> None:
        self._root = root
        self._validate(self._root)

    def _validate(
        self,
        root: BinaryTreeNode[T] | None,
        lower_bound: T | None = None,
        upper_bound: T | None = None,
    ) -> None:
        if root is None:
            return
        if lower_bound is not None and root.val < lower_bound:
            raise ValueError(
                "Unsorted BinarySearchTree: "
                f"{root.val} cannot be to the right of {lower_bound}"
            )
        if upper_bound is not None and root.val > upper_bound:
            raise ValueError(
                "Unsorted BinarySearchTree: "
                f"{root.val} cannot be to the left of {upper_bound}"
            )
        self._validate(
            root.left,
            lower_bound=lower_bound,
            upper_bound=root.val,
        )
        self._validate(
            root.right,
            lower_bound=root.val,
            upper_bound=upper_bound,
        )

    def __contains__(self, x: object) -> bool:
        if not self._root:
            return False
        if not isinstance(x, self._root.val.__class__):
            return False
        return self._contains_type_safe(self._root, x)

    def _contains_type_safe(
        self,
        root: BinaryTreeNode[T] | None,
        x: T,
    ) -> bool:
        if not root:
            return False
        if x == root.val:
            return True
        if x < root.val:
            return self._contains_type_safe(root.left, x)
        return self._contains_type_safe(root.right, x)

    def __iter__(self) -> Iterator[T]:
        return self.depth_first_in_order_iterator()

    def __len__(self) -> int:
        return sum(1 for _ in self.depth_first_in_order_iterator())

    def breadth_first_iterator(
        self,
    ) -> Iterator[T]:
        """Iterate through all tree elements, layer by layer

        >>> tuple(
        ...     BinarySearchTree(
        ...         BinaryTreeNode(
        ...             4,
        ...             left=BinaryTreeNode(
        ...                 2,
        ...                 left=BinaryTreeNode(1),
        ...                 right=BinaryTreeNode(3),
        ...             ),
        ...             right=BinaryTreeNode(
        ...                 6,
        ...                 left=BinaryTreeNode(5),
        ...                 right=BinaryTreeNode(7),
        ...             ),
        ...         )
        ...     ).breadth_first_iterator()
        ... )
        (4, 2, 6, 1, 3, 5, 7)
        """
        q: deque[BinaryTreeNode[T]] = deque()
        if self._root:
            q.append(self._root)
        while len(q) > 0:
            node = q.popleft()
            yield node.val
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    def depth_first_pre_order_iterator(self) -> Iterator[T]:
        """Iterate through all tree elements, in value-left-right order

        >>> tuple(
        ...     BinarySearchTree(
        ...         BinaryTreeNode(
        ...             4,
        ...             left=BinaryTreeNode(
        ...                 2,
        ...                 left=BinaryTreeNode(1),
        ...                 right=BinaryTreeNode(3),
        ...             ),
        ...             right=BinaryTreeNode(
        ...                 6,
        ...                 left=BinaryTreeNode(5),
        ...                 right=BinaryTreeNode(7),
        ...             ),
        ...         )
        ...     ).depth_first_pre_order_iterator()
        ... )
        (4, 2, 1, 3, 6, 5, 7)
        """
        yield from self._depth_first_pre_order_iterator(self._root)

    def _depth_first_pre_order_iterator(
        self,
        root: BinaryTreeNode[T] | None,
    ) -> Iterator[T]:
        if not root:
            return
        yield root.val
        yield from self._depth_first_pre_order_iterator(root.left)
        yield from self._depth_first_pre_order_iterator(root.right)

    def depth_first_in_order_iterator(self) -> Iterator[T]:
        """Iterate through all tree elements, in left-value-right order (sort order)

        >>> tuple(
        ...     BinarySearchTree(
        ...         BinaryTreeNode(
        ...             4,
        ...             left=BinaryTreeNode(
        ...                 2,
        ...                 left=BinaryTreeNode(1),
        ...                 right=BinaryTreeNode(3),
        ...             ),
        ...             right=BinaryTreeNode(
        ...                 6,
        ...                 left=BinaryTreeNode(5),
        ...                 right=BinaryTreeNode(7),
        ...             ),
        ...         )
        ...     ).depth_first_in_order_iterator()
        ... )
        (1, 2, 3, 4, 5, 6, 7)
        """
        yield from self._depth_first_in_order_iterator(self._root)

    def _depth_first_in_order_iterator(
        self,
        root: BinaryTreeNode[T] | None,
    ) -> Iterator[T]:
        if not root:
            return
        yield from self._depth_first_in_order_iterator(root.left)
        yield root.val
        yield from self._depth_first_in_order_iterator(root.right)

    def depth_first_post_order_iterator(self) -> Iterator[T]:
        """Iterate through all tree elements, in left-right-value order

        >>> tuple(
        ...     BinarySearchTree(
        ...         BinaryTreeNode(
        ...             4,
        ...             left=BinaryTreeNode(
        ...                 2,
        ...                 left=BinaryTreeNode(1),
        ...                 right=BinaryTreeNode(3),
        ...             ),
        ...             right=BinaryTreeNode(
        ...                 6,
        ...                 left=BinaryTreeNode(5),
        ...                 right=BinaryTreeNode(7),
        ...             ),
        ...         )
        ...     ).depth_first_post_order_iterator()
        ... )
        (1, 3, 2, 5, 7, 6, 4)
        """
        yield from self._depth_first_post_order_iterator(self._root)

    def _depth_first_post_order_iterator(
        self,
        root: BinaryTreeNode[T] | None,
    ) -> Iterator[T]:
        if not root:
            return
        yield from self._depth_first_post_order_iterator(root.left)
        yield from self._depth_first_post_order_iterator(root.right)
        yield root.val

    @property
    def height(self) -> int:
        """1-based height of the tree

        >>> BinarySearchTree().height
        0

        >>> BinarySearchTree(BinaryTreeNode(1)).height
        1

        >>> BinarySearchTree(BinaryTreeNode(2, left=BinaryTreeNode(1))).height
        2
        """
        return self._height(self._root)

    def _height(self, root: BinaryTreeNode[T] | None) -> int:
        if not root:
            return 0
        return 1 + max(self._height(root.left), self._height(root.right))

    def add(self, val: T) -> None:
        """Add a value to the tree

        >>> tree = BinarySearchTree()
        >>> tree.add(1)
        >>> tree.add(2)
        >>> tree.add(3)
        >>> tuple(tree)
        (1, 2, 3)

        Duplicates are allowed.

        >>> tree = BinarySearchTree()
        >>> tree.add(1)
        >>> tree.add(1)
        >>> tuple(tree)
        (1, 1)
        """
        node = BinaryTreeNode(val)
        if not self._root:
            self._root = node
            return
        self._add(self._root, node)

    def _add(self, root: BinaryTreeNode[T], node: BinaryTreeNode[T]) -> None:
        if root.val > node.val:
            if root.left:
                self._add(root.left, node)
            else:
                root.left = node
        else:
            if root.right:
                self._add(root.right, node)
            else:
                root.right = node

    def remove(self, val: T) -> None:
        """Remove a value from the tree. Raises a ValueError if not present

        >>> tree = BinarySearchTree(BinaryTreeNode(2, left=BinaryTreeNode(1)))
        >>> tree.remove(1)
        >>> tuple(tree)
        (2,)
        >>> tree.remove(2)
        >>> tuple(tree)
        ()
        >>> tree.remove(3)
        Traceback (most recent call last):
            ...
        ValueError: 3 is not contained in the tree
        """
        self._root = self._remove(self._root, val)

    def _remove(
        self,
        root: BinaryTreeNode[T] | None,
        val: T,
    ) -> BinaryTreeNode[T] | None:
        if not root:
            raise ValueError(f"{val} is not contained in the tree")

        if root.val == val:
            if root.right:
                if root.left:
                    self._add(root.right, root.left)
                    return root.right
                return root.right
            if root.left:
                return root.left
            return None

        if root.val > val:
            root.left = self._remove(root.left, val)
        else:
            root.right = self._remove(root.right, val)

        return root

    def balance(self) -> None:
        """Balances this tree to have minimum height

        >>> tree = BinarySearchTree(
        ...     BinaryTreeNode(
        ...         1,
        ...         right=BinaryTreeNode(
        ...             2,
        ...             right=BinaryTreeNode(3),
        ...         ),
        ...     ),
        ... )
        >>> tree.balance()
        >>> tree.height
        2

        Balancing an empty tree has no effect:

        >>> tree = BinarySearchTree()
        >>> tree.balance()
        >>> tree.height
        0
        """
        ordered_elements = tuple(self)
        self._root = self._ordered_list_to_balanced_tree(
            ordered_elements=ordered_elements,
            start_index=0,
            end_index=len(ordered_elements) - 1,
        )

    def _ordered_list_to_balanced_tree(
        self,
        ordered_elements: tuple[T, ...],
        start_index: int,
        end_index: int,
    ) -> BinaryTreeNode[T] | None:
        if start_index > end_index:
            return None

        middle_index = start_index + (end_index - start_index) // 2
        root = BinaryTreeNode(ordered_elements[middle_index])

        root.left = self._ordered_list_to_balanced_tree(
            ordered_elements=ordered_elements,
            start_index=start_index,
            end_index=middle_index - 1,
        )
        root.right = self._ordered_list_to_balanced_tree(
            ordered_elements=ordered_elements,
            start_index=middle_index + 1,
            end_index=end_index,
        )

        return root
