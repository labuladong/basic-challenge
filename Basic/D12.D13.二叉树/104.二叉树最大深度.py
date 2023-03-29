# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

  #   3
  #  / \
  # 9  20
  #   /  \
  #  15   7
  #
tree1 = TreeNode(val = 15)
tree2 = TreeNode(val = 7)
tree3 = TreeNode(val = 20, left = tree1, right=tree2)
tree4 = TreeNode(val = 9)
tree5 = TreeNode(val = 3, left = tree4,right = tree3)


def getDepth(treeHead):
    if treeHead == None:
        return 0
    else :
        subdepth = max(getDepth(treeHead.left), getDepth(treeHead.right))
        return 1 + subdepth


getDepth(tree5)










