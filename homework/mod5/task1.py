class Node:
    """
    Вспомогательный класс для узлов списка
    """
    def __init__(self, data):
        self.data = data
        self.pref = None

    def __str__(self):
        return f"{" "*4}class <Node> data: {self.data}"


class Stack:
    """
    Основной класс стэка
    """
    def __init__(self):
        self.end = None

    def pop(self):
        """
         Возвращение последнего элемента из списка с удалением
        :return: Node
        """
        if self.end is not None:
            last_node = self.end
            self.end = last_node.pref
            return last_node
        else:
            return None

    def push(self, val):
        """
        Добавление элемента в конец списка
        """
        if self.end is not None:
            new_node = Node(val)
            new_node.pref, self.end = self.end, new_node
        else:
            self.end = Node(val)

    def print(self):
        """
        Вывод на печать содержимого стека
        """
        node = self.end
        print("Stack elements:")
        while node is not None:
            print(f"{node}")
            node = node.pref

if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(100)
    stack.push(500)
    stack.push("AAAAA")
    stack.print()
    n = stack.pop()
    print(f"Вынут элемент: {n}")
    stack.print()
