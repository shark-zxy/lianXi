

# class Node():
#     def __init__(self, item):
#         self.lchild = None
#         self.rchild = None
#         self.elem = item
#
#
# class Tree():
#     def __init__(self):
#         self.root = None
#
#     def add(self, item):
#         node = Node(item)
#         if self.root is None:
#             self.root = node
#             return
#         queue = [self.root]
#
#         while queue:
#             child_node = queue.pop(0)
#             if child_node.lchild is None:
#                 child_node.lchild = node
#                 return
#             else:
#                 queue.append(child_node.lchild)
#
#             if child_node.rchild is None:
#                 child_node.rchild = node
#                 return
#             else:
#                 queue.append(child_node.rchild)
#
#     def breath_travel(self):
#         if self.root is None:
#             return
#         queue = [self.root]
#         while queue:
#             cur_node = queue.pop(0)
#             print(cur_node.elem, end= " ")
#             if cur_node.lchild is not None:
#                 queue.append(cur_node.lchild)
#             if cur_node.rchild is not None:
#                 queue.append(cur_node.rchild)
#
#     def preorder(self, node):
#         if node is None:
#             return
#         print(node.elem, end=" ")
#         self.preorder(node.lchild)
#         self.preorder(node.rchild)
#
#
# if __name__ == "__main__":
#     tree = Tree()
#     tree.add(1)
#     tree.add(2)
#     tree.add(3)
#     tree.add(4)
#     tree.add(5)
#     tree.add(6)
#     tree.add(7)
#     print("_"*50)
#     tree.breath_travel()
#     print(" ")
#     print("+"*50)
#     tree.preorder(tree.root)

# class Node():
#     def __init__(self, item):
#         self.lchild = None
#         self.rchild = None
#         self.elem = item
#
#
# class Tree():
#     def __init__(self):
#         self.root = None
#
#     def add(self, item):
#         node = Node(item)
#         if self.root is None:
#             self.root = node
#             return
#         queue = [self.root]
#
#         while queue:
#             cur_node = queue.pop(0)
#             if cur_node.lchild is None:
#                 cur_node.lchild = node
#                 return
#             else:
#                 queue.append(cur_node.lchild)
#             if cur_node.rchild is None:
#                 cur_node.rchild = node
#                 return
#             else:
#                 queue.append(cur_node.rchild)
#
#     def breath_travel(self):
#         if self.root is None:
#             return
#         queue = [self.root]
#
#         while queue:
#             cur_node = queue.pop(0)
#             print(cur_node.elem, end=" ")
#             if cur_node.lchild is not None:
#                 queue.append(cur_node.lchild)
#             if cur_node.rchild is not None:
#                 queue.append(cur_node.rchild)
#
#     def preorder(self, node):
#         if node is None:
#             return
#
#         print(node.elem, end=" ")
#         self.preorder(node.lchild)
#         self.preorder(node.rchild)
#
#     def zhong(self, node):
#         if node is None:
#             return
#
#         self.preorder(node.lchild)
#         print(node.elem, end=" ")
#         self.preorder(node.rchild)
#
#     def hou(self, node):
#         if node is None:
#             return
#
#         self.preorder(node.lchild)
#         self.preorder(node.rchild)
#         print(node.elem, end=" ")
#
#
# if __name__ == "__main__":
#     tree = Tree()
#     tree.add(1)
#     tree.add(2)
#     tree.add(3)
#     tree.add(4)
#     tree.add(5)
#     tree.add(6)
#     tree.add(7)
#     tree.breath_travel()
#     print(" ")
#     tree.preorder(tree.root)
#     print(" ")
#     tree.zhong(tree.root)
#     print(" ")
#     tree.hou(tree.root)

import queue


def bfs(gra, sta):
    viv = set()
    g = queue.Queue()
    g.put(sta)

    while not g.empty():
        v = g.get()
        print(v)
        for i in gra.get(v, []):
            if i not in viv:
                viv.add(i)
                g.put(i)


graph = {1: [4, 2], 2: [3, 4], 3: [4], 4: [5]}
bfs(graph, 1)

(a, b) = [1, 0]
print(graph[a][b])


def dfs(adj, start):
    vivisted = set()
    stack = [[start, 0]]
    while stack:
        (v, child_next_idx) = stack[-1]
        if (v not in adj) or (child_next_idx >= len(adj[v])):
            stack.pop()
            continue
        next_child = adj[v][child_next_idx]
        stack[-1][1] += 1
        if next_child in vivisted:
            continue
        print(next_child)
        vivisted.add(next_child)
        stack.append([next_child, 0])


graph = {1: [4, 2], 2: [3, 4], 3: [4], 4: [5]}
dfs(graph, 1)
