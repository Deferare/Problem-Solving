class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left = 0
        right = len(letters) - 1
        min_result = letters[-1]
        while left < right and left < len(letters):
            mid = (left + right) // 2
            if letters[mid] > target[0] and letters[mid] < min_result:
                min_result = letters[mid]
            if letters[left] > target[0] and letters[left] < min_result:
                min_result = letters[left]
            if letters[mid] <= target[0]:
                left = mid + 1
            elif letters[mid] > target[0]:
                right = mid
        if min_result <= target[0]:
            return letters[0]
        return min_result
