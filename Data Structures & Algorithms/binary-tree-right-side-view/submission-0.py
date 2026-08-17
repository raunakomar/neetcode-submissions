# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        q = deque()
        if(root is None):
            return ans
        q.append(root)
        q.append(None)
        temp = []
        while(len(q)>0 ):
            d = q.popleft()
            if(d is None):
                ans.append(temp[-1])
                temp = []
                if(len(q)!=0):
                    q.append(None)
            else:
                temp.append(d.val)
                if(d.left):
                    q.append(d.left)
                if(d.right):
                    q.append(d.right)
        return ans
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        return self.levelOrder(root)