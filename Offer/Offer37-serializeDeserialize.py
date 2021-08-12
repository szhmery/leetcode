import collections
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    # 为完整表示二叉树，考虑将叶节点下的 null 也记录。在此基础上，对于列表中任意某节点 node ，
    # 其左子节点 node.left 和右子节点 node.right 在序列中的位置都是 唯一确定 的。
    # 设 m 为列表区间 [0,n] 中的 null 节点个数，则可总结出根节点、左子节点、右子节点的列表索引的递推公式
    # n是node的index， node.left = 2*(n - m) + 1,node.right = 2*(n - m) + 2
    def serialize(self, root):
        if not root:
            return "[]"
        queue = collections.deque()
        queue.append(root)
        res = []
        while queue:
            node = queue.popleft()
            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append("null")
        return '[' + ','.join(res) + ']'

    def deserialize(self, data):
        if data == "[]":
            return
        vals, i = data[1:-1].split(','), 1 #除去前后[],用,来split
        root = TreeNode(int(vals[0]))
        queue = collections.deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if vals[i] != "null":
                node.left = TreeNode(int(vals[i]))
                queue.append(node.left)
            i += 1
            if vals[i] != "null":
                node.right = TreeNode(int(vals[i]))
                queue.append(node.right)
            i += 1
        return root

