class TreeNode:
    def __init__(self,val = None,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def helper(self,root1,root2):
        if root1 == None or root2 == None:
            return root1 == root2
        if root1.val == root2.val:
            ans1 = self.helper(root1.left,root2.right)
            ans2 = self.helper(root1.right,root2.left)
            return ans1 and ans2
        else:
            return False

    def isSymmetricTree(self,root):
        if root == None:
            return True
        return self.helper(root.left,root.right) 
# Helper function to build a tree
def build_tree():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)
    return root

sol = Solution()
root = build_tree()
print(sol.isSymmetricTree(root))  # Output: True
