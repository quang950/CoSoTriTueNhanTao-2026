package DSA.DFS;

import java.util.ArrayList;
import java.util.List;

public class BackTracking {
    public List<List<Integer>> allNonZeroPath(TreeNode node) {
        List<List<Integer>> result = new ArrayList<>();
        dfs(node, new ArrayList<>(), result);
        return result;
    }

    public void dfs(TreeNode node, List<Integer> path, List<List<Integer>> result) {
        // base case
        if (node == null)
            return;
        if (node.val == 0)
            return;

        path.add(node.val); // choose

        if (node.left == null && node.right == null) {
            result.add(new ArrayList<>(path));
        } else {
            dfs(node.left, path, result);
            dfs(node.right, path, result);
        }
        path.remove(path.size() - 1);
    }
}
