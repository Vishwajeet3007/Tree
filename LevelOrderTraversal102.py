from collections import deque
class TreeNode:
    def __init__(self,val=None,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrderTraversal(self,root):
        if root is None:
            return []
        ans = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            curr_level = []

            for _ in range(level_size):
                curr_Node = queue.popleft()
                curr_level.append(curr_Node.val)

                if curr_Node.left:
                    queue.append(curr_Node.left)
                if curr_Node.right:
                    queue.append(curr_Node.right)
            ans.append(curr_level)
        return ans
# Creating a sample binary tree
#         1
#        / \
#       2   3
#      / \   \
#     4   5   6
#             /
#            7

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)
root.right.right.left = TreeNode(7)

solution = Solution()
print(solution.levelOrderTraversal(root))
