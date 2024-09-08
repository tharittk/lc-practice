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
    public int maxLevelSum(TreeNode root) {
        Queue<TreeNode> q = new LinkedList<TreeNode>();
        Queue<TreeNode> qnext = new LinkedList<TreeNode>();
        if (root == null) return 0;
        q.add(root);
        int sum = root.val;
        int maxSum = sum;
        int level = 1;
        int maxLevel = 1;

        while(!q.isEmpty() || !qnext.isEmpty()){
            sum = calSumAndAddQ (q, qnext);

            if (sum > maxSum){
                maxLevel = level;
                maxSum = sum;
            }
            level++;

            Queue<TreeNode> tmp = q;
            q = qnext;
            qnext = tmp;
        }
        return maxLevel;
    }

    private void addChildToQueue (TreeNode root, Queue<TreeNode> q){
        if (root.right != null) q.add(root.right);
        if (root.left != null) q.add(root.left);
    }

    private int calSumAndAddQ (Queue<TreeNode> q, Queue<TreeNode> qnext){
        int sum = 0;
        while (!q.isEmpty()){
            TreeNode curr = q.remove();
            addChildToQueue(curr, qnext);
            sum += curr.val;
        }
        return sum;
    }
}
