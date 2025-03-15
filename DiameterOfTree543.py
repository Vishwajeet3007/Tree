class TreeNode:
    def __init__(self,val = None,left=None,right  = None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.diameter = 0
    def height(self,root):
        if not root:
            return 0
        lh = self.height(root.left)
        rh = self.height(root.right)
        self.diameter = max(lh + rh , self.diameter)
        return max(lh,rh)  + 1
    def diameterOfBT(self,root):
        if not root:
            return 0
        height = self.height(root)
        return self.diameter
# Constructing the following tree:
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

# Creating a Solution object and finding the diameter
sol = Solution()
print(sol.diameterOfBT(root))  # Output: 3
