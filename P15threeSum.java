class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> answers = new ArrayList<List<Integer>>();
        
        Arrays.sort(nums);
        
        for (int i = 0; i < nums.length - 2; i++ ){

            if (i >= 1 && nums[i] == nums[i-1]){
                continue; // skip this totally
            }
            for (int j = (i + 1); j < nums.length; j++){
                if (j > (i+1) && nums[j] == nums[j-1]){
                    continue; // skip this totally
                }
                int negate = -(nums[i] + nums[j]);
                int idx = Arrays.binarySearch(nums, j + 1, nums.length, negate);
                if (idx > 0){ // found
                    List<Integer> answer = new ArrayList<Integer>();
                    answer.add(nums[i]);
                    answer.add(nums[j]);
                    answer.add(nums[idx]);
                    answers.add (answer);
                }
            }
        }
        return answers;

    }
}
