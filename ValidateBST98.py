class TreeNode:
    def  __init__(self,val=None,left=None,right=None):
        self.val = val
        self.left = left
        self.right =right

class Solution:
    def isValidBST(self,root):
        if not root:
            return True
        stack = []
        prev = None
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if prev is not None and root.val <= prev:
                return False
            prev = root.val
            root= root.right
        return True
    
sol = Solution()

# Valid BST
root1 = TreeNode(2)
root1.left = TreeNode(1)
root1.right = TreeNode(3)

print(sol.isValidBST(root1))  # Output: True

# Invalid BST
root2 = TreeNode(5)
root2.left = TreeNode(1)
root2.right = TreeNode(4)
root2.right.left = TreeNode(3)
root2.right.right = TreeNode(6)

print(sol.isValidBST(root2))  # Output: False
