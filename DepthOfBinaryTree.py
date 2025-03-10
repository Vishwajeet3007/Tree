class TreeNode:
    def __init__(self,val= None,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self,root):
        if not root:
            return 0
        left_height = self.maxDepth(root.left)
        right_height = self.maxDepth(root.right)
        return max(left_height,right_height) + 1
# Creating a sample binary tree:
#         1
#        / \
#       2   3
#      / \
#     4   5

# Define the tree nodes
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Create an instance of Solution and find max depth
sol = Solution()
print(sol.maxDepth(root))  # Output: 3
