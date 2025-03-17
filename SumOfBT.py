class TreeNode:
    def __init__(self,val = None,left = None , right = None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumBT(self,root):
        if not root:
            return 0
        sum = 0
        sum += root.val
        left = self.sumBT(root.left)
        right = self.sumBT(root.right)
        sum += left + right
        return sum
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.left.left.left = TreeNode(4)

sol = Solution()
print(sol.sumBT(root))  
   
