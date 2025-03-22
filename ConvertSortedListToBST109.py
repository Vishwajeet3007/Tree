class TreeNode:
    def __init__(self,val = None , left = None , right = None):
        self.val = val
        self.left = left
        self.right = right
class ListNode:
    def __init__(self,val=None,next=None):
        self.val = val
        self.next = next
class Solution:
    def middle(self,head):
        if head is None:
            return None
        fast = head
        slow = head
        prev = slow
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None
        return slow
    def sortedListToBST(self,head):
        if head is None:
            return None
        if head.next is None:
            root = TreeNode(head.val)
            return root
        mid = self.middle(head)
        root = TreeNode(mid.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(mid.next)
        return root
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head
head = create_linked_list([-10, -3, 0, 5, 9])
solution = Solution()
root = solution.sortedListToBST(head)
def pre_order_traversal(root):
    if not root:
        return []
    return [root.val] + pre_order_traversal(root.left) + pre_order_traversal(root.right)

print(pre_order_traversal(root))
