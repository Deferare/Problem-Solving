class Solution {
    func rearrangeBarcodes(_ barcodes: [Int]) -> [Int] {
        var maxHeap: Heap<(Int,Int)> = Heap(sort: {$0.1 > $1.1})
        var result: [Int] = []
        var counts: Dictionary<Int, Int> = [:]
        
        for barcode in barcodes {
            counts[barcode, default: 0] += 1
        }
        
        for v in counts { 
            maxHeap.insert(v)
        }
        
        while var pop = maxHeap.remove() {
            if pop.0 != result.last ?? -1 {
                result.append(pop.0)
                pop.1 -= 1
                if pop.1 > 0 {
                    maxHeap.insert(pop)
                }
            } else if var pop2 = maxHeap.remove() {
                result.append(pop2.0)
                pop2.1 -= 1
                if pop2.1 > 0 {
                    maxHeap.insert(pop2)
                }
                maxHeap.insert(pop)
            }
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

    public var count: Int {
        return nodes.count
    }

    public func peek() -> T? {
        return nodes.first
    }

    public mutating func insert(_ value: T) {
        nodes.append(value)
        shiftUp(nodes.count - 1)
    }

    public mutating func remove() -> T? {
        guard !nodes.isEmpty else {
            return nil
        }
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
        var parentIndex = self.parentIndex(ofIndex: childIndex)

        while childIndex > 0 && orderCriteria(child, nodes[parentIndex]) {
            nodes[childIndex] = nodes[parentIndex]
            childIndex = parentIndex
            parentIndex = self.parentIndex(ofIndex: childIndex)
        }
        nodes[childIndex] = child
    }

    private mutating func shiftDown(from index: Int, until endIndex: Int) {
        let leftChildIndex = self.leftChildIndex(ofIndex: index)
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

    private func parentIndex(ofIndex index: Int) -> Int {
        return (index - 1) / 2
    }

    private func leftChildIndex(ofIndex index: Int) -> Int {
        return 2*index + 1
    }

    private func rightChildIndex(ofIndex index: Int) -> Int {
        return 2*index + 2
    }
}
