/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    private List<Integer> lst;

    public List<Integer> rightSideView(TreeNode root) {
        this.lst = new ArrayList<Integer>();
        Queue<TreeNode> q = new LinkedList<TreeNode>();
        Queue<TreeNode> nextQ = new LinkedList<TreeNode>();
        if (root == null) return this.lst;
        q.add(root);

        while (!q.isEmpty() || !nextQ.isEmpty()){
            boolean hasVal1 = false;
            int val1=Integer.MAX_VALUE;
            while(!q.isEmpty()){
                TreeNode curr = q.poll();
                if(curr.left != null) nextQ.add(curr.left);
                if(curr.right!= null) nextQ.add(curr.right);

                hasVal1 = true;
                val1 = curr.val;
            }
            if (hasVal1) this.lst.add(val1);

            boolean hasVal2 = false;
            int val2=Integer.MAX_VALUE;
            while(!nextQ.isEmpty()){
                TreeNode curr = nextQ.poll();
                if(curr.left != null) q.add(curr.left);
                if(curr.right!= null) q.add(curr.right);

                hasVal2 = true;
                val2 = curr.val;
            }
            if (hasVal2) this.lst.add(val2);
        }

        return this.lst;
    }
}