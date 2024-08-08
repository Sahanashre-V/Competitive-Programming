# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True

        #Middle of the linked list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #Reverse the second half of the linked list
        prev, curr = None, slow
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp

        #Compare the first and the reversed second half
        first_half, second_half = head, prev
        while second_half:
            if first_half.val != second_half.val: 
                return False
            first_half = first_half.next
            second_half = second_half.next

        return True
