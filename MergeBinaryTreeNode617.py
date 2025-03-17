class TreeNode:
    def __init__(self,val = None,left = None,right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def mergeTreeNodes(self,root1,root2):
        if not root1 and not root2:
            return None
        elif not root1:
            return root2
        elif not root2:
            return root1
        root = TreeNode(root1.val + root2.val)
        root.left = self.mergeTreeNodes(root1.left,root2.left)
        root.right = self.mergeTreeNodes(root1.right,root2.right)
        return root
    
# Tree 1
root1 = TreeNode(1)
root1.left = TreeNode(3)
root1.right = TreeNode(2)
root1.left.left = TreeNode(5)

# Tree 2
root2 = TreeNode(2)
root2.left = TreeNode(1)
root2.right = TreeNode(3)
root2.left.right = TreeNode(4)
root2.right.right = TreeNode(7)

# Merging Trees
sol = Solution()
merged_root = sol.mergeTreeNodes(root1, root2)

# Function to print tree in-order
def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.val, end=" ")
    inorder(root.right)

# Output merged tree
inorder(merged_root)

