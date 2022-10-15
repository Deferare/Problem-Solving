class Solution {
  void nextPermutation(List<int> nums) {
    int left = nums.length-2;
    int right = left + 1;
    while (true){
      if (left < 0){
        nums.sort();
        return;
      }
      while (true){
        if (right <= left){
          right = nums.length-1;
          break;
        }
        if (nums[right] > nums[left]){
          int tmp = nums[right];
          nums[right] = nums[left];
          nums[left] = tmp;

          List<int> tmpList = [];
          for (var i = left+1; i < nums.length; i++){
            tmpList.add(nums[i]);
          }
          tmpList.sort();
          for (var i = 0; i < tmpList.length; i++){
            nums[left+1+i] = tmpList[i];
          }
          return;
        }
        right -= 1;
      }
      left -= 1;
    }
  }
}
