class TreeNode:
    def __init__(self,val= None,left = None,right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self,root,targetSum):
        if not root:
            return False
        if root.left == None and root.right == None and root.val == targetSum:
            return True
        ans1  = self.pathSum(root.left,targetSum-root.val)
        ans2 = self.pathSum(root.right,targetSum-root.val)
        return ans1 or ans2
    
root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.right =TreeNode(1)
sol = Solution()
result = sol.pathSum(root,18)
print(result)
