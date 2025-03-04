class TreeNode:
    def __init__(self,val = None,left = None , right = None):
        self.val = val
        self.left = left
        self.right = right
def isUniValTree(root):
    if not root:
        return True
    def dfs(node):
        if not node:
            return True
        if node.val != root.val:
            return False
        return dfs(node.left) and dfs(node.right)
    return dfs(root)
def buildTree(values):
    if not values:
        return None

    nodes = [TreeNode(val) if val is not None else None for val in values]
    
    for i in range(len(values)):
        if nodes[i] is not None:
            left_idx = 2 * i + 1
            right_idx = 2 * i + 2
            if left_idx < len(values):
                nodes[i].left = nodes[left_idx]
            if right_idx < len(values):
                nodes[i].right = nodes[right_idx]
    
    return nodes[0]  # Root node
# Construct the tree from the given list
root = buildTree([1, 1, 2, 1, 1, None, 1])

# Test the function
print(isUniValTree(root))  # Output: True