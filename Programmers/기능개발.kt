class Solution {
    fun solution(progresses: IntArray, speeds: IntArray): IntArray {
        var result = ""
        var index = 0
        var check = 0
        while (true) {
            while (true) {
                for (i in progresses.indices) {
                    if (progresses[i] != 0) progresses[i] += speeds[i]
                }
                if (progresses[index] >= 100) break
            }
            var cnt = 0
            for (i in index until progresses.size) {
                if (progresses[i] >= 100) {
                    cnt++
                    progresses[i] = 0
                    index++
                } else if (progresses[i] <= 100 || i == progresses.size - 1) {
                    break
                }
            }
            check++
            result += "$cnt "
            if (progresses[progresses.size - 1] == 0) break
        }
        val result2 = IntArray(check)
        index = 0
        var saveStr = ""
        for (i in 0 until result.length) {
            if (result[i] != ' ') {
                saveStr += result[i]
            } else if (result[i] == ' ') {
                result2[index] = saveStr.toInt()
                index++
                saveStr = ""
            }
        }
        return result2
    }
}
