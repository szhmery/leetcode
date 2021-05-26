import collections


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    # https://blog.csdn.net/fuxuemingzhu/article/details/79571892
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        ans = []
        def preorder(root):
            if not root:
                ans.append('#')
            while root:
                ans.append(str(root.val))
                preorder(root.left)
                preorder(root.right)


        # def preorder2(root):
        #     ans = []
        #     stack = []
        #     if root is None:
        #         ans.append('#')
        #     node = root
        #     while stack or node:
        #         while node:
        #             ans.append(str(node.val))
        #             stack.append(node)
        #             node = node.left
        #         ans.append("#")
        #         node = stack.pop()
        #         node = node.right
        #     return ans
        # ans = preorder(root)
        preorder(root)
        return ' '.join(ans)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        vals = collections.deque(val for val in data.split())

        def build():
            if vals:
                val = vals.popleft()
                if val == '#':
                    return None
                root = TreeNode(int(val))
                root.left = build()
                root.right = build()
                return root

        return build()



# Your Codec object will be instantiated and called as such:
ser = Codec()
deser = Codec()
ans = deser.deserialize(ser.serialize(root))