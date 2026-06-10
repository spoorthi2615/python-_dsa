class Node:
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

#level order traversal to represent a node in a binary tree
def level_order_traversal(root):
    if root is None:
        return []
    
    result = []
    queue = [root]
    
    while queue:
        current_node = queue.pop(0)
        result.append(current_node.value)
        
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)
    
    return result

#sum of all nodes in a binary tree
def sum_of_nodes(root):
    if root is None:
        return 0
    return root.value + sum_of_nodes(root.left) + sum_of_nodes(root.right)

#height of the tree
def height(root):
    if root is None:
        return -1
    return max(height(root.left),height(root.right))+1

#top view of the tree
def top_view(root):
d={}
q=[root]
root.level=0
while q:
    curr=q.pop(0)
    if curr.level not in d:
        d[curr.level]=curr.data
    if curr.left:
        curr.left.level=curr.level-1
        q.append(curr.left)
    if curr.right:
        curr.right.level=curr.level+1

#check whether a tree is binary search tree or not
def


    