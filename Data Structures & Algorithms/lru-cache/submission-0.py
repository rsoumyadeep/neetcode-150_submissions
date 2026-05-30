class Node:
    """Doubly linked list node."""
    __slots__ = ('key', 'val', 'prev', 'next')
    def __init__(self, key=0, val=0):
        self.key, self.val = key, val
        self.prev = self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.map = {}                  # key -> Node

        # Sentinel head (MRU side) and tail (LRU side)
        self.head = Node()             # dummy head
        self.tail = Node()             # dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head

    # ── Internal helpers ──────────────────────────────────────────────

    def _remove(self, node: Node) -> None:
        """Detach node from its current position."""
        node.prev.next = node.next
        node.next.prev = node.prev

    def _insert_front(self, node: Node) -> None:
        """Insert node right after dummy head (= mark as most-recently used)."""
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    # ── Public API ────────────────────────────────────────────────────

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        node = self.map[key]
        self._remove(node)             # detach from current pos
        self._insert_front(node)       # move to MRU end
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self._remove(self.map[key])
        node = Node(key, value)
        self.map[key] = node
        self._insert_front(node)

        if len(self.map) > self.cap:   # evict LRU
            lru = self.tail.prev       # node just before dummy tail
            self._remove(lru)
            del self.map[lru.key]