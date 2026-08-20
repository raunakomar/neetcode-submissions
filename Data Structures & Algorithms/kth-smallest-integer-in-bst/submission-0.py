# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.ar = []
    def inorder(self,root:Optional[TreeNode])->None:
        if(root is None):
            return
        self.inorder(root.left)
        self.ar.append(root.val)
        self.inorder(root.right)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.inorder(root)
        for i in range(len(self.ar)):
            print(self.ar[i])
        return self.ar[k-1]
