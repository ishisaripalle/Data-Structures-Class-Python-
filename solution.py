from typing import TypeVar, List

# for more information on type hinting, check out https://docs.python.org/3/library/typing.html
T = TypeVar("T")  # represents generic type
Node = TypeVar("Node")  # represents a Node object (forward-declare to use in Node __init__)
DLL = TypeVar("DLL")


# pro tip: PyCharm auto-renders docstrings (the multiline strings under each function definition)
# in its "Documentation" view when written in the format we use here. Open the "Documentation"
# view to quickly see what a function does by placing your cursor on it and using CTRL + Q.
# https://www.jetbrains.com/help/pycharm/documentation-tool-window.html


class Node:
    """
    Implementation of a doubly linked list node.
    Do not modify.
    """
    __slots__ = ["value", "next", "prev", "child"]

    def __init__(self, value: T, next: Node = None, prev: Node = None, child: Node = None) -> None:
        """
        Construct a doubly linked list node.

        :param value: value held by the Node.
        :param next: reference to the next Node in the linked list.
        :param prev: reference to the previous Node in the linked list.
        :return: None.
        """
        self.next = next
        self.prev = prev
        self.value = value

        # The child attribute is only used for the application problem
        self.child = child

    def __repr__(self) -> str:
        """
        Represents the Node as a string.

        :return: string representation of the Node.
        """
        return f"Node({str(self.value)})"

    __str__ = __repr__


class DLL:
    """
    Implementation of a doubly linked list without padding nodes.
    Modify only below indicated line.
    """
    __slots__ = ["head", "tail", "size"]

    def __init__(self) -> None:
        """
        Construct an empty doubly linked list.

        :return: None.
        """
        self.head = self.tail = None
        self.size = 0

    def __repr__(self) -> str:
        """
        Represent the DLL as a string.

        :return: string representation of the DLL.
        """
        result = []
        node = self.head
        while node is not None:
            result.append(str(node))
            node = node.next
            if node is self.head:
                break
        return " <-> ".join(result)

    def __str__(self) -> str:
        """
        Represent the DLL as a string.

        :return: string representation of the DLL.
        """
        return repr(self)

    def __eq__(self, other: DLL) -> bool:
        """
        :param other: compares equality with this List
        :return: True if equal otherwise False
        """
        cur_node = self.head
        other_node = other.head
        while True:
            if cur_node != other_node:
                return False
            if cur_node is None and other_node is None:
                return True
            if cur_node is None or other_node is None:
                return False
            cur_node = cur_node.next
            other_node = other_node.next
            if cur_node is self.head and other_node is other.head:
                return True
            if cur_node is self.head or other_node is other.head:
                return False

    # MODIFY BELOW #
    # Refer to the classes provided to understand the problems better#

    def empty(self) -> bool:
        """
        INSERT DOCSTRINGS HERE!
        """
        if self.head is None and self.tail is None:
            return True
        return False

    def push(self, val: T, back: bool = True) -> None:
        """
        INSERT DOCSTRINGS HERE!
        """
        new_node = Node(val)
        if self.empty() == False:
            if not back:
                self.head.prev = new_node
                new_node.next = self.head
                self.head = new_node
            else:
                self.tail.next = new_node
                new_node.prev = self.tail
                self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node
        self.size += 1

    def pop(self, back: bool = True) -> None:
        """
        INSERT DOCSTRINGS HERE!
        """
        if self.size == 1:
            self.head = None
            self.tail = None
            self.size = 0
        if self.size > 1:
            if self.empty():
                if not back:
                    self.head = self.head.next
                    self.head.prev = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = None
            self.size -= 1

    def list_to_dll(self, source: List[T]) -> None:
        """
        INSERT DOCSTRINGS HERE!
        """
        self.size = 0
        if not self.empty():
            self.head = None
            self.tail = None
            for i in source:
                self.push(i)
        else:
            for i in source:
                self.push(i)

    def dll_to_list(self) -> List[T]:
        """
        INSERT DOCSTRINGS HERE!
        """
        the_list = []
        current = self.head
        if not self.empty():
            while current:
                the_list.append(current.value)
                current = current.next
            return the_list
        else:
            return the_list

    def _find_nodes(self, val: T, find_first: bool = False) -> List[Node]:
        """
        INSERT DOCSTRINGS HERE!
        """
        the_list = []
        current = self.head
        if not find_first:
            while current:
                if current.value is val:
                    the_list.append(current)
                    current = current.next
                else:
                    current = current.next
            return the_list
        else:
            while self.head:
                if self.head.value is val:
                    the_list.append(self.head.value)
                    break
            return the_list

    def find(self, val: T) -> Node:
        """
        INSERT DOCSTRINGS HERE!
        """
        the_list = self._find_nodes(val)
        if len(the_list) >= 1:
            return the_list[0]
        else:
            return None

    def find_all(self, val: T) -> List[Node]:
        """
        INSERT DOCSTRINGS HERE!
        """
        the_list = self._find_nodes(val)
        return the_list

    def _remove_node(self, to_remove: Node) -> None:
        """
        INSERT DOCSTRINGS HERE!
        """
        if to_remove is None:
            return
        if to_remove is self.head:
            if to_remove is self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
            self.size -= 1
        elif to_remove is self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
            self.size -= 1
        else:
            to_remove.next.prev = to_remove.prev
            to_remove.prev.next = to_remove.next
            self.size -= 1

    def remove(self, val: T) -> bool:
        """
        INSERT DOCSTRINGS HERE!
        """
        found_node = self.find(val)
        size = self.size
        self._remove_node(found_node)
        if self.size == size:
            return False
        return True

    def remove_all(self, val: T) -> int:
        """
        INSERT DOCSTRINGS HERE!
        """
        count = 0
        the_list = self.find_all(val)
        for i in range(len(the_list)):
            self._remove_node(the_list[i])
            count += 1
        return count

    def reverse(self) -> None:
        """
        INSERT DOCSTRINGS HERE!
        """
        current = self.head
        while current is not None:
            previous = current.next
            current.next = current.prev
            current.prev = previous
            current = current.prev
        previous = self.head
        self.head = self.tail
        self.tail = previous

def dream_escaper(dll: DLL) -> DLL:
    """
    INSERT DOCSTRING HERE!
    """
    new_dll = DLL()
    stack = []
    current = dll.head
    while current:
        if current.child:
            if current.next:
                stack.append(current)
            new_dll.push(current.value)
            current = current.child
        new_dll.push(current.value)
        if current.next is None and stack:
            current = stack.pop()
        current = current.next
    return new_dll


