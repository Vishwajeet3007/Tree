class TreeNode:
    def __init__(self,val = None,left = None,right = None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def binaryTreePaths(self,root):
        ans = []
        if not root:
            return ans
        elif not root.left and not root.right:
            ans.append(str(root.val))
            return ans
        leftAns = self.binaryTreePaths(root.left)
        rightAns = self.binaryTreePaths(root.right)

        for s in leftAns:
            ans.append(str(root.val)+"->"+s)
        for s in rightAns:
            ans.append(str(root.val)+"->"+s)
        return ans

# Creating a sample tree: 
#        1
#       / \  
#      2   3
#     / \  / \
#    4   5 6  7

root = TreeNode(1)
root.left = TreeNode(2)
root.left.right = TreeNode(5)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

sol = Solution()
print(sol.binaryTreePaths(root))
