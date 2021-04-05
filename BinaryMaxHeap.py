import sys


class BinaryMaxHeap:
    def __init__(self, maxsize):
        self.maxsize = int(maxsize)
        self.size = 0
        self.Heap = [[0] * i for i in range(self.maxsize+1)]
        self.Heap[0] = sys.maxsize
        self.head = 1

    @staticmethod
    def parent(pos):

        return pos // 2

    @staticmethod
    def left(pos):

        return 2 * pos

    @staticmethod
    def right(pos):

        return (2 * pos) + 1

    def is_leaf(self, pos):

        if (self.size // 2) <= pos <= self.size:
            return True
        return False

    def swap(self, fpos, swap_pos):

        self.Heap[fpos], self.Heap[swap_pos] = (self.Heap[swap_pos],
                                                self.Heap[fpos])

    def max_heapify(self, pos):
        if not self.is_leaf(pos):
            if (self.Heap[pos] < self.Heap[self.left(pos)] or
                    self.Heap[pos] < self.Heap[self.right(pos)]):

                # Swap with the left child and heapify
                # the left child
                if (self.Heap[self.left(pos)] >
                        self.Heap[self.right(pos)]):
                    self.swap(pos, self.left(pos))
                    self.max_heapify(self.left(pos))

                # Swap with the right child and heapify
                # the right child
                else:
                    self.swap(pos, self.right(pos))
                    self.max_heapify(self.right(pos))

    def insert(self, element):

        if self.size >= self.maxsize:
            print("Max value reached")
            return
        self.size += 1
        self.Heap[self.size] = element

        current = self.size

        while (self.Heap[current] >
               self.Heap[self.parent(current)]):
            self.swap(current, self.parent(current))
            current = self.parent(current)

    def extract_max(self):

        popped = self.Heap[self.head]
        self.Heap[self.head] = self.Heap[self.size]
        self.size -= 1
        self.max_heapify(self.head)

        return popped

    def get_max(self):
        if self.size == 0:
            return None
        return self.Heap[1]
