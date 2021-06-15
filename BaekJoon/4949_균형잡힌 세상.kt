fun main (args: Array<String>) {
    while (true) {
        var str = readLine()
        if (str == ".") break;
        var saveStr = ""
        for (i in 0 until str!!.length) {
            if (str[i] == '[' || str[i] == '(' || str[i] == ']' || str[i] == ')') {
                saveStr += str[i]
            }
        }
        var check = 0;
        var i = 0
        while (i < saveStr.length-1) {
            if (saveStr[i] == '(') {
                if (saveStr[i+1] == ')') {
                    saveStr = saveStr.removeRange(i,i+2)
                    i = 0; continue
                }
            }
            else if (saveStr[i] == '[') {
                if (saveStr[i+1] == ']') {
                    saveStr = saveStr.removeRange(i,i+2)
                    i = 0; continue
                }
            }
            else {
                check = 1
                break;
            }
            i++
        }
        if (check == 1 || saveStr.length != 0) println("no")
        else println("yes")
    }
}
