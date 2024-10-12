# # Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def convert_to_number(list_node):
            list_like_number = []
            while list_node:
                list_like_number.append(list_node.val)
                list_node = list_node.next
            return int("".join(map(str, list_like_number)))

        def convert_to_list_node(number):
            stroke_number = list(reversed(str(number)))
            head = ListNode(stroke_number[0])
            current = head
            for val in stroke_number[1:]:
                current.next = ListNode(int(val))
                current = current.next
            return head

        return convert_to_list_node(convert_to_number(l1) + convert_to_number(l2))