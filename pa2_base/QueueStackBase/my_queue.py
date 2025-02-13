from array_deque import ArrayDeque


class Queue:
    def __init__(self):
        self.container = ArrayDeque()

    def add(self, data):
        """Takes a parameter and adds its value to the back of the queue."""
        self.container.push_back(data)

    def remove(self):
        """Removes the item off the front of the queue and returns its value."""
        return self.container.pop_front()

    def get_size(self):
        return self.container.get_size()

    def __str__(self):
        return str(self.container)
