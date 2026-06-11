# Given the root of a binary tree, determine if it is a valid binary search tree (BST).
# A valid BST is defined as follows:
# The left subtree of a node contains only nodes with keys strictly less than the node's key.
# The right subtree of a node contains only nodes with keys strictly greater than the node's key.
# Both the left and right subtrees must also be binary search trees.

 class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        inorder = []

        def dfs(node):
            if not node:
                return

            dfs(node.left)
            inorder.append(node.val)
            dfs(node.right)

        dfs(root)

        for i in range(1, len(inorder)):
            if inorder[i] <= inorder[i - 1]:
                return False

        return True