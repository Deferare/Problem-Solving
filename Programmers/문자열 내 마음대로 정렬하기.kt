class Solution {
fun solution(strings: Array<String>, n: Int): Array<String> {
    var arr = Array(strings.size,{' '})
    var i = 0
    while (i < strings.size-1) {
        var j = 0
        while(j < strings.size-1) {
            if (strings[j][n] > strings[j+1][n]) {
                var tmpS1 = strings[j]
                var tmpS2 = strings[j+1]
                strings[j] = tmpS2
                strings[j+1] = tmpS1
            }
            else if (arr[j]-'0' == arr[j]-'0') {
                var index = 0
                while(true) {
                    if (strings[j][index] > strings[j+1][index]) {
                        var tmpS1 = strings[j]
                        var tmpS2 = strings[j+1]
                        strings[j] = tmpS2
                        strings[j+1] = tmpS1
                        j--
                        break
                    }
                    else if (strings[j][index] < strings[j+1][index]) {
                        break;
                    }
                    if (index == strings[j].length-1 || index == strings[j+1].length-1)
                        break;
                    index++
                }
            }
            j++
        }
        i++
    }
    return strings
}
}
