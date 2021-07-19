fun main() {
    val (n,m) = readLine()!!.split(" ").map { it.toInt() }
    val words_n = mutableMapOf<String,Int>()
    for (i in 0..n-1){
        words_n.put(readLine().toString(),1)
    }
    var result_list = mutableListOf<String>()
    for (i in 0..m-1){
        val word = readLine().toString()
        if (word in words_n){
            result_list.add(word)
        }
    }
    result_list.sort()
    println(result_list.size)
    for (crnt in result_list){
        println(crnt)
    }
}
