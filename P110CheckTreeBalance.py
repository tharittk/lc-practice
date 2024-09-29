# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def check_balance_and_height(root):
            if (not root.left) and (not root.right):
                return (True, 0)
            if root.left:
                lpair = check_balance_and_height(root.left)
                if not lpair[0]:
                    return (False, 0)
                else:
                    lc = 1 + lpair[1]
            else:
                lc = 0
            if root.right:
                rpair = check_balance_and_height(root.right)
                if not rpair[0]:
                    return (False, 0)
                else:
                    rc = 1 + rpair[1]
            else:
                rc = 0

            return ( abs(lc - rc) <= 1, max(lc, rc))

        if not root:
            return True
        return check_balance_and_height(root)[0]

