import Foundation

func solution(_ sizes:[[Int]]) -> Int {
    var maxWidth = 0, maxHeight = 0
    
    for size in sizes {
        if size[0] > size[1] {
            maxWidth = max(maxWidth, size[0])
            maxHeight = max(maxHeight, size[1])
        } else {
            maxWidth = max(maxWidth, size[1])
            maxHeight = max(maxHeight, size[0])
        }
    }
    
    return maxWidth * maxHeight
}
