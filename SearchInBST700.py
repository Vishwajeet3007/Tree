class TreeNode:
    def __init__(self,val=None,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    def SearchInBST(self,root,val):
        while root:
            if root.val == val:
                return True
            elif root.val > val:
                root = root.left
            else:
                root = root.right
        return False

# Creating a sample BST
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.left = TreeNode(12)
root.right.right = TreeNode(18)

# Searching for a value in BST
solution = Solution()
val_to_search = 7
result = solution.SearchInBST(root, val_to_search)

# Output the result
print(f"Value {val_to_search} found in BST: {result}")  # Output: True

val_to_search = 20
result = solution.SearchInBST(root, val_to_search)

print(f"Value {val_to_search} found in BST: {result}")  # Output: False
