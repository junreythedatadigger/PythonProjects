# Write a function to reverse a queue.
# A queue is a data structure that follows the First In, First Out (FIFO) principle.



class Queue:

    def __init__(self, queue_array=[]):
        self.queue_array = queue_array

    def add(self, element):
        self.queue_array.append(element)
        return self.queue_array

    def remove(self):
        first_item = self.queue_array[0]
        self.queue_array.pop(0)
        return first_item

    def is_empty(self):
        if len(self.queue_array) == 0:
            return True
        else:
            return False


def main():
    queue = Queue([1, 2, 3, 4, 5])
    stack = []
    while not queue.is_empty():
        stack.append(queue.remove())
    print(stack)


if __name__ == "__main__":
    main()
