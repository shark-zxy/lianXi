# coding :"utf-8"
class Node:
    def __init__(self, elem):
        self.elem = elem
        self.next = None


class singleLink:
    def __init__(self, node=None):
        self.__head = node
        if node:
            node.next = self.__head

    def is_empty(self):
        return self.__head is None

    def length(self):
        if self.is_empty():
            return 0
        cur = self.__head
        count = 1
        while cur.next is not self.__head:
            count += 1
            cur = cur.next
        return count
        # """cur.next指向self.__head时，不进入循环，即会漏掉最后一个节点"""

    def travel(self):
        if self.is_empty():
            return
        cur = self.__head
        while cur.next is not self.__head:
            print(cur.elem, end=" ")
            cur = cur.next
        print(cur.elem)
        # 就像上面得原因一样，遍历到最后一个节点得时候停止打印，所以最后添加上

    def add(self, item):
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next is not self.__head:
                cur = cur.next
            node.next = self.__head
            self.__head = node
            cur.next = self.__head

    def append(self, item):
        node = Node(item)
        if self.__head is None:
            self.__head = node
            node.next = self.__head
        else:
            cur = self.__head
            while cur.next is not self.__head:
                cur = cur.next
            node.next = self.__head
            cur.next = node

    def insert(self, pos, item):
        """pre是指前一个节点，cur是指当前节点"""
        node = Node(item)
        if pos <= 0:
            self.add(item)
        elif pos > self.length():
            self.append(item)
        else:
            pre = self.__head
            count = 0
            while count < (pos - 1):
                count += 1
                pre = pre.next
            node.next = pre.next
            pre.next = node

    def search(self, item):
        if self.is_empty():
            return False
        cur = self.__head
        while cur.next is not self.__head:
            if cur.elem is item:
                return True
            else:
                cur = cur.next
        if cur.elem is item:
            return True
        return False

    def remove(self, item):
        if self.is_empty():
            return
        cur = self.__head
        pre = None
        while cur.next is not self.__head:
            if cur.elem == item:
                # 判断是否是头节点
                if cur == self.__head:
                    # 寻找尾节点
                    rear = self.__head
                    while rear.next is not self.__head:
                        rear = rear.next
                    self.__head = cur.next
                    rear.next = self.__head
                else:
                    pre.next = cur.next
                return
            else:
                pre = cur
                cur = cur.next
        if cur.elem is item:
            if cur is self.__head:
                self.__head = None
            else:
                pre.next = cur.next


if __name__ == "__main__":
    """单向循环链表"""
    ll = singleLink()
    print(ll.is_empty())
    ll.append(2)
    ll.travel()
    ll.add(1)
    ll.travel()
    print(ll.length())
    ll.insert(1, 3)
    ll.travel()
    ll.remove(1)
    ll.travel()
    print(ll.search(1))

"""
def remove(self,item):
    if self.is_empty():
        return 
    cur = self.__head
    pre = None
    while cur.next is not self.__head:
        if cur.elem is item:
            if cur is self.__head:
                rear = self.__head
                while rear.next is not self.__head:
                    rear = rear.next
                self.__head = cur.next
                rear.next = self.__head
            else:
                pre.next = cur.next
            return 
        else:
            pre = cur
            cur = cur.next
    if cur.elem is item:
        if cur is self.__head:
            self.__head = None
        else:
            pre.next = cur.next
"""
