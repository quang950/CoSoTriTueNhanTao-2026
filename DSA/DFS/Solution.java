package DSA.DFS;

public class Solution {
    private boolean nonZero(TreeNode root){
        return dfs(root);
    }   
    //base case and method
    private boolean dfs(TreeNode node){
        if (node == null) return false;
        if (node.val == 0) return false;
        if (node.left == null & node.right == null) return true;

        return dfs(node.left ) || dfs(node.right) ;
    }

}
