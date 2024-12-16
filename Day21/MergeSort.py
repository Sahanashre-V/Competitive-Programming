def mergeSort(head):
    if not head or not head.next:
        return head  

    mid = getMiddle(head)
    left = head
    right = mid.next
    mid.next = None  

    left = mergeSort(left)
    right = mergeSort(right)

    return merge(left, right)

def getMiddle(head):
    slow, fast = head, head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def merge(left, right):
    dummy = ListNode(0)
    tail = dummy

    while left and right:
        if left.val < right.val:
            tail.next = left
            left = left.next
        else:
            tail.next = right
            right = right.next
        tail = tail.next

    tail.next = left if left else right

    return dummy.next
