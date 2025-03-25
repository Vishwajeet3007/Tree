class TreeNode:
    def __init__(self,val = None , left = None,right= None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def bstToGST(self,root):
        self.sum = 0
        self.helper(root)
        return root
    def helper(self,root):
        if not root:
            return 
        self.helper(root.right)
        self.sum += root.val
        root.val = self.sum
        self.helper(root.left)
def inorder(root):
    return inorder(root.left) + [root.val] + inorder(root.right) if root else []

# Constructing a sample BST
root = TreeNode(4)
root.left = TreeNode(1)
root.right = TreeNode(6)
root.left.left = TreeNode(0)
root.left.right = TreeNode(2, right=TreeNode(3))
root.right.left = TreeNode(5)
root.right.right = TreeNode(7, right=TreeNode(8))

sol = Solution()
sol.bstToGST(root)

print(inorder(root)) 