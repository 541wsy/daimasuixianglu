# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # #单层逻辑：比较left.left和right.right(外侧)；left.right和right.left(里侧)
        # #后序
        # def compare(leftnode, rightnode):
        #     #判断当前左右子树是否对称

        #     if not leftnode and not rightnode:
        #         return True
        #     elif not leftnode or not rightnode:
        #         return False
        #     elif leftnode.val != rightnode.val:
        #         return False
        #     #子树非空，且根节点对称，则继续向下递归
        #     else:
        #         isoutsame = compare(leftnode.left, rightnode.right)
        #         isinsame = compare(leftnode.right, rightnode.left)

        #         return isoutsame and isinsame
        # return compare(root.left, root.right)

        # stack:层序遍历
        ##使用队列成对判断元素是否相等，只要相等出栈
        from collections import deque
        q = deque()
        # 加入左右子树根节点
        q.append(root.left)
        q.append(root.right)

        while q:
            # 关键在于，一次pop需要比较的节点（可以泛化到多个节点需要比较的情况），根据if条件进行判断
            leftroot = q.popleft()
            rightroot = q.popleft()
            # 判断，什么条件可以直接终止判断(成对比较关键步骤)
            if not leftroot and not rightroot:
                continue  # 注意：成对比较时，只有false的条件可以直接break
            elif not leftroot or not rightroot:
                return False
            elif leftroot.val != rightroot.val:
                return False
            else:

                # 进队外侧节点
                outleft = q.append(leftroot.left)
                outright = q.append(rightroot.right)
                # 进队内侧节点
                inleft = q.append(leftroot.right)
                inright = q.append(rightroot.left)
        return True





