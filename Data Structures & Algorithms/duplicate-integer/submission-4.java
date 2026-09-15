class Solution {
    public boolean hasDuplicate(int[] nums) {
        int[] check = new int[nums.length];
        for(int i = 0; i < check.length; i++)
        {
            int sameCount = 0;
            for(int j = 0; j < check.length; j++)
            {
                if(nums[i] == nums[j])
                {
                    sameCount++;
                }
                if(sameCount > 1)
                {
                    return true;
                }
            }
        }
        return false;
    }
}
