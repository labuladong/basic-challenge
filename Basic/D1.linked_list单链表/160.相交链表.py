# Definition for singly-linked list.
# 2023-03-02
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


s6 = ListNode(5, None)
s5 = ListNode(4, s6)
s4 = ListNode(8, s5)
s3 = ListNode(1, s4)
s2 = ListNode(4, s3)

h3 = ListNode(1, s4)
h2 = ListNode(6, h3)
h1 = ListNode(5, h2)


headA = s2
headB = h1

startA = headA
startB = headB

waiting_cnt = 0
longer_start = None
shorter_start = None
both_end = False

while both_end == False:
    print(headA, headB)
    if headA == None and headB != None:
        waiting_cnt += 1
        if longer_start == None:
            longer_start = startB
            shorter_start = startA
            
        headB = headB.next

    elif headB == None and headA != None:
        waiting_cnt += 1
        if longer_start == None:
            longer_start = startA
            shorter_start = startB
        headA = headA.next

    elif headB == None and headA == None:
        both_end = True

    elif headB != None and headA != None:
        headA = headA.next
        headB = headB.next

## if two list have same length
if longer_start == None:
    longer_start = startA
    shorter_start = startB

if longer_start != None:
    for i in range(waiting_cnt):
        longer_start = longer_start.next

joint_node = None
while longer_start != None and shorter_start != None:
    if longer_start == shorter_start:
        joint_node = longer_start
        break

    longer_start = longer_start.next
    shorter_start = shorter_start.next




# return joint_node
print(joint_node)





