class TreeNode:
    def __init__(self,val=None,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def LCAofBST(self,root,p,q):
        if not root:
            return None
        temp = root
        while temp:
            if temp.val > p.val and temp.val > q.val:
                temp = temp.left
            elif temp.val < p.val and temp.val < q.val:
                temp = temp.right
        return temp
    