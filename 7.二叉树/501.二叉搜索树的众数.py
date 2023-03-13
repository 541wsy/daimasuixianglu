# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        # 中序遍历，双指针
        pre = None
        # 当前最大count_
        # 当前遍历节点的count：tmp_count
        # pre.val == node.val:tmp_count +=1，if tmp_count > count_:count_ = tmp_count
        count_ = 1
        tmp_count = 1
        result = []  # 结果集，只要有更大的count_,result清空

        def traversal(node):
            nonlocal pre
            nonlocal count_
            nonlocal tmp_count
            nonlocal result

            if not node:
                return

            traversal(node.left)

            if pre:
                # 计数当前频率
                if pre.val == node.val:  # 相等，计数+1
                    tmp_count += 1
                else:  # 不等：清零
                    tmp_count = 1

                # 更新count_
                if tmp_count == count_:
                    result.append(node.val)
                elif tmp_count > count_:
                    result = [node.val]
                    count_ = tmp_count
            # 将第一个数加入result
            else:
                result.append(node.val)
            # 移动指针
            pre = node

            traversal(node.right)

        traversal(root)
        return result






