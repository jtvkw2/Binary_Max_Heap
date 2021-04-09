class TernaryMaxHeap:
    def __init__(self, tm_max):
        self.Heap = []
        self.max = int(tm_max)

    def size(self):
        return len(self.Heap)

    @staticmethod
    def parent(i):
        return (i - 1) // 3

    @staticmethod
    def left(i):
        return 3 * i + 1

    @staticmethod
    def mid(i):
        return 3 * i + 2

    @staticmethod
    def right(i):
        return 3 * i + 3

    def get(self, i):
        return self.Heap[i]

    def get_max(self):
        if self.size() == 0:
            return None
        return self.Heap[0]

    def extract_max(self):
        if self.size() == 0:
            return None
        largest = self.get_max()
        self.Heap[0] = self.Heap[-1]
        del self.Heap[-1]
        self.max_heapify(0)
        return largest

    def max_heapify(self, i):
        left = self.left(i)
        r = self.right(i)
        m = self.mid(i)
        if left <= self.size() - 1 and self.get(left) > self.get(i):
            largest = left
        else:
            largest = i
        if m <= self.size() - 1 and self.get(m) > self.get(largest):
            largest = m
        if r <= self.size() - 1 and self.get(r) > self.get(largest):
            largest = r
        if largest != i:
            self.swap(largest, i)
            self.max_heapify(largest)

    def swap(self, i, j):
        self.Heap[i], self.Heap[j] = self.Heap[j], self.Heap[i]

    def insert(self, key):
        index = self.size()
        if self.size() > self.max:
            print("Max value reached")
            return
        self.Heap.append(key)

        while index != 0:
            p = self.parent(index)
            if self.get(p) < self.get(index):
                self.swap(p, index)
            index = p
