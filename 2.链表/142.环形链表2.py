# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        '''
        如果链表有环，最多size步返回自身。
        从头节点开始循环，找到第一个size步能返回自身的节点即为入环点
        '''

        # 1. 循环计算链表长度
        cur = head
        size = 0
        while cur:
            cur = cur.next
            size += 1

        cur = head
        # 2. 从头节点开始循环, cur记录外层循环指针，loop记录内层寻找环的指针
        for ind in range(size):
            loop = cur
            for _ in range(size):
                loop = loop.next
                if loop == cur:
                    return ind
            cur = cur.next
        # 如果找不到
        return None

head = ListNode(3)
node1 = ListNode(2)
node2 = ListNode(0)
node3 = ListNode(4)

head.next = node1
node1.next = node2
node2.next = node3
node3.next = node1

solution = Solution()
result = solution.detectCycle(head)