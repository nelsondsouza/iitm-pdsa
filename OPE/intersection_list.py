'''
Intersection Elements of two sorted linked list

class Node:
	def _init (self, data):
		self.data = data # Stores data
		self.next = None # Contains reference to the next node if it exists, otherwise None

Consider the following structure of a linked list, where each node is created using the given class Node. 
Suppose it has a head variable that contains the reference to the first node of the linked list.

You are given two singly linked lists, list1 and list2. Each linked list contains distinct integers sorted in ascending order. 
Your task is to find the intersection of these two linked lists, i.e., the elements that appear in both lists. Return a new linked list containing the intersection elements in ascending order.

Complete the function intersection_list(head1, head2), where head1 and head2 are references to the first nodes of two sorted linked lists list1 and list2 respectively. 
The function should return the reference of the first node of the linked list containing the intersection elements in ascending order. 
If there is no common element in both lists, return None

Sample input
1 3 5 7 9 11 #E€lements of first sorted linked list
1 2 4 5 6 9 #Elements of second sorted linked list

Output
Intersection List: 1 5 9 #Elements of intersection sorted linked list
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def intersection_list(head1, head2):
    result_head = None
    result_tail = None

    current1 = head1
    current2 = head2

    while current1 is not None and current2 is not None:
        if current1.data == current2.data:
            # Add the common element to the result linked list
            new_node = Node(current1.data)

            if result_head is None:
                result_head = new_node
                result_tail = new_node
            else:
                result_tail.next = new_node
                result_tail = new_node

            current1 = current1.next
            current2 = current2.next
        elif current1.data < current2.data:
            current1 = current1.next
        else:
            current2 = current2.next

    return result_head

# Helper function to print linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.data, end=" ")
        current = current.next
    print()

# Sample input
# Creating two sorted linked lists
list1 = Node(1)
list1.next = Node(3)
list1.next.next = Node(5)
list1.next.next.next = Node(7)
list1.next.next.next.next = Node(9)
list1.next.next.next.next.next = Node(11)

list2 = Node(1)
list2.next = Node(2)
list2.next.next = Node(4)
list2.next.next.next = Node(5)
list2.next.next.next.next = Node(6)
list2.next.next.next.next.next = Node(9)

# Finding intersection and printing result
result_list = intersection_list(list1, list2)
print("Intersection List:", end=" ")
print_linked_list(result_list)
