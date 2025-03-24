class TreeNode:
    def __init__(self,val = None,left=None,right = None):
        self.val = val
        self.left = left 
        self.right = right 
class Solution:
    def height(self,root):
        if not root:
            return 0
        lh = self.height(root.left)
        rh = self.height(root.right)
        return max(lh , rh ) + 1
    
    def deepestLeaveSum(self,root):
        h = self.height(root)
        self.ans = 0
        self.helper(root,h)
        return self.ans
    def helper(self,root,height):
        if not root:
            return 
        if height == 1:
            self.ans += root.val
        self.helper(root.left,height-1)
        self.helper(root.right,height-1)
# Constructing the tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)
root.left.left.left = TreeNode(7)
root.right.right.right = TreeNode(8)

sol = Solution()
print(sol.deepestLeaveSum(root))  # Output: 15 (7 + 8)
