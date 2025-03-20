class TreeNode:
    def __init__(self,val=None,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def LCAofBST(self,root,p,q):
        if not root:
            return None
        temp = root
        while temp:
            if temp.val > p.val and temp.val > q.val:
                temp = temp.left
            elif temp.val < p.val and temp.val < q.val:
                temp = temp.right
            else:
                break
        return temp
# Example Usage:
# Constructing the BST
"""
        6
       / \
      2   8
     / \  / \
    0   4 7 9
       / \
      3   5
"""
root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(8)
root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)

# Finding LCA of 2 and 8
sol = Solution()
p = root.left  # Node with value 2
q = root.right  # Node with value 8
lca = sol.LCAofBST(root, p, q)
print("LCA of 2 and 8 is:", lca.val)  # Output: 6

# Finding LCA of 2 and 4
p = root.left  # Node with value 2
q = root.left.right  # Node with value 4
lca = sol.LCAofBST(root, p, q)
print("LCA of 2 and 4 is:", lca.val)  # Output: 2