'''
Binary Search Tree Operation

class Node:
	def init _ (self,data):
		self.left = None # Contains reference to the left child node if it exists, otherwise None
		self.data = data # Stores data
		self.right = None # Contains reference to the right child node if it exists, otherwise None

Consider an implementation of a Binary Search Tree, where each node is created using the given class Node. 
Suppose it has a root variable that contains the reference to the root node of the binary search tree.
Write a function comparison_count(root, k) That accepts the reference of root node root of a non-empty binary search tree and an integer k. 
The function returns the number of comparisons during the search k in the binary search tree. 
Return (number of comparison, True) if k exists in BST, otherwise returns (number of comparison, False).

Sample input 1
10 5 18 8 3 15 25 17
17

Output
(4, True)

Explanation: You have to compare the searching element with 10, 18, 15, and 17 in the given binary search tree. 
Hence, the output will be (4, True).

Sample input 2
10 5 18 8 3 15 25 17
24

Output
(3, False)

Explanation: You have to compare the searching element with 10, 18, and 25 in the given binary search tree. Hence, the output will be (3, False).

'''

class Node:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None

def comparison_count(root, k):
    if root is None:
        return (0, False)

    comparisons = 0
    current = root

    while current is not None:
        comparisons += 1

        if k == current.data:
            return (comparisons, True)
        elif k < current.data:
            current = current.left
        else:
            current = current.right

    return (comparisons, False)

# Sample input 1
# Creating the Binary Search Tree
root1 = Node(10)
root1.left = Node(5)
root1.right = Node(18)
root1.left.left = Node(8)
root1.left.right = Node(3)
root1.right.left = Node(15)
root1.right.right = Node(25)
root1.right.left.right = Node(17)

# Searching for 17
result1 = comparison_count(root1, 17)
print(result1)  # Output: (4, True)

# Sample input 2
# Creating another Binary Search Tree
root2 = Node(10)
root2.left = Node(5)
root2.right = Node(18)
root2.left.left = Node(8)
root2.left.right = Node(3)
root2.right.left = Node(15)
root2.right.right = Node(25)
root2.right.left.right = Node(17)

# Searching for 24
result2 = comparison_count(root2, 24)
print(result2)  # Output: (3, False)
