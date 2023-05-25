class Solution:
    def intToRoman(self, num: int) -> str:
        answer = ""
        nums = [int(c) for c in str(num)]
        roman_ones = ["I", "X", "C", "M"]
        roman_five = ["V", "L", "D"]

        for i in range(0, len(nums)):
            sub_answer = ""
            c = nums[i]
            if c == 1:
                sub_answer = roman_ones[len(nums)-i-1]
            elif c == 5:
                sub_answer = roman_five[len(nums)-i-1]
            elif c == 4:
                sub_answer = roman_ones[len(nums)-i-1] + roman_five[len(nums)-i-1]
            elif c == 9:
                sub_answer = roman_ones[len(nums)-i-1] + roman_ones[len(nums)-i]
            else:
                while c > 0:
                    if c < 4:
                        sub_answer += roman_ones[len(nums)-i-1]
                        c -= 1
                    elif c < 9:
                        sub_answer += roman_five[len(nums)-i-1]
                        c -= 5
            answer += sub_answer

        return answer
