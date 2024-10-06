# Define a Node class
class Node:
    def __init__(self, data):
        self.data = data  # Store data
        self.next = None  # Store reference (link) to the next node

# Define a LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None  # Initialize the head of the linked list

    # Method to append new nodes to the end of the list
    def append(self, data):
        new_node = Node(data)  # Create a new node
        if self.head is None:  # If the list is empty, the new node is the head
            self.head = new_node
            return
        last = self.head
        while last.next:  # Traverse the list to find the last node
            last = last.next
        last.next = new_node  # Append the new node at the end

    # Method to display the linked list
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> " if current.next else "\n")
            current = current.next

# Create a linked list and append the given data
ll = LinkedList()
ll.append("Header")
ll.append(44)
ll.append(36)
ll.append(90)
ll.append(10)
ll.append(60)
ll.append(99)

# Display the linked list
ll.display()
