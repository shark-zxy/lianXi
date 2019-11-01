class Queue:
    def __init__(self):
        self.__list = []

    def enqueue(self, item):
        self.__list.append(item)
        # 2 self.__list.insert(0,item)

    def deQueue(self):
        return self.__list.pop(0)
        # 2 self.__list.pop()

    def empty(self):
        return self.__list == []

    def size(self):
        return len(self.__list)


# 双端队列
class deQue():
    def __init__(self):
        self.__list = []

    def enQ_front(self, item):
        self.__list.insert(0, item)

    def enQ_reas(self, item):
        self.__list.append(item)

    def deQ_front(self):
        return self.__list.pop()

    def deQ_reas(self):
        return self.__list.pop(0)

    def empty(self):
        return self.__list == []

    def size(self):
        return len(self.__list)


if __name__ == "__main__":
    Q = Queue()
    Q.enqueue(1)
    Q.enqueue(2)
    Q.enqueue(3)
    print(Q.deQueue())
    print(Q.deQueue())
    print(Q.deQueue())

    q = deQue()
    q.enQ_front(1)
    q.enQ_front(2)
    q.enQ_front(3)
    print(q.deQ_front())
    print(q.deQ_front())
    print(q.deQ_front())
