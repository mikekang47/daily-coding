import sys


class Node:
    def __int__(self):
        self.value = None
        self.left = None
        self.right = None


def postorder(n: Node):
    global poststr
    if n:
        if n.left != ".":
            postorder(dic[n.left])
        if n.right != ".":
            postorder(dic[n.right])
        poststr += n.value

def inorder(n: Node):
    global instr
    if n:

        if n.left != ".":
            inorder(dic[n.left])
        instr += n.value
        if n.right != ".":
            inorder(dic[n.right])

def preorder(n: Node):
    global prestr
    if n:
        prestr += n.value
        if n.left != ".":
            preorder(dic[n.left])
        if n.right != ".":
            preorder(dic[n.right])

input = sys.stdin.readline
dic = {}
st = []
n = int(input())
for _ in range(n):
    a, b, c = map(str, input().split())
    node = Node()
    node.value = a
    node.left = b
    node.right = c
    dic[node.value] = node
    if len(st) == 0:
        st.append(node)

instr = ""
poststr = ""
prestr = ""


n = st.pop()
preorder(n)
postorder(n)
inorder(n)
print(prestr)
print(instr)
print(poststr)
