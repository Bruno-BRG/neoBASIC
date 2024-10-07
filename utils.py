class Buffer:
    def __init__(self):
        self.lines = []

    def append(self, line):
        self.lines.append(line)

    def clear(self):
        self.lines = []

class Variables:
    def __init__(self):
        self.data = {}