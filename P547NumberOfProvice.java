class Solution {
    public int findCircleNum(int[][] isConnected) {
        int n = isConnected.length;
        boolean[] marked = new boolean[n];
        int count = 0;
        for (int i = 0; i < n; i++){
            marked[i] = false;
        }

        for (int i = 0; i < n; i++){
            if (!marked[i]){
                dfs (i, isConnected, marked);
                count++;
            }
        }
        return count;
    }


    private void dfs (int v, int[][] isConnected, boolean[] marked){
        marked[v] = true;
        for (int j = 0; j < isConnected.length; j++){
            if ((isConnected[v][j]==1) && !marked[j]){
                dfs (j, isConnected, marked);
            }
        }
    }
}