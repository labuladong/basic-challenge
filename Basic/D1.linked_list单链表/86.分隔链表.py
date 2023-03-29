
## 二月份答题记录
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        normal_list = [str(self.val)]
        while self.next != None:
            normal_list.append(str(self.next.val))
            self = self.next
        return "->".join(normal_list)


# class Solution:
#     def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
#         pass

s1 = ListNode(2, None)
s2 = ListNode(5, s1)
s3 = ListNode(2, s2)
s4 = ListNode(3, s3)
s5 = ListNode(4, s4)
s6 = ListNode(1, s5)

head = ListNode(1, None)
start = head
x = 3



smaller = ListNode(-1, next=None)
bigger = ListNode(-1, next=None)

smaller_head = smaller
bigger_head = bigger

while head:
    if head.val < x:
        smaller.next = ListNode(head.val, next=None)
        smaller = smaller.next
    else:
        bigger.next = ListNode(head.val, next=None)
        bigger = bigger.next
    head = head.next


smaller_head = smaller_head.next
bigger_head = bigger_head.next


smaller_head
bigger_head

# if smaller_head == None:
#     return bigger_head
# elif bigger_head == None:
#     return samller_head
# else:
#     smaller.next = bigger_head
#     return smaller_head
#
#









