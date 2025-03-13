class TreeNode:
    def __init__(self,val=None,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self,root):
        ans = []
        self.helper(root,ans,0)
        return ans
    def helper(self,root,ans,level):
        if not root:
            return
        if len(ans) == level:
            ans.append(root.val)
        self.helper(root.left,ans,level + 1)
        self.helper(root.right,ans,level + 1)
# Constructing a sample tree
#        1
#       / \
#      2   3
#     / \    \
#    6   5    4
#   /
#  7
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)
root.right.right = TreeNode(4)
root.left.left = TreeNode(6)
root.left.left.left = TreeNode(7)

sol = Solution()
print(sol.rightSideView(root))  
