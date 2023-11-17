# Class for Node in binary tree.
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Recursive function to insert a number in binary tree.
def insert(root, data):
    if root is None:
        return Node(data)
    elif data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)
    return root


# Function to insert list of numbers in binary tree.
def insert_list(tree, list):
    if not list:
        return tree
    tree = insert(tree, list[0])
    return insert_list(tree, list[1:])


# Function to print tree
def print_tree(root):
    if root is None:
        return []
    queue = [root]
    result = []
    while queue:
        node = queue.pop(0)
        temp = []
        if node.left:
            temp.append(node.left.data)
        else:
            temp.append(None)
        temp.append(node.data)
        if node.right:
            temp.append(node.right.data)
        else:
            temp.append(None)
        result.append(temp)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result


tree = None
lst = [10, 5, 15, 3, 7, 12, 18]

tree = insert_list(tree, lst)
print(print_tree(tree))

input("\n\nPress Enter to close...")
