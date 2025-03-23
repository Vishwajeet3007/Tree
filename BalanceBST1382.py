class TreeNode:
    def __init__(self,val=None,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorder(self,root,lst):
        if not root:
            return
        self.inorder(root.left,lst)
        lst.append(root.val)
        self.inorder(root.right,lst)


    def balanceBST(self,root):
        lst = []
        self.inorder(root,lst)
        return self.BSTMakers(lst,0,len(lst)-1)
    def BSTMakers(self,lst,start,end):
        if start > end:
            return None
        mid = (start + end) // 2
        root = TreeNode(lst[mid])
        root.left = self.BSTMakers(lst,start,mid-1)
        root.right = self.BSTMakers(lst,mid + 1,end)
        return root
# Creating an unbalanced BST
root = TreeNode(10)
root.right = TreeNode(20)
root.right.right = TreeNode(30)
root.right.right.right = TreeNode(40)

# Running balanceBST function
sol = Solution()
balanced_root = sol.balanceBST(root)

# Helper function to print inorder traversal of the balanced BST
def inorder_traversal(root):
    if not root:
        return []
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)

# Printing the inorder traversal of balanced BST
print("Inorder of Balanced BST:", inorder_traversal(balanced_root))
