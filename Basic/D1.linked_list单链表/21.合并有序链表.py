"""
https://leetcode.cn/problems/merge-two-sorted-lists/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
"""


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




s1 = ListNode(4, None)
s2 = ListNode(2, s1)
s3 = ListNode(1, s2)

s4 = ListNode(4, None)
s5 = ListNode(3, s4)
s6 = ListNode(1, s5)


### if changed the original list node

A = s3
B = s6

A = s6
B = s3

smaller, bigger = (
                    (B, None) if A == None else
                    (A, None) if B == None else
                    (A, B)   if B != None and A.val <= B.val 
                    else (B, A)
)

start = smaller
while bigger != None and smaller != None:
    bigger, smaller.next = (
            (None, bigger)          if smaller.next == None else
            (None, smaller.next)    if bigger == None else
            (bigger, smaller.next) if (
                smaller.next.val <= bigger.val or smaller.next == None
                )
            else (smaller.next, bigger)
        )

    smaller = smaller.next 

print(str(start))


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode],
                      list2: Optional[ListNode]) -> Optional[ListNode]:
        

        A = list1
        B = list2

        smaller, bigger = (
                            (B, None) if A == None else
                            (A, None) if B == None else
                            (A, B)   if B != None and A.val <= B.val 
                            else (B, A)
        )

        start = smaller
        while bigger != None and smaller!= None:
            bigger, smaller.next = (
                (None, bigger)          if smaller.next == None else
                (None, smaller.next)    if bigger == None else
                (bigger, smaller.next) if (
                    smaller.next.val <= bigger.val or smaller.next == None
                    )
                else (smaller.next, bigger)
            )
            smaller = samlelr.next

        return start








