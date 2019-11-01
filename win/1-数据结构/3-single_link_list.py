# coding:"utf-8"

class Node:
    def __init__(self, elem):
        self.elem = elem
        self.next = None


class singleLinkList:
    """单链表创建"""

    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        """判断是否为空"""
        return self.__head is None

    def length(self):
        """查看链表长度"""
        cur = self.__head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历链表"""
        cur = self.__head
        while cur is not None:
            print(cur.elem, end=" ")
            cur = cur.next
        print("")

    def add(self, item):
        """从头部添加元素"""
        node = Node(item)
        node.next = self.__head
        self.__head = node

    def append(self, item):
        """从尾部添加元素"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next is not None:
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):
        """从pos位置插入item"""
        node = Node(item)
        if pos <= 0:
            self.add(item)
        elif pos > self.length() - 1:
            self.append(item)
        else:
            pre = self.__head
            count = 0
            while count < (pos - 1):
                count += 1
                pre = pre.next
            node.next = pre.next
            pre.next = node

    def remove(self, item):
        """删除链表元素"""
        cur = self.__head
        pre = None
        while cur is not None:
            if cur.elem == item:
                if cur == self.__head:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next

    def search(self, item):
        """查找链表元素"""
        cur = self.__head
        while cur is not None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False


if __name__ == "__main__":
    sll = singleLinkList()
    print(sll.is_empty())
    print(sll.length())

    sll.append(1)
    sll.append(12)
    sll.append(123)

    print(sll.is_empty())
    print(sll.length())
    sll.travel()
    sll.add(0)
    sll.travel()
    sll.insert(3, 5)
    sll.travel()
    sll.remove(5)
    sll.travel()
