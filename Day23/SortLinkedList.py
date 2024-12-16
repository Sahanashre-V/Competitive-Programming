class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def sortList(head):
    if not head or not head.next:
        return head

    def get_middle(node):
        slow, fast = node, node
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge(left, right):
        dummy = ListNode()
        current = dummy

        while left and right:
            if left.val < right.val:
                current.next = left
                left = left.next
            else:
                current.next = right
                right = right.next
            current = current.next

        current.next = left if left else right
        return dummy.next

    middle = get_middle(head)
    right_half = middle.next
    middle.next = None
    left_half = head

    left_sorted = sortList(left_half)
    right_sorted = sortList(right_half)

    return merge(left_sorted, right_sorted)
