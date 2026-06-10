class Node
#in order to represent a node in a binary tree
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def inorder_traversal(root):
    if root is None:
        return []
    return inorder_traversal(root.left) + [root.value] + inorder_traversal(root.right)

#in preorder to represent a node in a binary tree
def preorder_traversal(root):
    if root is None:
        return []
    return [root.value] + preorder_traversal(root.left) + preorder_traversal(root.right)   

#in postorder to represent a node in a binary tree 
def postorder_traversal(root):
    if root is None:
        return []
    return postorder_traversal(root.left) + postorder_traversal(root.right) + [root.value] 
 
# Example usage:
if __name__ == "__main__":
    # Create a sample binary tree
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print("Inorder Traversal:", inorder_traversal(root))  # Output: [4, 2, 5, 1, 3]
    print("Preorder Traversal:", preorder_traversal(root))  # Output: [1, 2, 4, 5, 3]
    print("Postorder Traversal:", postorder_traversal(root))  # Output: [4, 5, 2, 3, 1]