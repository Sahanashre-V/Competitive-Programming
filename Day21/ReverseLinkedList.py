def reverseListRecursive(head):
    if not head or not head.next:
        return head  

    reversed_head = reverseListRecursive(head.next)
    head.next.next = head  
    head.next = None       

    return reversed_head
