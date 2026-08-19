# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')

        def maxSum(root:Optional[TreeNode])->int:
            if(root is None):
                return 0
            left_max = maxSum(root.left)
            right_max = maxSum(root.right)
            left_max = max(0,left_max)
            right_max = max(0,right_max)
            self.max_sum = max(self.max_sum,root.val+left_max+right_max)
            return max(root.val+left_max,root.val+right_max)
        maxSum(root)
        return self.max_sum