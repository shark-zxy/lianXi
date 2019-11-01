#coding :utf-8

class Node:
    def __init__(self,item):
        self.elem = item
        self.lchild = None
        self.rchild = None


class Tree:
    def __init__(self):
        self.root = None

    def add(self, item):
        node = Node(item)
        if self.root is None:
            self.root = node
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            if cur_node.lchild is None:
                cur_node.lchild = node
                return
            else:
                queue.append(cur_node.lchild)
            if cur_node.rchild is None:
                cur_node.rchild = node
                return
            else:
                queue.append(cur_node.rchild)

    def breadth_travel(self):
        """广度优先遍历"""
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.elem, end=" ")
            if cur_node.lchild is not None:
                queue.append(cur_node.lchild)
            if cur_node.rchild is not None:
                queue.append(cur_node.rchild)

    def preorder(self, node):
        if node is None:
            return
        print(node.elem, end=" ")
        self.preorder(node.lchild)
        self.preorder(node.rchild)

    def zhong(self,node):
        if node is None:
            return
        self.preorder(node.lchild)
        print(node.elem, end=" ")
        self.preorder(node.rchild)

    def hou(self,node):
        if node is None:
            return
        self.preorder(node.lchild)
        self.preorder(node.rchild)
        print(node.elem, end=" ")
if __name__ == "__main__":
    tree = Tree()
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.breadth_travel()
    print(" ")
    tree.preorder(tree.root)
    print(" ")
    tree.zhong(tree.root)
    print(" ")
    tree.hou(tree.root)
