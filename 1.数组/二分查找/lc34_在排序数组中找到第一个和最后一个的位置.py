'''
题目描述：
    给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。

    如果数组中不存在目标值 target，返回 [-1, -1]。

    你必须设计并实现时间复杂度为 O(log n) 的算法解决此问题。



示例 1：

输入：nums = [5,7,7,8,8,10], target = 8
输出：[3,4]
示例 2：

输入：nums = [5,7,7,8,8,10], target = 6
输出：[-1,-1]
示例 3：

输入：nums = [], target = 0
输出：[-1,-1]
'''


class Solution:
    def searchRange(self, nums, target):

        def get_left_border(nums, target):
            left = 0
            right = len(nums) - 1
            leftborder = -2 #使用一个变量来存储左边界的赋值状态
            while left <= right:
                mid = (left + right) // 2
                if target <= nums[mid]:
                    right = mid - 1
                    leftborder = right
                else:
                    left = mid + 1
            return leftborder

        def get_right_border(nums, target):
            left = 0
            right = len(nums) - 1
            rightborder = -2
            while left <= right:
                mid = (left + right) // 2
                if target >= nums[mid]:
                    left = mid + 1
                    rightborder = left
                else:
                    right = mid - 1
            return rightborder

        rightborder = get_right_border(nums, target)
        leftborder = get_left_border(nums, target)

        #case1：target不在nums，并且排序在nums两端，rightborder,leftborder一定有一个不会被赋值
        if rightborder == -2 or leftborder == -2:
            return [-1, -1]
        #case2:target在nums取值范围内，但不在nums中
        ##此时等价于没有等于这一项，其实就等价于普通的二分法查找，此时leftborder和rightborder位置一定差1
        if rightborder - leftborder == 1:
            return [-1, -1]

        else:
            return [leftborder + 1, rightborder - 1]

if __name__ == '__main__':
    nums = [5,7,7,8,8,10]
    target = 8
    solution = Solution()
    result = solution.searchRange(nums,target)