class TreeNode:
    def __init__(self,val=None,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
class Solution:
    def kthSmallest(self,root,k):
        self.count = 0
        self.ans = None
        self.helper(root,k)
        return self.ans
    
    def helper(self,root,k):
        if not root:
            return
        
        self.helper(root.right,k)
        self.count += 1
        if self.count == k:
            self.ans = root.val
            return
        
        self.helper(root.left,k)

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(7)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.right = TreeNode(8)

sol = Solution()
print(sol.kthSmallest(root, 3))  # Find the 3rd smallest element


        