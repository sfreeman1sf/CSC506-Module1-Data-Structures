class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop() if not self.is_empty() else None
    
    def peek(self):
        return self.items[-1] if not self.is_empty() else None
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
    def __str__(self):
        return f"Stack: {self.items}"
    
class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        return self.items.pop(0) if not self.is_empty() else None
    
    def peek(self):
        return self.items[0] if not self.is_empty() else None
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
    def __str__(self):
        return f"Queue: {self.items}"
    
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
    
    def __str__(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.data))
            current
def demo():
    print("=== Data Structure Demo ===")
    s = Stack()
    s.push(10)
    s.push(20)
    print("Stack after push:", s)
    print("Popped:", s.pop())
    print("Stack now:", s)
    
    q = Queue()
    q.enqueue(5)
    q.enqueue(15)
    print("Queue after enqueue:", q)
    print("Dequeued:", q.dequeue())
    print("Queue now:", q)
    
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    print("Linked List:", ll)

if __name__ == "__main__":
    demo()