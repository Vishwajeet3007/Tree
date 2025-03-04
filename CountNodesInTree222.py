class NodeTree:
    def __init__(self,val=None,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
def countNodes(root):
    if root is None:
        return 0
    left_count = countNodes(root.left)
    right_count = countNodes(root.right)
    return left_count + right_count + 1
# Creating a simple tree
root = NodeTree(1)
root.left = NodeTree(2)
root.right = NodeTree(3)
root.left.left = NodeTree(4)
root.left.right = NodeTree(5)


root.right.left = NodeTree(6)

print(countNodes(root))  # Output: 5
