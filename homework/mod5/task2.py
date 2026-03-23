class Node:
    """
    Вспомогательный класс для узлов списка
    """
    def __init__(self, data):
        self.data = data
        self.pref = None
        self.nref = None

    def __str__(self):
        return f"{" "*4}class <Node> data: {self.data}"

class Queue:
    def __init__(self):
        self.start = None
        self.end = None

    def __len__(self):
        node = self.start
        count = 0
        while node is not None:
            count += 1
            node = node.nref
        return count

    def pop(self):
        node = self.start
        if node is not None:
            self.start, self.start.pref = node.nref, None
            return node
        return None

    def push(self, val):
        if self.start is None:
            new_node = Node(val)
            self.start, self.end = new_node, new_node
        else:
            new_node = Node(val)
            self.end.nref = new_node
            new_node.pref, self.end = self.end, new_node

    def insert(self, n, val):
        if n > len(self) or n < 0:
            raise ValueError(f"Укажите число меньше {len(self)} и не меньше 0")
        elif n == 0:
            new_node = Node(val)
            new_node.nref = self.start
            self.start.pref = new_node
            self.start = new_node
        else:
            node_n_1 = self.start
            for _ in range(1, n):
                node_n_1 = node_n_1.nref
            node_n = node_n_1.nref
            new_node = Node(val)
            if node_n is None:
                self.end.nref = new_node
                new_node.pref = self.end
                self.end = new_node
            else:
                node_n_1.nref = new_node
                new_node.pref = node_n_1
                new_node.nref = node_n
                node_n.pref = new_node

    def print(self):
        print("Queue elements:")
        node = self.start
        while node is not None:
            print(f"{node}")
            node = node.nref

if __name__ == "__main__":
    q = Queue()
    q.push("First")
    q.push("Second")
    q.push("Third")
    q.push("Fourth")
    q.print()
    e = q.pop()
    print(f"Извлечен первый элемент очереди: {e}")
    q.print()
    print("Втавляем элемент:")
    q.insert(2, "Third and Half")
    q.print()
