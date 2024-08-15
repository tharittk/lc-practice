class Solution {
    public int nearestExit(char[][] maze, int[] entrance) {

        int m = maze.length;
        int n = maze[0].length;
        boolean[][] visited = new boolean[m][n];

        // bfs
        Queue<Integer> qr = new LinkedList<>();
        Queue<Integer> qc = new LinkedList<>();
        Queue<Integer> steps = new LinkedList<>();

        int r0 = entrance[0];
        int c0 = entrance[1];
        
        int rt = r0;
        int ct = c0;
        int step = 0;
        int finalStep=0;
        boolean done = false;
        visited[rt][ct] = true;
        qr.add(rt);
        qc.add(ct);
        steps.add(step);

        while (!qr.isEmpty()){
            rt = qr.remove();
            ct = qc.remove();
            finalStep = steps.remove();
            visited[rt][ct] = true;
            done = isDone (rt, ct, r0, c0, m, n);
            if (done){
                break;
            }
            step = finalStep+1;

            if (isValidPoint (rt-1, ct, visited, maze, m, n)){
                qr.add(rt-1);
                qc.add(ct);
                steps.add(step);
                visited[rt-1][ct] = true;

            }
            if (isValidPoint (rt+1, ct, visited, maze, m , n)){
                qr.add(rt+1);
                qc.add(ct);
                steps.add(step);
                visited[rt+1][ct] = true;

            }
            if (isValidPoint (rt, ct-1, visited, maze, m, n)){
                qr.add(rt);
                qc.add(ct-1);
                steps.add(step);
                visited[rt][ct-1] = true;
            }
            if (isValidPoint (rt, ct+1, visited, maze, m, n)){
                qr.add(rt);
                qc.add(ct+1);
                steps.add(step);
                visited[rt][ct+1] = true;
            }
        }
        if (done){
            return finalStep;
        }
        else {
            return -1;
        }
    }

    private boolean isValidPoint (int row, int col, boolean[][] visited, char[][] maze, int m, int n){

        if (row >= 0 && row < m && col >= 0 && col < n){
            if (!visited[row][col] && (maze[row][col] == '.')){
                return true;
            } else {
                return false;
            }
        } else{
            return false;
        }
    }

    private boolean isDone (int row, int col, int r0, int c0, int m, int n){
        if (row==0 || row == (m-1) || col == 0 || col == (n-1)){
            if (row != r0 || col != c0){
                return true;
            }
            else {
                return false;
            }
        } else {
            return false;
        }
    }


}