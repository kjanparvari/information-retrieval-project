import sys

from searchengine import Candidate


class MaxHeap:
    Heap: [Candidate]

    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.Heap = [None] * (self.maxsize + 1)
        self.Heap[0] = Candidate(-1, sys.maxsize)
        self.FRONT = 1

    # Function to return the position of parent for the node currently at pos
    @staticmethod
    def parent(pos):
        return pos // 2

    # Function to return the position of the left child for the node currently at pos
    @staticmethod
    def leftChild(pos):
        return 2 * pos

    # Function to return the position of the right child for the node currently at pos
    @staticmethod
    def rightChild(pos):
        return (2 * pos) + 1

    # Function that returns true if the passed node is a leaf node
    def isLeaf(self, pos):
        if (self.size // 2) <= pos <= self.size:
            return True
        return False

    # Function to swap two nodes of the heap
    def swap(self, fpos, s_pos):
        self.Heap[fpos], self.Heap[s_pos] = (self.Heap[s_pos], self.Heap[fpos])

    # Function to heapify the node at pos
    def maxHeapify(self, pos):
        # If the node is a non-leaf node and smaller than any of its child
        if not self.isLeaf(pos):
            if self.Heap[pos].getScore() < self.Heap[self.leftChild(pos)].getScore() or self.Heap[pos].getScore() < \
                    self.Heap[self.rightChild(pos)].getScore():

                # Swap with the left child and heapify the left child
                if self.Heap[self.leftChild(pos)].getScore() > self.Heap[self.rightChild(pos)].getScore():
                    self.swap(pos, self.leftChild(pos))
                    self.maxHeapify(self.leftChild(pos))

                # Swap with the right child and heapify the right child
                else:
                    self.swap(pos, self.rightChild(pos))
                    self.maxHeapify(self.rightChild(pos))

                    # Function to insert a node into the heap

    def insert(self, element):
        if self.size >= self.maxsize:
            return
        self.size += 1
        self.Heap[self.size] = element

        current = self.size

        while self.Heap[current].getScore() > self.Heap[self.parent(current)].getScore():
            self.swap(current, self.parent(current))
            current = self.parent(current)

    # Function to print the contents of the heap
    def Print(self):
        for i in range(1, (self.size // 2) + 2):
            print(" PARENT : " + str(self.Heap[i]) +
                  " LEFT CHILD : " + str(self.Heap[2 * i]) if 2*i <= self.size else "" +
                  " RIGHT CHILD : " + str(self.Heap[2 * i + 1])) if 2*i +1 <= self.size else ""

    # Function to remove and return the maximum element from the heap
    def extractMax(self):
        popped = self.Heap[self.FRONT]
        self.Heap[self.FRONT] = self.Heap[self.size]
        self.size -= 1
        if self.size > 0:

            self.maxHeapify(self.FRONT)

        return popped
