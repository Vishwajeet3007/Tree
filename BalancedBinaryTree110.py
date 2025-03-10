class TreeNode:
    def __init__(self,val=None,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
class Solution:
    def __init__(self):
        self.balanced_factor = True
    def depth(self,root):
        if root is None:
            return 0
        left_height = self.depth(root.left)
        right_height = self.depth(root.right)
        if abs(left_height-right_height) > 1:
            self.balanced_factor = False
        return max(left_height,right_height) + 1
    def isBalanced(self,root):
        self.balanced_factor=True
        self.depth(root)
        return self.balanced_factor
# Balanced Tree:
#         1
#        / \
#       2   3
#      / \
#     4   5

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

sol = Solution()
print(sol.isBalanced(root))  # Output: True

# Unbalanced Tree:
#         1
#        /
#       2
#      /
#     3

root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.left.left = TreeNode(3)

sol = Solution()
print(sol.isBalanced(root2))  # Output: False
