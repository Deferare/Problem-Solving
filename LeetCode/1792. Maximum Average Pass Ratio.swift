class Solution {
    func maxAverageRatio(_ classes: [[Int]], _ extraStudents: Int) -> Double {
        var heap = Heap<(increment: Double, p: Int, t: Int)>(sort: {$0.increment > $1.increment})
        
        for i in 0..<classes.count {
            heap.insert((Double(classes[i][0]+1)/Double(classes[i][1]+1) - Double(classes[i][0])/Double(classes[i][1]), classes[i][0], classes[i][1] ))
        }
        
        var extraStudents = extraStudents
        
        while extraStudents > 0 {
            if let low = heap.remove() {
                heap.insert((Double(low.p+2)/Double(low.t+2) - Double(low.p+1)/Double(low.t+1), low.p+1, low.t+1))
                extraStudents -= 1
            } else {break}
        }
        var result: Double = 0
        for element in heap.nodes {
            result += (Double(element.p)/Double(element.t))/Double(classes.count)
        }
        
        return result
    }
}

public struct Heap<T> {
    var nodes = [T]()
    private var orderCriteria: (T, T) -> Bool
    public init(sort: @escaping (T, T) -> Bool) {
        self.orderCriteria = sort
    }
    public var isEmpty: Bool {
        return nodes.isEmpty
    }
    public func peek() -> T? {
        return nodes.first
    }
    public mutating func insert(_ value: T) {
        nodes.append(value)
        shiftUp(nodes.count - 1)
    }
    public mutating func remove() -> T? {
        guard !nodes.isEmpty else { return nil }
        if nodes.count == 1 {
            return nodes.removeFirst()
        } else {
            let value = nodes[0]
            nodes[0] = nodes.removeLast()
            shiftDown(0)
            return value
        }
    }
    private mutating func shiftUp(_ index: Int) {
        var childIndex = index
        let child = nodes[childIndex]
        var parentIndex = self.parentIndex(of: childIndex)
        while childIndex > 0 && orderCriteria(child, nodes[parentIndex]) {
            nodes[childIndex] = nodes[parentIndex]
            childIndex = parentIndex
            parentIndex = self.parentIndex(of: childIndex)
        }
        nodes[childIndex] = child
    }
    private mutating func shiftDown(from index: Int, until endIndex: Int) {
        let leftChildIndex = self.leftChildIndex(of: index)
        let rightChildIndex = leftChildIndex + 1
        var first = index
        if leftChildIndex < endIndex && orderCriteria(nodes[leftChildIndex], nodes[first]) {
            first = leftChildIndex
        }
        if rightChildIndex < endIndex && orderCriteria(nodes[rightChildIndex], nodes[first]) {
            first = rightChildIndex
        }
        if first == index { return }
        nodes.swapAt(index, first)
        shiftDown(from: first, until: endIndex)
    }
    private mutating func shiftDown(_ index: Int) {
        shiftDown(from: index, until: nodes.count)
    }
    private func parentIndex(of index: Int) -> Int {
        return (index - 1) / 2
    }
    private func leftChildIndex(of index: Int) -> Int {
        return 2*index + 1
    }
    private func rightChildIndex(of index: Int) -> Int {
        return 2*index + 2
    }
}
