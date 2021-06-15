class Solution {
fun solution(numbers: IntArray): IntArray {
    var data = ArrayDeque<Int>()
    numbers.sort()
    for (i in 0 until numbers.size-1) {
        for (j in i+1 until numbers.size) {
            var save = numbers[i]+numbers[j]
            if (!data.contains(save)) {
                data.addLast(save)
            }
        }
    }
    var resultArr = IntArray(data.size)
    for (i in 0 until data.size) {
        resultArr[i] = data.elementAt(i)
    }
    return resultArr
}
}
