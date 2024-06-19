class Node:
    def __init__(self, value: int, key: int):

        self.value = value
        self.key = key
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.map = {}
        self.capacity = capacity

        self.head = Node(0, 0)
        self.tail = Node(0, 0)

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1

        node = self.map[key]

        self._remove(node)
        self._append(node)

        return node.value
        

    def put(self, key: int, value: int) -> None:

        if key in self.map:

            node = self.map[key]
            node.value = value
            self._remove(node)
            self._append(node)

            return 

        if len(self.map) >= self.capacity:
            del self.map[self.head.next.key]
            self._remove(self.head.next)
        
        new_node = Node(value, key)
        self.map[key] = new_node
        self._append(new_node)

        return
    
    def _remove(self, node: Node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

    def _append(self, node: Node) -> None:
        
        last_node = self.tail.prev
        last_node.next = node
        node.prev = last_node

        node.next = self.tail
        self.tail.prev = node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)