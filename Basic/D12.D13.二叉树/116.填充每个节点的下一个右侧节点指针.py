"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':

        if root == None or root.left == None:
            return root
        
        root.left.next = root.right
        if root.left.right != None:
            root.left.right.next = root.right.left
        self.connect(root.left)
        self.connect(root.right)
        return root

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':

        if root == None or root.left == None:
            return root
        
        root.left.next = root.right
        if root.next != None:
            root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)
        return root







