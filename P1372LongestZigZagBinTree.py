# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestZigZag(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxlen = 0

        def _longZigZag(root, prev_is_right, acc):

            if root.right == None and root.left == None:
                return acc
            _longZigZag

            if prev_is_right:
                if root.left:
                    maxleft = _longZigZag(root.left, False, acc + 1)
                else:
                    maxleft = acc
                if root.right:
                    maxright =_longZigZag(root.right, True, 1)
                else:
                    maxright = 0

            else:
                if root.right:
                    maxright = _longZigZag(root.right, True, acc + 1)
                else:
                    maxright = acc
                if root.left:
                    maxleft = _longZigZag(root.left, False, 1)
                else:
                    maxleft = 0
            
            maxlen = max(maxleft, maxright)
            return maxlen

        if root.right == None:
            maxright = 0
        else:
            maxright = _longZigZag(root.right, True, 1)
        if root.left == None:
            maxleft = 0
        else:
            maxleft =  _longZigZag(root.left, False, 1)

        return max(maxright, maxleft)

        
