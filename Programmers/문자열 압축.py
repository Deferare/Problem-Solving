def solution(s):
    def recursion(bias):
        sub_result = ""
        i = 0
        n = 1
        while i+bias <= len(s):
            left = s[i:i + bias]
            right = s[i+bias:i+bias+bias]
            if left == right:
                n += 1
            else:
                if n == 1:
                    sub_result += left
                else:
                    sub_result += str(n) + left
                    n = 1
            i += bias
        sub_result += s[i:]
        return len(sub_result)
    n_min = len(s)
    for i in range(1, (len(s)//2)+1):
        sub_n = recursion(i)
        if sub_n < n_min:
            n_min = sub_n
    return n_min
