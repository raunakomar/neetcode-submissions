# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def find(self,root:Optional[TreeNode],val:int)->Optional[TreeNode]:
        if(root is None):
            return None
        if(root.val==val):
            return root
        left = self.find(root.left,val)
        if(left is None):
            right = self.find(root.right,val)
        else:
            return left
        if(right is None):
            return None
        else:
            return right 
    def isSame(self,root:Optional[TreeNode],sub:Optional[TreeNode])->bool:
        if(root is None and sub is not None):
            #print("25")
            return False
        if(root is not None and sub is None):
            #print("27")
            return False
        if(root is None and sub is None):
            #print("31")
            return True
        if(root.val != sub.val):
            #print("34")
            return False
        if(root.val == sub.val):
            #print("37")
            return (self.isSame(root.left,sub.left) and self.isSame(root.right,sub.right))
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if(root is None and subRoot is not None):
            return False
        if(root is not None and subRoot is None):
            return False
        if(self.isSame(root,subRoot)==False):
            if(self.isSubtree(root.left,subRoot)==False):
                if(self.isSubtree(root.right,subRoot)==False):
                    return False
                else:
                    return True
            else:
                return True
        else:
            return True

        