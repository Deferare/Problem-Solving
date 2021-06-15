fun main() {
    while (true) {
        var str = readLine()
        if (str == "END") break
        else {
            var saveStr = ""
            for (i in str!!.length-1 downTo 0) {
                saveStr += str[i]
            }
            println(saveStr)
        }
    }
}
