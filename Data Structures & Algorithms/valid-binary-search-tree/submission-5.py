# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def check(self,n:Optional[TreeNode],mn:int,mx:int)->bool:
        if(n is None):
            return True
        if(n.val<=mn or n.val>=mx):
            return False
        return (self.check(n.left,mn,n.val) and self.check(n.right,n.val,mx))
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.check(root,float('-inf'),float('inf'))