class PriorityQueue:
    def __init__(self, array=[]):
        self.array = array

    def get_values(self):
        return self.array

    def add_value(self, value):
        if len(self.array) == 0:
            self.array.append(value)
        elif self.array[-1] < value:
            self.array.append(value)
        else:
            self.array.append(self.array[-1])
            index = -3
            while self.array[index] > value:
                self.array[index+1] = self.array[index]
                index -= 1
            else:
                self.array[index+1] = value
        return self.get_values()

"""
[1,3,5,7,9] <- 6
[1,3,5,7,9,9]
[1,3,5,7,7,9]

"""

pq = PriorityQueue([1, 3, 5, 7, 9])
print(pq.get_values())
# pq.add_value(3)
print(pq.add_value(4))
