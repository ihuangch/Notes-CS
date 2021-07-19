# coding = 'utf-8'

# 题目描述
from typing import List


给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。
请你将两个数相加，并以相同形式返回一个表示和的链表。
你可以假设除了数字 0 之外，这两个数都不会以 0 开头。




class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = curr = ListNode()
        carry = 0

        while carry or l1 or l2:
            val = carry
            if l1: l1, val = l1.next, l1.val + val
            if l2: l2, val = l2.next, l2.val + val

            carry, val = divmod(val, 10)
            curr.next = ListNode(val)
            curr = curr.next
        
        return head.next