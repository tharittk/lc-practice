class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def isGood(node, maxInPath):
            if node==None:
                return 0
            if node.val >= maxInPath:
                maxInPath = node.val
                return 1 + isGood(node.left, maxInPath) + isGood(node.right, maxInPath)
            else:
                return isGood(node.left, maxInPath) + isGood(node.right, maxInPath)
        if root == None:
            return 0
        maxInPath = root.val
        return isGood(root, maxInPath)