# Singly Linked List Implementation

## Overview
This Python program implements a **singly linked list** using Object-Oriented Programming (OOP) principles. It includes a `Node` class for individual elements and a `LinkedList` class to manage the list, with methods to add nodes, print the list, and delete nodes at specific positions. The implementation includes robust exception handling for edge cases.

## Features
- **Node Class**: Represents a single node with data and a reference to the next node.
- **LinkedList Class**:
  - `append(data)`: Adds a node with the given data to the end of the list.
  - `print_list()`: Displays the list in a readable format (e.g., `10 -> 20 -> 30`).
  - `delete_nth_node(n)`: Removes the nth node (1-based index) from the list.
- **Exception Handling**:
  - Handles empty list scenarios.
  - Validates index ranges and prevents invalid (non-positive) indices.
- **Test Cases**: Includes a test function to demonstrate adding nodes, deleting nodes, and handling errors.

## Requirements
- Python 3.x
- No external libraries required.

## Usage
1. Save the program as `linked_list.py`.
2. Run the script using Python:
   ```bash
   python linked_list.py
   ```
3. The program will execute a series of test cases, showing the list operations and their results.

## Example Output
When you run `linked_list.py`, you'll see output like this:
```
=== Welcome to Linked List Fun ===

Step 1: Let's add some numbers to our list
Added 10 to the list!
Added 20 to the list!
Added 30 to the list!
Added 40 to the list!
Your list: 10 -> 20 -> 30 -> 40

Step 2: Let's remove the 2nd node
Removed the node at position 2!
Your list: 10 -> 30 -> 40

Step 3: Now, let's remove the first node
Removed the node at position 1!
Your list: 30 -> 40

Step 4: What happens if we try to remove from an empty list?
Error: Can't delete from an empty list!

Step 5: What if we try to remove a node that doesn't exist?
Error: Position 10 is too big for a list with 2 nodes.

Step 6: What if we use a position that's not allowed?
Error: Oops! The position must be a positive number.
```

## Code Structure
- **Node Class**: Defines a node with `data` and `next` attributes.
- **LinkedList Class**: Manages the list with a `head` pointer and `size` counter.
- **Test Function**: Demonstrates the functionality with sample operations.

## Notes
- The list uses a 1-based index for node deletion (e.g., position 1 is the first node).
- The program is designed to be beginner-friendly with clear comments and user-friendly error messages.
- Feel free to modify the test cases in the `test_linked_list()` function to experiment with different scenarios!
