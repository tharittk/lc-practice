# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: int
        """
        def pathSumNoMem (root, targetSum):
            if root == None:
                return 0

            lsub_incl = pathSumNoMem (root.left, targetSum - root.val)
            rsub_incl = pathSumNoMem (root.right, targetSum - root.val)
            total = lsub_incl + rsub_incl

            if root.val == targetSum:
                return total + 1
            else:
                return total

        def pathSumMem(root, targetSum, origSum):
            if root == None:
                return 0

            lsub = pathSumMem (root.left, origSum, origSum)
            rsub = pathSumMem (root. right, origSum, origSum)
            # if you use pathSum, this will repeatedly call lsub, rsub, with exact same arguments so end up double counting
            lsub_incl = pathSumNoMem (root.left, targetSum - root.val)
            rsub_incl = pathSumNoMem (root.right, targetSum - root.val)

            total = lsub + rsub + lsub_incl + rsub_incl

            if root.val == targetSum:
                return total + 1
            else:
                return total
        return pathSumMem(root, targetSum, targetSum)
