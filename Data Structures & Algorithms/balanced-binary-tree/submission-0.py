# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getDepth(self,root:Optional[TreeNode])->bool:
        if(root is None):
            return 0
        l = self.getDepth(root.left)
        r = self.getDepth(root.right)
        return (max(l,r)+1)
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if(root is None):
            return True
        left = self.getDepth(root.left)
        print("left hight of ",root.val,left)
        right = self.getDepth(root.right)
        print("right hight of ",root.val,right)
        isLB = self.isBalanced(root.left)
        print("is left balanced for ",root.val,isLB)
        isRB = self.isBalanced(root.right)
        print("is right balanced for ",root.val,isRB)
        return(abs(left-right)<=1 and isLB and isRB)