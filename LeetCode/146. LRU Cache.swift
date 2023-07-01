class Node {
    var key: Int
    var value: Int
    var prev: Node?
    var next: Node?

    init(_ key: Int, _ value: Int) {
        self.key = key
        self.value = value
    }
}

class LRUCache {
    private var capacity: Int
    private var hashMap = [Int: Node]()
    private var head: Node?
    private var tail: Node?

    init(_ capacity: Int) {
        self.capacity = capacity
    }
    
    func get(_ key: Int) -> Int {
        guard let node = hashMap[key] else {
            return -1
        }
        
        remove(node)
        add(node)
        return node.value
    }
    
    func put(_ key: Int, _ value: Int) {
        if let node = hashMap[key] {
            remove(node)
        }

        if hashMap.count == capacity, let tail = tail {
            remove(tail)
        }

        add(Node(key, value))
    }

    private func add(_ node: Node) {
        node.next = head
        node.prev = nil

        head?.prev = node
        head = node

        if tail == nil {
            tail = head
        }

        hashMap[node.key] = node
    }

    private func remove(_ node: Node) {
        hashMap.removeValue(forKey: node.key)

        if let nextNode = node.next {
            nextNode.prev = node.prev
        } else {
            tail = node.prev
        }

        if let prevNode = node.prev {
            prevNode.next = node.next
        } else {
            head = node.next
        }
    }
}
