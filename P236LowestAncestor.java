/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        ArrayList<TreeNode> pathp = new ArrayList<TreeNode>();
        ArrayList<TreeNode> pathq = new ArrayList<TreeNode>();

        TreeNode dump = dfs(root, p, pathp);
        TreeNode dumq = dfs(root, q, pathq);

        // for (TreeNode tp : pathp) System.out.println(tp.val);
        // for (TreeNode tq : pathq) System.out.println(tq.val);

        int dp = pathp.size();
        int dq = pathq.size();
        
        int i = 0;
        int j = 0;
        if (dp > dq){
            i = dp-dq;
            if (pathp.get(i) == q) return q;
        } else if(dq > dp){
            j = dq-dp;
            if (pathq.get(j) == p) return p;
        }

        while (pathp.get(i) != pathq.get(j)){
            // System.out.println("i: " + i);
            // System.out.println("j: "+ j);
            i++;
            j++;
        }

        return pathp.get(i);
    }
    private TreeNode dfs (TreeNode root, TreeNode target, ArrayList<TreeNode> path){
        if (root == null) return null;
        if (root == target){
            path.add(root);
            return root;
        } else {
            TreeNode r = dfs(root.right, target, path);
            TreeNode l = dfs(root.left, target, path);
            if (r != null || l != null){
                path.add(root);
                return root;
            } else return null;
        }
    }
}

class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if (root == NULL)
            return NULL;
        if (root == p)
            return p;
        if (root == q)
            return q;
        TreeNode* leftAns = lowestCommonAncestor(root->left, p, q);
        TreeNode* rightAns = lowestCommonAncestor(root->right, p, q);
        if (leftAns != NULL && rightAns == NULL)
            return leftAns;
        if (leftAns == NULL && rightAns != NULL)
            return rightAns;
        if (leftAns != NULL && rightAns != NULL)
            return root;
        return NULL;
    }
};
