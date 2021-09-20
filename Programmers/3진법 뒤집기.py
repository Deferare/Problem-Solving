def base_convert(n, q):
    rev_base = ''
    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)
    return rev_base
def solution(n):
    return int(base_convert(n,3),3)
