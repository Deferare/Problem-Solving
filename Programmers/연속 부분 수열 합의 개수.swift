import Foundation

func solution(_ elements: [Int]) -> Int {
    let extendedElements = elements + elements
    var sumSet = Set<Int>()
    
    for i in 0..<elements.count {
        var sum = 0
        for j in i..<i+elements.count {
            sum += extendedElements[j]
            sumSet.insert(sum)
        }
    }

    return sumSet.count
}
