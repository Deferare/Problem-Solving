class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        arr = [1]*n  # Initialize arr with size n, all set to 1 as each child must have at least one candy

        # Forward pass: If the current child has a higher rating than the previous one, give him one more candy than the previous one
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                arr[i] = arr[i-1] + 1

        # Backward pass: If the current child has a higher rating than the next one and less candies, give him one more candy than the next one
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                arr[i] = max(arr[i], arr[i+1] + 1)

        return sum(arr)  # Return the total number of candies
