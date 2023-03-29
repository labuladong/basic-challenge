
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




pointer_list = []

