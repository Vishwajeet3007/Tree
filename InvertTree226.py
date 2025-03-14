class TreeNode:
    def __init__(self,val=None,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self,root):
        if not root:
            return root
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left = right
        root.right = left 
        return root

def print_tree(root):
    """Helper function to print the tree in level-order (BFS)"""
    if not root:
        return
    queue = [root]
    while queue:
        node = queue.pop(0)
        print(node.val, end=" ")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

# Constructing a sample binary tree
#         4
#       /   \
#      2     7
#     / \   / \
#    1   3 6   9

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

print("Original Tree (Level-Order):")
print_tree(root)

# Inverting the tree
sol = Solution()
root = sol.invertTree(root)

print("\nInverted Tree (Level-Order):")
print_tree(root)