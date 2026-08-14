# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.max_d = 0
    def maxDepth(self,root:Optional[TreeNode])->int:
        if(root is None):
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        self.max_d = max(self.max_d,left+right)
        height = max(left,right)+1
        return height
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if(root is None):
            return 0
        self.maxDepth(root)
        return self.max_d