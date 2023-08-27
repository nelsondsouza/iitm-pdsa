# 
**Binary Search Tree**

```python
class Node:
    def __init__(self,data):
        self.left = None # Contains reference to the left child node if it exists, otherwise None
        self.data = data # Stores data
        self.right = None # Contains reference to the right child node if it exists, otherwise None

```

Consider an implementation of a  **Binary Search Tree**, where each node is created using the given class  `Node`. Suppose it has a  `root`  variable that contains the reference to the root node of the binary search tree.

Complete the function  **insert_element(root, k)**  That accepts the reference of root node  `root`  of non-empty binary search tree and an integer  `k`. The function insert the element  `k`  at the correct position of the binary search tree. The function does not print or return anything.

**Sample Input 1**

```
10 #root element
5 18 8 3 15 25 17 #Elements to be insert in bst in given order

```

**Output**

```
3 5 8 10 15 17 18 25 #Inorder
10 5 3 8 18 15 17 25 #Preorder
3 8 5 17 15 25 18 10 #Postorder

```

**Explanation:-**  After insertion all element, following is the resultant BST
![image](https://github.com/nelsondsouza/iitm-pdsa/assets/19646977/ab1f5777-63e2-4c10-996f-5f11050064bb)

```python
class Node:
    def __init__(self,data):
        self.left = None
        self.data = data
        self.right = None

def insert_element(root,k):
    # If the tree is empty, return a new node
    if root is None:
        return Node(k)
    # Otherwise, recur down the tree
    if k < root.data:
        root.left = insert_element(root.left, k)
    else:
        root.right = insert_element(root.right, k)
    # Return the (unchanged) node pointer
    return root

def inorder(root):
    if root:
        # First recur for the left child
        inorder(root.left)
        # Then print the data of the node
        print(root.data)
        # Now recur for the right child
        inorder(root.right)

def preorder(root):
    if root:
        # First print the data of the node
        print(root.data)
        # Then recur for the left child
        preorder(root.left)
        # Finally recur for the right child
        preorder(root.right)

def postorder(root):
    if root:
        # First recur for the left child
        postorder(root.left)
        # the recur for the right child
        postorder(root.right)
        # Now print the data of the node
        print(root. Data)

```
