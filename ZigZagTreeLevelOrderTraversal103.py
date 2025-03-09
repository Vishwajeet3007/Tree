class TreeNode:
    def __init__(self,val=None,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def ZigZagLevelOrderTraversal(self,root):
        ans = []
        if not root:
            return ans
        currAns = []
        main = []
        helper = []
        level = 0
        main.append(root)
        while len(main)>0:
            currNode = main.pop()
            currAns.append(currNode.val)
            if level == 0:
                if currNode.left:
                    helper.append(currNode.left)
                if currNode.right:
                    helper.append(currNode.right)
            else:
                if currNode.right:
                    helper.append(currNode.right)
                if currNode.left:
                    helper.append(currNode.left)
            if len(main) == 0:
                ans.append(currAns)
                currAns=[]
                level = 1 - level
                main = helper
                helper = []
        return ans
# Create the tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

# Call the function
sol = Solution()
result = sol.ZigZagLevelOrderTraversal(root)

# Print result
print(result)
