# Node class: Represents a single element in our linked list
class Node:
    def __init__(self, data):
        self.data = data  # The value stored in this node
        self.next = None  # Points to the next node (or None if it's the last)

# LinkedList class: Manages the entire chain of nodes
class LinkedList:
    def __init__(self):
        self.head = None  # The first node in the list
        self.size = 0     # Keeps track of how many nodes we have

    # Add a new node with the given data to the end of the list
    def append(self, data):
        new_node = Node(data)
        if not self.head:  # If the list is empty
            self.head = new_node
        else:  # Find the last node and attach the new one
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1
        print(f"Added {data} to the list!")

    # Display the list in a friendly, readable format
    def print_list(self):
        if not self.head:
            print("The list is empty. Nothing to show yet!")
            return
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print("Your list: " + " -> ".join(elements))

    # DeleteNth node (1-based index, like 1st, 2nd, etc.)
    def delete_nth_node(self, n):
        try:
            if n < 1:
                raise ValueError("Oops! The position must be a positive number.")
            if not self.head:
                raise IndexError("Can't delete from an empty list!")
            if n > self.size:
                raise IndexError(f"Position {n} is too big for a list with {self.size} nodes.")

            # If we're deleting the first node
            if n == 1:
                self.head = self.head.next
                self.size -= 1
                print(f"Removed the node at position 1!")
                return

            # Find the node just before the one we want to delete
            current = self.head
            for i in range(n - 2):
                current = current.next

            # Skip over the node to delete it
            if current.next:
                current.next = current.next.next
                self.size -= 1
                print(f"Removed the node at position {n}!")

        except ValueError as e:
            print(f"Error: {e}")
        except IndexError as e:
            print(f"Error: {e}")

# Let's test our linked list with some fun examples
def test_linked_list():
    print("=== Welcome to Linked List Fun ===")
    my_list = LinkedList()

    # Test 1: Building a list with some numbers
    print("\nStep 1: Let's add some numbers to our list")
    for num in [10, 20, 30, 40]:
        my_list.append(num)
    my_list.print_list()

    # Test 2: Removing a node in the middle
    print("\nStep 2: Let's remove the 2nd node")
    my_list.delete_nth_node(2)
    my_list.print_list()

    # Test 3: Removing the first node
    print("\nStep 3: Now, let's remove the first node")
    my_list.delete_nth_node(1)
    my_list.print_list()

    # Test 4: Trying to remove from an empty list
    print("\nStep 4: What happens if we try to remove from an empty list?")
    empty_list = LinkedList()
    empty_list.delete_nth_node(1)

    # Test 5: Trying a position that's too big
    print("\nStep 5: What if we try to remove a node that doesn't exist?")
    my_list.delete_nth_node(10)

    # Test 6: Trying an invalid position
    print("\nStep 6: What if we use a position that's not allowed?")
    my_list.delete_nth_node(0)

if __name__ == "__main__":
    test_linked_list()
