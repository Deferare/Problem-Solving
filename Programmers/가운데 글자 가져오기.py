
def solution(s):
    s_len = len(s)
    if s_len%2 == 0:
        return s[(s_len//2)-1]+s[s_len//2]
    return s[s_len//2]
