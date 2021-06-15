# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """

class NestedInteger:
    def __init__(self):
        self.nestedList = []

    def isInteger(self) -> bool:
        """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       """

    def getInteger(self) -> int:
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        """

    def getList(self) -> [NestedInteger]:
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        """


class NestedIterator:
    #    /https://www.bilibili.com/video/BV1Dy4y1x71j?from=search&seid=11319396923938999149
    def __init__(self, nestedList: [NestedInteger]):
        def flatten(ll):
            tmp = []
            for element in ll:
                if element.isInteger():
                    tmp.append(element.getInteger())
                else:
                    tmp.extend(flatten(element.getList()))
            return tmp

        self.queue = flatten(nestedList)

    def next(self) -> int:
        if self.queue:
            return self.queue.pop(0)

    def hasNext(self) -> bool:
        return self.queue

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
