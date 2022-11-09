class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def check(a:str, b:str) -> bool:
            a = str(a)
            b = str(b)
            left = a+b
            right = b+a
            return left < right
        answer = ""
        for i in range(0, len(nums)-1):
            for j in range(i+1, len(nums)):
                if check(nums[i], nums[j]):
                    nums[i], nums[j] = nums[j], nums[i]
        for n in nums:
            answer += str(n)
        return str(int(answer))
