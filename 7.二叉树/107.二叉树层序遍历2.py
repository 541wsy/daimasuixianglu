# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # cur和栈记录遍历顺序
        # 只要遇到空节点，就从栈顶弹出一个元素
        if not root:
            return []
        result = []
        stack = []
        cur = root
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:  # 当遍历到空节点，从栈弹出节点，放到result
                node = stack.pop()
                result.append(node.val)
                cur = node.right
        return result

        # 递归法
        # result = []
        # def traversal(cur):
        #     if not cur:
        #         return
        #     #要一直先往左搜索，先递归左
        #     traversal(cur.left)
        #     result.append(cur.val)
        #     traversal(cur.right)
        # traversal(root)
        # return result

