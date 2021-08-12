class Solution:
    #时间复杂度 O(N)： 每次调用 recur(i,j) 减去一个根节点，因此递归占用 O(N)O(N) ；最差情况下（即当树退化为链表），每轮递归都需遍历树所有节点，占用 O(N)O(N) 。
    #空间复杂度 O(N) ： 最差情况下（即当树退化为链表），递归深度将达到 N 。

    def verifyPostorder(self, postorder: [int]) -> bool:
        def recur(i, j):
            if i >= j:
                return True
            p = i
            while postorder[p] < postorder[j]: # postorder[j]为root，找到左半边所有小于root的数组作为左子树
                p += 1
            m = p
            while postorder[p] > postorder[j]: #找到右半边所有大于root的数组作为右子树
                p += 1
            # p是否为j判断右半边数列是否都大于root
            return p == j and recur(i, m - 1) and recur(m, j - 1)

        return recur(0, len(postorder) - 1)

