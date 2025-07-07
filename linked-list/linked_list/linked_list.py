from .node import Node

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return "Node added as head."
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        return f"Node with value {data} appended."

    def display(self):
        values = []
        current = self.head
        while current:
            values.append(str(current.data))
            current = current.next
        return " -> ".join(values) if values else "List is empty."

    def delete_nth_node(self, n):
        if n < 1:
            raise ValueError("Index should be 1 or greater.")

        if not self.head:
            raise IndexError("Cannot delete from empty list.")

        if n == 1:
            self.head = self.head.next
            return "Head node deleted."

        current = self.head
        for _ in range(n - 2):
            if not current.next:
                raise IndexError("Index out of range.")
            current = current.next

        if not current.next:
            raise IndexError("Index out of range.")

        deleted = current.next.data
        current.next = current.next.next
        return f"Node at position {n} with value {deleted} deleted."
