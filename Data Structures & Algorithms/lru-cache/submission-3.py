class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.dictionary = {}


    def remove(self, node):
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next

        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev


    def add_to_tail(self, node):
        node.prev = self.tail
        node.next = None

        if self.tail:
            self.tail.next = node
        else:
            self.head = node

        self.tail = node


    def get(self, key: int) -> int:
        if key not in self.dictionary:
            return -1

        node = self.dictionary[key]

        self.remove(node)
        self.add_to_tail(node)

        return node.value


    def put(self, key: int, value: int) -> None:
        if key in self.dictionary:
            node = self.dictionary[key]
            node.value = value

            self.remove(node)
            self.add_to_tail(node)

        else:
            node = Node(key, value)
            self.dictionary[key] = node
            self.add_to_tail(node)

            if len(self.dictionary) > self.capacity:
                lru = self.head

                self.remove(lru)
                del self.dictionary[lru.key]