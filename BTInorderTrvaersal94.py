class TreeNode:
    def __init__(self,val = None,left = None,right=None):
        self.val = val
        self.right= right
        self.left = left
class Solution:
    def InorderTraversal(self,root):
        result = []
        def traverse(root):
            if not root:
                return
            traverse(root.left)
            result.append(root.val)
            traverse(root.right)
        traverse(root)
        return result
root = TreeNode(1)
root.left =TreeNode(2)
root.right = TreeNode(3)
root.left.left=TreeNode(4)
root.right.right=TreeNode(5)
solution =  Solution()
result = solution.InorderTraversal(root)
print(result)