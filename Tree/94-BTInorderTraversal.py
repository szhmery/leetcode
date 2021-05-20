from Tree.PrintBST import PrintBST


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root: 'TreeNode') -> 'List[int]':
        """利用堆栈实现树的中序遍历"""
        result = []
        if root is None:
            return result
        myStack = []
        node = root
        while node or myStack:
            while node:  # 从根节点开始，一直找它的左子树
                myStack.append(node)
                node = node.left
            node = myStack.pop()  # while结束表示当前节点node为空，即前一个节点没有左子树了
            result.append(node.val)
            node = node.right  # 开始查看它的右子树
        return result

    def inorderTraversal2(self, root: 'TreeNode') -> 'List[int]':
        def inorderTraversal_recursion(root: 'TreeNode') -> 'List[int]':
            if root is None:
                return

            inorderTraversal_recursion(root.left)
            ans.append(root.val)
            inorderTraversal_recursion(root.right)
            return
        ans = []
        inorderTraversal_recursion(root)
        return ans


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(5)
    a = TreeNode(4)
    root.right = a
    a.left = TreeNode(3)
    a.right = TreeNode(6)

    PrintBST.printBST(root)
    solution = Solution()
    result = solution.inorderTraversal(root)
    print('Inorder BT:{}'.format(result))
    result = solution.inorderTraversal2(root)
    print('Inorder BT:{}'.format(result))