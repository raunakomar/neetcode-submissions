# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def getTree(self, preorder, preStart, inStart, inEnd, m):
        # No elements in this subtree
        if inStart > inEnd:
            return None

        # First element in preorder is the root
        rootVal = preorder[preStart]
        root = TreeNode(rootVal)

        # Find root's position in inorder
        index = m[rootVal]

        # Number of nodes in left subtree
        leftSize = index - inStart

        # Build left subtree
        root.left = self.getTree(
            preorder,
            preStart + 1,
            inStart,
            index - 1,
            m
        )

        # Build right subtree
        root.right = self.getTree(
            preorder,
            preStart + leftSize + 1,
            index + 1,
            inEnd,
            m
        )

        return root

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #print("lenght is ",len(preorder))
        m = {}
        for i in range(len(preorder)):
            m[inorder[i]]= i
        
        root = self.getTree(preorder,0,0,len(preorder)-1,m)
        return root
        
        