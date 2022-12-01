class Queue:
    def __init__(self):
        self.value = []

    def __len__(self):
        return len(self.value)

    def enqueue(self, value):
        self.value.append(value)

    def dequeue(self):
        return self.value.pop(0)

    def search(self, index):
        if index > len(self.value) or index < 0:
            raise IndexError
        return self.value[index]
