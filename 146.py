# 请你设计并实现一个满足  LRU (最近最少使用) 缓存 约束的数据结构。
# 实现 LRUCache 类：
# LRUCache(int capacity) 以 正整数 作为容量 capacity 初始化 LRU 缓存
# int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
# void put(int key, int value) 如果关键字 key 已经存在，则变更其数据值 value ；如果不存在，则向缓存中插入该组 key-value 。如果插入操作导致关键字数量超过 capacity ，则应该 逐出 最久未使用的关键字。
# 函数 get 和 put 必须以 O(1) 的平均时间复杂度运行。
class Node:
    def __init__(self, key = 0, value = 0):
        self.key = key
        self.value = value
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dummy = Node()
        self.dummy.next = self.dummy
        self.dummy.prev = self.dummy
        self.key_to_node = {}
    
    def get_node(self, key):
        if key not in self.key_to_node:
            return None
        node = self.key_to_node[key]
        self.remove_node(node)
        self.put_front(node)
        
        


    def get(self, key: int) -> int:
        node = self.get_node(key)
        return node.value if node else -1


    def put(self, key: int, value: int) -> None:
        node = self.get_node(key)
        if node:
            node.value = value
            return
        node = Node(key, value) = self.key_to_node[key]
        self.put_front(node)
        self.put_front(node)
        if len(self.key_to_node) > self.capacity:
            back_book = self.dummy.prev
            del self.key_to_node[back_book.key]
            self.remove_node(back_book)
        
        
    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        
    def put_front(self, node):
        node.prev = self.dummy
        node.next = self.dummy.next
        node.prev.next = node
        node.next.prev = node
        



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)