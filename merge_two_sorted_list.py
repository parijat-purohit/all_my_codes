"""
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

https://leetcode.com/problems/merge-two-sorted-lists/
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        l1 = []
        l2 = []
        if list1:
            while(list1.next!=None):
                l1.append(list1.val)
                list1 = list1.next
            l1.append(list1.val)


        if list2:
            while(list2.next!=None):
                l2.append(list2.val)
                list2 = list2.next
            l2.append(list2.val)

        
        l3 = sorted(l1+l2)

        head = []
        if len(l3)!=0:
            head = list3 = ListNode()
            for i,l in enumerate(l3):
                list3.val = l
                if(i<len(l3)-1):
                    list3.next = ListNode()
                    list3 = list3.next
            return head 
