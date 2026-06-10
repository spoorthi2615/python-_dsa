# #Given a binary search tree (BST), find the lowest common ancestor (LCA) 
# node of two given nodes in the BST.
# According to the definition of LCA on Wikipedia:
#  “The lowest common ancestor is defined between two nodes p and q 
# as the lowest node in T that has both p and q as descendants 
# (where we allow a node to be a descendant of itself).”
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        while root:
            if p.val<root.val and q.val<root.val:
                root=root.left
            elif p.val>root.val and q.val>root.val:
                root=root.right
            else:
                return root