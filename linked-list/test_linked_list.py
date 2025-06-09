import unittest
from linked_list.linked_list import LinkedList

class TestLinkedList(unittest.TestCase):
    def test_operations(self):
        ll = LinkedList()
        self.assertEqual(ll.display(), "List is empty.")
        ll.append(10)
        ll.append(20)
        ll.append(30)
        self.assertEqual(ll.display(), "10 -> 20 -> 30")
        self.assertEqual(ll.delete_nth_node(2), "Node at position 2 with value 20 deleted.")
        self.assertEqual(ll.display(), "10 -> 30")
        with self.assertRaises(IndexError):
            ll.delete_nth_node(10)

if __name__ == "__main__":
    unittest.main()
