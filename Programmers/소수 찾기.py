def prime_getter(range_of):
    prime_numbers = [2, 3, 5, 7]
    if range_of <= prime_numbers[-1]:
        sub_result = []
        for i in range(4):
            if prime_numbers[i] <= range_of:
                sub_result.append(prime_numbers[i])
            else:
                return set(sub_result)
    while True:
        start_num = prime_numbers[-1]
        push_primes = []
        end_num = 0
        for num in range(start_num + 1, (start_num * start_num) + 1):
            if num > range_of:
                end_num = num
                break
            push_primes.append(num)
            for prime in prime_numbers:
                if num%prime == 0:
                    push_primes.pop(-1)
                    break
        prime_numbers.extend(push_primes)
        if end_num >= range_of:
            break
    return set(prime_numbers)



def solution(n):
    primes = prime_getter(n)
    result_cnt = 0
    for crnt in range(1,n+1):
        if crnt in primes:
            result_cnt += 1
    return result_cnt
