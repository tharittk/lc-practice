# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.min_cache = {None:float("inf")}
        self.max_cache = {None:-float("inf")}

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def build_min_subtree(self, root):
            if (not root.left) and (not root.right):
                self.min_cache[root] = root.val
            else:
                if root.left and root.left not in self.min_cache.keys():
                    build_min_subtree(self, root.left)
                if root.right and root.right not in self.min_cache.keys():
                    build_min_subtree(self, root.right)

                self.min_cache[root] = min(root.val, min(self.min_cache[root.left], self.min_cache[root.right]))

        def build_max_subtree(self, root):
            if (not root.left) and (not root.right):
                self.max_cache[root] = root.val
            else:
                if root.left and root.left not in self.max_cache.keys():
                        build_max_subtree(self, root.left)

                if root.right and root.right not in self.max_cache.keys():
                        build_max_subtree(self, root.right)
                        
                self.max_cache[root] = max(root.val, max(self.max_cache[root.left], self.max_cache[root.right]))
        
        def validate(self, root):
            if not root:
                return True
            if root.left:
                lc_ok = root.val > self.max_cache[root.left]
            else:
                lc_ok = True
            if root.right:
                rc_ok = root.val < self.min_cache[root.right]
            else:
                rc_ok = True

            if rc_ok and lc_ok:
                return validate(self, root.left) and validate(self, root.right)
            else:
                return False
        
        build_max_subtree(self, root)
        build_min_subtree(self, root)
        return validate(self, root)
