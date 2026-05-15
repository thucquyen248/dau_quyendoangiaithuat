class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}  # key -> Node
        # Dummy head và tail để dễ quản lý
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        """Xóa node khỏi danh sách liên kết"""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add_to_front(self, node):
        """Thêm node vào ngay sau head (đầu danh sách)"""
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            # Đưa node lên đầu (vì vừa được dùng)
            self._remove(node)
            self._add_to_front(node)
            return node.value
        return -1

    def put(self, key, value):
        if key in self.cache:
            # Cập nhật giá trị và đưa lên đầu
            node = self.cache[key]
            node.value = value
            self._remove(node)
            self._add_to_front(node)
        else:
            if len(self.cache) >= self.capacity:
                # Xóa node cuối (LRU)
                lru = self.tail.prev
                self._remove(lru)
                del self.cache[lru.key]
            # Thêm node mới
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_to_front(new_node)
