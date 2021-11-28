# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        while n > 0:
            if n-100000 > 0:
                n -= 100000
            elif n-10000 > 0:
                n -= 10000
            elif n-1000 > 0:
                n -= 1000
            elif n-100 > 0:
                n -= 100
            elif n - 10 > 0:
                n -= 10
            else:
                n -= 1
            if not isBadVersion(n):
                while not isBadVersion(n):
                    n += 1
                break
        return n
