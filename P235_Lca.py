# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr_p = root
        curr_q = root
        prev = root
        while (True):

            if curr_p.val != p.val:
                if curr_p.val > p.val:
                    curr_p = curr_p.left
                else:
                    curr_p = curr_p.right

            if curr_q.val != q.val:
                if curr_q.val > q.val:
                    curr_q = curr_q.left
                else:
                    curr_q = curr_q.right
            
            if curr_q != curr_p:
                return prev
            else:
                prev = curr_p

            # print("curr_p ", curr_p.val)
            # print("curr_q", curr_q.val)
            # print("====")
