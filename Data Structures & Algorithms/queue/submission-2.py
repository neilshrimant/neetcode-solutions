class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

class Deque:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head


    def isEmpty(self) -> bool:
        return self.head.next == self.tail    

    def append(self, value: int) -> None:
        new_node = Node(value)
        prevNode = self.tail.prev

        prevNode.next = new_node
        new_node.next = self.tail
        new_node.prev = prevNode
        self.tail.prev = new_node
        

    def appendleft(self, value: int) -> None:
        new_node = Node(value)
        nextNode = self.head.next

        nextNode.prev = new_node
        new_node.prev = self.head
        new_node.next = nextNode
        self.head.next = new_node


    def pop(self) -> int:
        if self.isEmpty():
            return -1
        lastNode = self.tail.prev
        value = lastNode.value
        prevNode = lastNode.prev
        prevNode.next = self.tail
        self.tail.prev = prevNode
        return value


    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        firstNode = self.head.next
        value = firstNode.value
        nextNode = firstNode.next
        nextNode.prev = self.head
        self.head.next = nextNode
        return value
            
        
