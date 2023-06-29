# from ctypes import Structure
# from queue import LifoQueue


# Queue :
#     linear Data Structure
#     It follows Lifo
#     Insertion is done on Rear which is called (Enqueue)
#     Deletion is done on Front which is called (Dequeue)
#     Time Complexity => O(1) [Similar to Stack]

# class Queue:
#     def __init__(self):
#         self.queue = []
#     def isEmpty(self):
#         return self.queue == []
#     def enqueue(self, data):
#         self.queue.insert(0, data)
#         return '{} added to queue'.format(data)
#     def dequeue(self):
#         return self.queue.pop()
#     def sizeofQueue(self):
#         return '{} size of queue'.format(len(self.queue))

# if __name__ == '__main__':
#     q = Queue()
#     print(q.enqueue(1))
#     print(q.enqueue(2))
#     print(q.dequeue())


class Queue:
    def __init__(self, s):
        self.q = []
        self.size = s
        self.front = 0
        self.rare = 0
    def enqueue(self, ele):
        if self.rare <= self.size-1:
            self.q.append(ele)
            self.rare += 1
        else:
            return "Queue is full"
    def dequeue(self):
        # del_ele = 0
        if self.rare > self.front:
            
            del_ele = self.q[self.front]
            del self.q[self.front]
            self.front += 1
            return del_ele
        else:
            return "Queue is Empty"
    def display(self):
        return self.q[self.front : self.rare+1]


q = Queue(10)
q.enqueue(7)
q.enqueue(10)
q.enqueue(20)
print(q.display())
q.dequeue()
print(q.display())