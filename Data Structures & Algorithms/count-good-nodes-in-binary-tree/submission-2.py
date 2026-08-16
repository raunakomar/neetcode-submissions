# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def __init__(self):
        self.goodNode = 0
    def checkGoodNode(self,n:TreeNode,m:int)->None:
        maxNode = m
        if(n):
            #print("max is ",maxNode , "n value",n.val)
            if(n.val>=m):
                #print("found max")
                self.goodNode += 1
                maxNode = n.val
            self.checkGoodNode(n.left,maxNode)
            self.checkGoodNode(n.right,maxNode)
        else:
            return
    def goodNodes(self, root: TreeNode) -> int:
        if(root is None):
            return 0
        self.checkGoodNode(root,root.val)
        return self.goodNode