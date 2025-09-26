# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        
        if not root.left and not root.right:
            return root

        frontiers = []
        frontiers.append(root)

        while len(frontiers) != 0:
            
            cur = frontiers.pop(0) # pop front to be a queue (BFS)

            if cur.left and cur.right: # fuck it im doing this the dirty way
                # swap
                temp = cur.left
                cur.left = cur.right
                cur.right = temp
                frontiers.append(cur.left)
                frontiers.append(cur.right)

            elif cur.left: # right becomes left, left becomes none
                cur.right = cur.left
                cur.left = None
                frontiers.append(cur.right)

            elif cur.right: # left becomes right, right becomes none
                cur.left = cur.right
                cur.right = None
                frontiers.append(cur.left)
        
        return root