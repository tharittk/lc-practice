class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> acc = new ArrayList<>();
        for (int i = 0; i < candidates.length; i++){
                List<Integer> unfinished = new ArrayList<Integer>();
                dfs(candidates, i, target, i, unfinished, acc);
          }

        return acc;
    }
    private void dfs (int[] candidates, int beg, int target, int i, List<Integer> unfinished, List<List<Integer>> acc){
            int remain = target - candidates[i];
            unfinished.add (candidates[i]);
            if (remain == 0) acc.add(unfinished);
            else if (remain > 0){
                for (int j = beg; j < candidates.length; j++){
                    dfs(candidates, j, remain, j, new ArrayList<Integer>(unfinished), acc);
                }
            }
    }
}