#!/usr/bin/env python3

class DLinkedNode:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None

class DLinkedList:
    def __init__(self):
        self.head = DLinkedNode(-1, -1)
    def PopLRUKey(self):
        node = self.head.next
        if node.next != None:
            node.next.prev = self.head
        self.head.next = node.next
        return node.key
    def InsertNode(self, node):
        if self.head.next == None:
            self.head.next = node
            self.head.prev = node
            node.next = self.head
            node.prev = self.head
        else:
            self.head.prev.next = node
            node.next = self.head
            node.prev = self.head.prev
            self.head.prev = node
    def PromoteNode(self, node):
        if node.prev != None:
            node.prev.next = node.next
        if node.next != None:
            node.next.prev = node.prev
        self.InsertNode(node)

class LRUCache:
    # @param capacity, an integer
    def __init__(self, capacity):
        self.cap = capacity
        self.pages = {}
        self.LRUList = DLinkedList()

    # @return an integer
    def get(self, key):
        if key in self.pages:
            self.LRUList.PromoteNode(self.pages[key])
            return self.pages[key].val
        else:
            return -1

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self.pages:
            self.LRUList.PromoteNode(self.pages[key])
            self.pages[key].val = value
        else:
            newNode = DLinkedNode(key, value)
            self.LRUList.InsertNode(newNode)
            self.pages[key] = newNode
        if len(self.pages) > self.cap:
            LRUKey = self.LRUList.PopLRUKey()
            del self.pages[LRUKey]
            
def main():
    l = LRUCache(10)
    for i in range(1, 12):
        l.set(i,i*10)
    print(l.get(2))

if __name__ == "__main__":
    main()