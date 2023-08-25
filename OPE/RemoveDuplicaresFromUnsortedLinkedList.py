'''
Remove Duplicates from Unsorted Linked List
class Node:
	def _init_(self, datasNone):
		self.data = data # Stores data
		selt.next = None # Contains reference to the next node if it exists, otherwise None
Consider an implementation of a singly linked list, where each node is created using the given class Node. Suppose it has a head variable that contains the reference to the first node of the linked list.
You are given non-empty unsorted singly linked list containing integers. Your task is to remove all duplicate elements from the list. The relative order of the first occurrence of distinct elements should be preserved in the output linked fist.
Complete the function remove_duplicate(head), that removes nodes with duplicate values from the given linked list. The function should modify the same input-linked list and should Not return any value.

Sample input
1 3 1 2 1 3 3 4 7 4 1 5 9 9 #Input Linked list elenents

Output
Output Linked List: 1 3 2 4 7 5 9 @Linked List elements after removing duplicates

'''

class Node:
    def __init__(self, data=None):
        self.data = data # Stores data
        self.next = None # Contains reference to the next node if it exists, otherwise None

def remove_duplicate(head):
    if not head:
        return

    seen = set()
    seen.add(head.data)
    current_node = head

    while current_node.next:
        if current_node.next.data in seen:
            current_node.next = current_node.next.next
        else:
            seen.add(current_node.next.data)
            current_node = current_node.next

def create_linked_list(values):
    head = Node(values[0])
    current_node = head
    for value in values[1:]:
        current_node.next = Node(value)
        current_node = current_node.next
    return head

# Sample Input
values = [1 1 1 3 3 3 2 1 3 3 4 7 4 1 5 9 9]
head = create_linked_list(values)

remove_duplicate(head)

current_node = head
while current_node:
    print(current_node.data, end=" ")
    current_node = current_node.next
# Output: 1 3 2 4 7 5 9
