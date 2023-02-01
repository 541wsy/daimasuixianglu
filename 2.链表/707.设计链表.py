class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList(object):

    def __init__(self):
        # 此处的head是dummyhead
        self.head = ListNode()
        self.size = 0

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        # 判定索引有效性
        if index < 0 or index > self.size - 1:
            return -1
        # 定义一个指针遍历链表
        curr = self.head.next
        for _ in range(index):
            curr = curr.next
        return curr.val

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        # 定义新节点
        newnode = ListNode(val=val)
        # 增加节点
        newnode.next = self.head.next
        self.head.next = newnode
        self.size += 1

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        newnode = ListNode(val=val)

        # 定义遍历链表指针
        curr = self.head
        while curr.next:  # 跳出循环时curr是最后一个节点
            curr = curr.next
        curr.next = newnode
        self.size += 1

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        # 特殊情况处理
        if index > self.size:
            return
        if index < 0:
            return self.addAtHead(val)
        if index == self.size:
            return self.addAtTail(val)

        # 一般情况
        newnode = ListNode(val=val)
        curr = self.head
        for _ in range(index):
            curr = curr.next
        newnode.next = curr.next
        curr.next = newnode
        self.size += 1

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index < 0 or index > self.size - 1:
            return
        curr = self.head
        for _ in range(index):
            curr = curr.next
        # 当跳出循环则curr.next是删除目标
        curr.next = curr.next.next
        self.size -= 1
    def print_linklist(self):
        result = []
        curr = self.head.next
        while curr.next: #当curr不是最后一个
            result.append(curr.val)
            curr = curr.next
        result.append(curr.val)
        print(result)


# Your MyLinkedList object will be instantiated and called as such:
linklist = MyLinkedList()
linklist.addAtHead(7)
linklist.addAtHead(2)
linklist.addAtHead(1)
linklist.addAtIndex(3,0)
linklist.deleteAtIndex(2)
linklist.addAtHead(6)
linklist.addAtTail(4)
linklist.get(4)
