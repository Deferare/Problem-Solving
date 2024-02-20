import Foundation

class Solution {
    func eatenApples(_ apples: [Int], _ days: [Int]) -> Int {
        var pq: Heap<(expiration: Int, count: Int)> = Heap(sort: { a, b in return a.expiration < b.expiration })
        var eaten = 0
        var i = 0
        
        while i < apples.count || !pq.isEmpty {
            if i < apples.count && apples[i] > 0 {
                pq.insert((i + days[i], apples[i]))
            }
            
            while let top = pq.peek(), top.expiration <= i {
                let _ = pq.remove()
            }
            
            if var top = pq.remove(), top.expiration > i {
                eaten += 1
                top.count -= 1
                if top.count > 0 {
                    pq.insert(top)
                }
            }
            
            i += 1
        }
        
        return eaten
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
    
    public var isEmpty: Bool {
        return nodes.count == 0
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
