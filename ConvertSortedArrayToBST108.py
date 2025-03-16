class TreeNode:
    def __init__(self,val=None,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self,nums):
        return self.helper(nums,0,len(nums)-1)
    
    def helper(self,nums,start,end):
        if start > end:
            return None
        mid = (start + end) // 2
        root = TreeNode(nums[mid])
        root.left = self.helper(nums,start,mid-1)
        root.right = self.helper(nums,mid + 1,end)
        return root
nums = [-10, -3, 0, 5, 9]
sol = Solution()
root = sol.sortedArrayToBST(nums)

def inorder_traversal(root):
    if not root:
        return []
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)

print(inorder_traversal(root))
