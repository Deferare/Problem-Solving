import Foundation

func solution(_ array:[Int], _ commands:[[Int]]) -> [Int] {
    var result: [Int] = []
    
    for command in commands {
        result.append(array[command[0]-1...command[1]-1].sorted()[command[2]-1])
    }
    
    return result
}
