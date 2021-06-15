import kotlin.math.max

class Solution {
fun longestPalindromeSubseq(s:String) : Int {
        var memo = mutableMapOf<String,Int>()
        fun dp(index1:Int, index2:Int) : Int {
            if (index1 == index2) {
                return 1
            }
            else if (index1 > index2) {
                return 0
            }
            val key = index1.toString() + "|" + index2.toString()
            if (memo.containsKey(key)) {
                return memo.get(key)!!
            }
            if (s.get(index1) == s.get(index2)) {
                val result = dp(index1+1, index2-1)?.plus(2)
                return result
            }
            val result = max(dp(index1+1,index2),dp(index1,index2-1))
            memo.put(key, result)
            return result
        }
        return dp(0, s.length-1)
    }
}
