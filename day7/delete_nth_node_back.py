# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        temp = ListNode(0,head)
        fast = temp
        slow = temp
        if not head:
            return head
        n=n+1
        while n:
            fast = fast.next
            n-=1
        if fast == None:
            head = head.next
            return head
        while fast:
            fast = fast.next 
            slow = slow.next
        slow.next = slow.next.next
        return temp.next