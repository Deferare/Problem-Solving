class Solution {
    func maxScore(_ nums1: [Int], _ nums2: [Int], _ k: Int) -> Int {
        let n = nums1.count
        var nums:[(Int,Int)] = []
        for i in 0..<n {
            nums.append((nums1[i], nums2[i]))
        }
        nums.sort{$0.1 > $1.1}
        
        var sum = 0
        var hp = Heap([Int](), <)
        for i in 0..<k {
            hp.push(nums[i].0)
            sum += nums[i].0
        }
        
        var maxSum = sum * nums[k-1].1
        for i in k..<n {
            if let minum = hp.peek(), minum < nums[i].0 {
                sum = sum - hp.pop()! + nums[i].0
                hp.push(nums[i].0)
            }
            
            maxSum = max(maxSum, sum * nums[i].1)
        }
        
        return maxSum
    }
}

struct Heap<Element> {
    var elements : [Element]
    var sort : (Element, Element) -> Bool

    init(_ elements: [Element], _ sort: @escaping (Element, Element) -> Bool) {
        self.elements = elements
        self.sort = sort
    }

    var isEmpty : Bool {
        return self.elements.isEmpty
    }

    var count : Int {
        return self.elements.endIndex
    }

    func isRoot(_ index: Int) -> Bool {
        return index == 0
    }

    func peek() -> Element? {
        return self.elements.first
    }

    func parentIdx(of index: Int) -> Int {
        return (index - 1) / 2
    }

    func leftChildIdx(of index: Int) -> Int {
        return (index * 2) + 1
    }

    func rightChildIdx(of index: Int) -> Int {
        return (index * 2) + 2
    }

    func isHigherPriority(at firstIdx: Int, than secondIdx: Int) -> Bool {
        return sort(elements[firstIdx], elements[secondIdx])
    }

    func highestPriorityIdx(of parent: Int, and child: Int) -> Int {
        guard child < count && isHigherPriority(at: child, than: parent) else {
            return parent
        }
        return child
    }

    func highestPriorityIdx(of parent: Int) -> Int {
        return highestPriorityIdx(of: highestPriorityIdx(of: parent, and: leftChildIdx(of: parent)), and: rightChildIdx(of: parent))
    }

    mutating func push(_ element: Element) {
        self.elements.append(element)
        siftUp(from: count-1)
    }

    mutating func pop() -> Element? {
        if isEmpty { return nil }
        swapElements(at: 0, with: count - 1)
        let element = self.elements.removeLast()

        if !isEmpty {
            siftDown(from: 0)
        }
        return element
    }

    mutating func swapElements(at firstIdx: Int, with secondIdx: Int) {
        if firstIdx == secondIdx { return }
        self.elements.swapAt(firstIdx, secondIdx)
    }

    mutating func siftUp(from index: Int) {
        let parent = parentIdx(of: index)

        guard !isRoot(index) && isHigherPriority(at: index, than: parent) else { return }
        swapElements(at: index, with: parent)
        siftUp(from: parent)
    }

    mutating func siftDown(from index: Int) {
        let child = highestPriorityIdx(of: index)

        guard child != index else { return }
        swapElements(at: index, with: child)
        siftDown(from: child)
    }
}
