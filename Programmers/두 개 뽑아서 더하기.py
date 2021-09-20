def solution(numbers):
    basket = set()
    n_sum = 0
    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            n_sum = numbers[i] + numbers[j]
            if n_sum not in basket:
                basket.add(n_sum)
    result_arr = list(basket)
    return sorted(result_arr)
