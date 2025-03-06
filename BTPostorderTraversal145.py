class TreeNode:
    def __init__(self,val=None,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postOrderTraversal(self,root):
        result = []
        def traverse(root):
            if root is None:
                return
            traverse(root.left)
            traverse(root.right)

            result.append(root.val)
        traverse(root)
        return result
# Define the tree structure
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Create an instance of the Solution class
solution = Solution()

# Call the postOrderTraversal method
result = solution.postOrderTraversal(root)

# Print the result
print(result)
