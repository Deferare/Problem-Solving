def solution(prices):
    stack = []
    result = [0 for _ in range(len(prices))]
    for i in range(len(prices)):
        if len(stack) != 0 and prices[i] > prices[stack[-1]]:
            stack.append(i)
        else:
            while len(stack) > 0 and prices[stack[-1]] > prices[i]:
                pop = stack.pop()
                result[pop] = i-pop
            stack.append(i)
    while len(stack) > 0:
        pop = stack.pop()
        result[pop] = len(prices)-pop-1
    return result
