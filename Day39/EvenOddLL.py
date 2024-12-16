class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def printEvenOddLL(head):
    current = head
    even_flag = True  
    
    while current:
        if even_flag and current.value % 2 == 0:  
            print(current.value, end=" ")
            even_flag = False  
        elif not even_flag and current.value % 2 != 0: 
            print(current.value, end=" ")
            even_flag = True  
        current = current.next

def createLinkedList(arr):
    head = ListNode(arr[0])
    current = head
    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

arr = [2, 5, 4, 7, 8, 3, 10]
head = createLinkedList(arr)
printEvenOddLL(head)  
