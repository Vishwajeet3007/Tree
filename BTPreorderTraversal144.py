class TreeNode:
    def __init__(self,val=None,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preOrderTraversal(self,root):
        result = []
        def traverse(root):
            if root is None:
                return
            result.append(root.val)
            traverse(root.left)
            traverse(root.right)
        traverse(root)
        return result
root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.left.left =TreeNode(4)
root.left.right =TreeNode(5) 

solution = Solution()
result= solution.preOrderTraversal(root)
print(result)
