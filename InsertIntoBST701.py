class TreeNode:
    def __init__(self,val=None,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insertIntoBST(self,root,val):
        if not root:
            return TreeNode(val)
        if root.val > val:
            root.left = self.insertIntoBST(root.left,val)
        elif root.val < val: # Ensure no duplicates are inserted
            root.right = self.insertIntoBST(root.right,val)
        return root

# Function to print BST in-order (for verification)
def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.val, end=" ")
    inorder(root.right)

# Creating the initial BST
root = TreeNode(50)
root.left = TreeNode(30)
root.right = TreeNode(70)
root.left.left = TreeNode(20)
root.left.right = TreeNode(40)
root.right.left = TreeNode(60)
root.right.right = TreeNode(80)

# Solution object
sol = Solution()

# Inserting 25 into BST
root = sol.insertIntoBST(root, 25)

# Printing in-order traversal (should be sorted)
inorder(root)  # Expected Output: 20 25 30 40 50 60 70 80
