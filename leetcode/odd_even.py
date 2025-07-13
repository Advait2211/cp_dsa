# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        cur = fut = head

        while cur:
            if cur.val % 2 == 0:
                while fut:
                    if fut.val % 2 == 1:
                        break
                    fut = fut.next
                else:
                    return head
                
                fut.val, cur.val = cur.val, fut.val

            cur = cur.next
            fut = fut.next

        return head





            
