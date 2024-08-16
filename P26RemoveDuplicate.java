// My solution
class Solution {
    public int removeDuplicates(int[] nums) {
        if (nums.length == 0 || nums.length==1) return nums.length;
        int head=0;
        int tail = head + 1;
        boolean fwd = false;
        int count = 1;
        while (tail < nums.length){
            while (tail < nums.length  && nums[head] == nums[tail]){
                tail++;
            }
            if (tail >= (nums.length) ) return count;
            swap (nums, head + 1, tail);
            head++;
            tail++;
            count++;
        }
        return count;
    }
    private void swap (int[] nums, int i, int j){
        int tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp; 
    }
}

// Solution from community
class Solution {
    public int removeDuplicates(int[] arr) {
        int i=0;
        for(int j=1;j<arr.length;j++){
            if(arr[i]!=arr[j]){
                i++;
                arr[i]=arr[j];
            }
        }
        return i+1;
        
    }
}
