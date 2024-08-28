class Solution {
    public int[] asteroidCollision(int[] asteroids) {
        Stack<Integer> r = new Stack<Integer>();
        Stack<Integer> l = new Stack<Integer>();

        int countFree = 0;
        List<Integer> free = new ArrayList<Integer>();
        // those moving left in the start of the row never collides
        while (countFree < asteroids.length && asteroids[countFree] < 0){
            free.add(asteroids[countFree]);
            countFree++;
        }
        int i = countFree;
        while (i < asteroids.length){
            if (asteroids[i] >= 0) r.push(asteroids[i]);
            else l.push(asteroids[i]);

            while(!r.empty() && !l.empty()){
                int robj = Math.abs(r.peek());
                int lobj = Math.abs(l.peek());
                if (robj < lobj) r.pop();
                else if (robj > lobj) l.pop();
                else {
                    r.pop();
                    l.pop();
                }
            }
            //liberate all the left moveing
            if (r.empty()){
                while (!l.empty()) free.add(l.pop());
            }
            i++;
        }
        int[] Arr;
        Integer[] free2 = free.toArray(new Integer[0]);
        int[] freeArr = Arrays.stream(free2).mapToInt(Integer::intValue).toArray();
        if (!r.empty()){
            Arr = r.stream().mapToInt(Integer::intValue).toArray();
        }
        else{
            Arr = l.stream().mapToInt(Integer::intValue).toArray();
        }
        int[] result = new int[freeArr.length + Arr.length];
        System.arraycopy(freeArr, 0, result, 0, freeArr.length);
        System.arraycopy(Arr, 0, result, freeArr.length, Arr.length);

        return result;
    }
}
