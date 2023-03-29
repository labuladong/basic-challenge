
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



s5 = ListNode(5,None)
s4 = ListNode(4,s5)
s3 = ListNode(3,s4)
s2 = ListNode(2,s3)
s1 = ListNode(1,s2)

s1


def reverse_node(old_head):

    if old_head.next == None or old_head == None:
        return old_head
    else:
        pass
        # return old_head.next
    
    last_node = reverse_node(old_head.next)
    old_head.next.next = old_head
    old_head.next = None
    
    return last_node



reverse_node(s1)






------------- 2023-02-19 ----------------

def reverseList(old_head):
    if old_head == None:
        return None
    elif old_head.next == None:
        return old_head

    
    new_tail = old_head.next
    new_head = reverseList(old_head.next)

    old_head.next = None

    new_tail.next = old_head
    
    return new_head



s5 = ListNode(5,None)
s4 = ListNode(4,s5)



reverseList(s4)









