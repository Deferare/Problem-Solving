class Solution {
func exist(_ board: [[Character]], _ word: String) -> Bool {
    func dfs(_ checkArr:[[Int]],_ wordIndex:Int,_ index1:Int,_ index2:Int) {
        if wordIndex == word.count {
            result = true
            return
        }
        if index1 >= board.count || index2 >= board[0].count || index1 < 0 || index2 < 0 {
            return
        }
        if checkArr[index1][index2] != -1 {
            return
        }
        if board[index1][index2] == word.get(wordIndex) {
            var checkArr = checkArr
            checkArr[index1][index2] = 0
            var wordIndex = wordIndex
            wordIndex += 1
            dfs(checkArr, wordIndex, index1+1, index2)
            dfs(checkArr, wordIndex, index1-1, index2)
            dfs(checkArr, wordIndex, index1, index2+1)
            dfs(checkArr, wordIndex, index1, index2-1)
        }
    }
    var result = false
    let checkArr = [Array](repeating: [Int](repeating: -1, count: board[0].count), count: board.count)
    loop : for i in 0...board.count-1 {
        for j in 0...board[0].count-1 {
            if board[i][j] == word.get(0) {
                dfs(checkArr, 0, i, j)
                if result == true {
                    break loop
                }
            }
        }
    }
    return result
}
}

extension String {
    func get(_ index:Int) -> Character {
        return self[self.index(self.startIndex, offsetBy: index)]
    }
}
