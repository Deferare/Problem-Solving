fun main() {
    var arr = Array(5,{""})
    var max:Int = 0
    for (i in 0..arr.size-1) {
        arr[i] = readLine().toString()
        if (arr[i].length > max)
            max = arr[i].length
    }
    var result = ""
    for (i in 0..max-1) {
        for (j in 0 .. arr.size-1) {
            if (arr[j].length > i)
                result += arr[j].get(i)
        }
    }
    print(result)
}
