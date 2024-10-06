# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        def processed_two_chlid(to_del):
            lmost = to_del.right
            prev = to_del
            while lmost.left:
                prev = lmost
                lmost = lmost.left
            # no left most at all
            if prev == to_del:
                return lmost
            else:
                if lmost.right:
                    prev.left = lmost.right
                else:
                    prev.left = None
                return lmost

        if not root:
            return root
        curr = root
        prev = None
        go_right = False
        while curr and curr.val != key:
            if curr.val < key:
                prev = curr
                curr = curr.right
                go_right = True
            else:
                prev = curr
                curr = curr.left
                go_right = False
        
        if not curr:
            return root
        else:
            #print("found @", curr.val)
            # delete root 
            if not prev:
                if (not curr.left) and (not curr.right):
                    root = None
                    return root
                elif not curr.left and curr.right:
                    return curr.right
                elif curr.left and not curr.right:
                    return curr.left
                #print("Hit case root")
                lmost = processed_two_chlid(curr)
                #print("lmost ", lmost.val)
                lmost.left = curr.left
                if curr.right != lmost:
                    lmost.right = curr.right
                return lmost
            
            # no chlid
            elif (not curr.left) and (not curr.right):
                #print("Hit case no child")
                if go_right:
                    prev.right = None
                else:
                    prev.left = None
            # only one chlid
            elif not curr.left or not curr.right:
                #print("Hit case one child")
                replace = curr.left if curr.left else curr.right
                if go_right:
                    prev.right = replace
                else:
                    prev.left = replace
            # two chlid
            else:
                #print("Hit case two child")
                lmost = processed_two_chlid(curr)
                if go_right:
                    prev.right = lmost
                else:
                    prev.left = lmost

                lmost.left = curr.left
                if curr.right != lmost:
                    lmost.right = curr.right
            right
            curr = None
            return root


        
