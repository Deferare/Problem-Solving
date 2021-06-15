fun main() {
    var str = readLine()
    var happyCnt = 0; var sadCnt = 0
    for (i in 0 until str!!.length-2) {
        if (str[i] == ':') {
            if (str[i+1] == '-' && str[i+2] == ')') happyCnt++
            else if (str[i+1] == '-' && str[i+2] == '(') sadCnt++
        }
    }
    if (happyCnt == 0 && sadCnt == 0) print("none")
    else if (happyCnt == sadCnt) print("unsure")
    else if (happyCnt > sadCnt) print("happy")
    else if (happyCnt < sadCnt) print("sad")
}
