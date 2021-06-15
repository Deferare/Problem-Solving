fun main (args: Array<String>) {
    var str = readLine()
    var arr = Array(26,{-1})
    for (i in 0 until str!!.length) {
        if (arr[str.get(i)-'a'] == -1)
            arr[str.get(i)-'a'] = i
    }
    for (i in 0 until arr.size-1) {
        print("${arr[i]} ")
    }
    print(arr[arr.size-1])
}
