fun main()  {
    var n = readLine()!!.toInt()
    print(factorial(n))
}
fun factorial(n:Int):Int {
    if (n == 0) return 1
    if (n == 1) return 1
    return factorial(n-1)*n
}
