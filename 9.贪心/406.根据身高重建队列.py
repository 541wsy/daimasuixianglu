class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        #people先按身高排序
        people.sort(key = lambda x: (-x[0], x[1])) #优先按第一维降序，再按第二维升序

        que = []
        #按照第二维度插入
        for peo in people:
            que.insert(peo[1], peo)
        return que
        #两个维度，先保证一个维度，让身高降序，这样能保证前面的人身高大于等于当前遍历的people
        #这样在做插入的时候，并不会影响已经遍历过节点结果的正确性