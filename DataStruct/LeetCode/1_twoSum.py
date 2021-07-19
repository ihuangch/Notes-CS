# coding='utf-8'

# 题目描述
""" 
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
你可以按任意顺序返回答案。
输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
"""

from typing import List


class Solution:
    # 暴力破解版本
    # 时间复杂度 O(n^2)
    # 空间复杂度 O(1)
    def twoSum_1(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    return [i, j]

    # Hash表的方法是通过 list的值作为dict的key, list的索引作为dict的value, 因为字典中的key需要唯一， 所以通过判断 target - num 是否是字典的key
    # 来确定是否匹配, 如果匹配则return
    # 时间复杂度 O(n)
    # 空间复杂度 O(n)
    # 牺牲了时间换空间
    def twoSum_2(self, nums: List[int], target: int) -> List[int]:
        hashtable = dict()
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable[nums[i]] = i
        return []
    


