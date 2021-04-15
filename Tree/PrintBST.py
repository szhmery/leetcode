
class PrintBST:
    @staticmethod
    def printBST(root) -> None:
        res = []
        if root is None:
            print("Tree is None")
        queue = [root]
        while len(queue) != 0:
            valid_queue = []
            for node in queue:
                if type(node) is str:
                    res.append(node)
                else:
                    res.append(node.val)
                    valid_queue.append(node)

            new_queue = []

            for node in valid_queue:
                if node.left:
                    new_queue.append(node.left)
                else:
                    new_queue.append("Left null")
                if node.right:
                    new_queue.append(node.right)
                else:
                    new_queue.append('Right null')
            queue = new_queue
        print(res)