# TODO: Implement a circular queue

class circular_queue:
    def __init__(self):
        self.queue = list()
        self.max_size = 20
        self.first =0 
        self.last = 0 

    def enque(self, e):
        if self.findsize() == (self.max_size - 1):
            print("Element can not be enqueued, the queue is already full")
        else:
            self.queue.append(e)
            self.last = (self.last + 1) % self.max_size

    def deque(self):
        if self.findsize() == 0:
            print("Element can not be dequeued, the queue is already empty.")
        else:
            element = self.queue[self.first] #HACK: Used for testing
            self.queue[self.first] = None
            self.first = (self.first + 1) % self.max_size
            print(f"dequeued {element}") #HACK: Used for testing


    def findsize(self):
        if self.last >= self.first:
            size = self.last - self.first
        else:
            size = self.max_size - (self.first - self.last)
        return size

    def displayQ(self):
        print(self.queue)


if __name__ == "__main__":
    q = circular_queue()
    q.enque(10)
    q.enque(20)
    q.enque(30)
    q.enque(40)
    q.enque(50)
    q.enque(70)
    q.enque(80)
    q.enque(90)
    q.displayQ()
    q.deque()
    q.deque()
    q.deque()
    q.displayQ()
    q.deque()
    q.deque()
    q.deque()
    q.displayQ()
