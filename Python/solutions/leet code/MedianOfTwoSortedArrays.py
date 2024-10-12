import unittest


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        new_list = list(sorted(nums1 + nums2))
        if len(new_list) % 2 == 1:
            index = len(new_list) // 2
            return new_list[index]
        else:
            first_index = len(new_list) // 2 - 1
            last_index = len(new_list) // 2
            value = (float(new_list[first_index]) + float(new_list[last_index])) / 2
            return value



solution = Solution()


class TestMyModule(unittest.TestCase):

    def test_1(self):
        self.assertEqual(solution.findMedianSortedArrays(nums1=[1, 2, 3], nums2=[5, 6]), 3)

    def test_2(self):
        self.assertEqual(solution.findMedianSortedArrays(nums1=[1, 2, 3], nums2=[5, 6, 7]), 4)

    def test_3(self):
        self.assertEqual(solution.findMedianSortedArrays(nums1=[1, 2], nums2=[3, 4]), 2)
