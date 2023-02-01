# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 初始化dummyhead
        dummyhead = ListNode()
        dummyhead.next = head

        pred = dummyhead
        curr = head

        while curr:
            if not curr.next:  # 如果curr.next是空，即奇数情况
                pred.next = curr
                return dummyhead.next
            pred.next = curr.next
            newnode = pred.next.next
            pred.next.next = curr

            # 更新指针
            pred = curr
            curr = newnode
        pred.next = curr
        return dummyhead.next

