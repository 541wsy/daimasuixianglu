# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        # dummy head
        dummy_head = ListNode()
        dummy_head.next = head

        # 开始遍历链表，要删除的始终是acurr.next
        curr = dummy_head

        while curr.next:
            if curr.next.val == val:  # 删除curr.next
                curr.next = curr.next.next
            else:
                curr = curr.next
        return dummy_head.next





