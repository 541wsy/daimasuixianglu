# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ##双指针法
        ##此处初始化注意，pred从None开始，否则head.next不是空，链表会死循环
        pred = None
        curr = head

        while curr:
            nextnode = curr.next  # 先把下一个节点记住，否则翻转后找不到这个节点
            curr.next = pred  # 翻转
            # 进行下一步遍历
            pred = curr
            curr = nextnode
        return pred

        ##递归法
        # def reverse(curr, pred):
        #     if not curr: #当curr为空
        #         return pred
        #     nextnode = curr.next
        #     #翻转
        #     curr.next = pred
        #     ##递归，进入下一层
        #     return reverse(nextnode, curr) #此处注意调用自身要return
        # return reverse(head, None)




