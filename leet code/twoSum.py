import unittest


class Solution(object):
    def twoSum(self, nums, target):
        """
        :param nums: list[числа]
        :param target: int
        :return: list with index elements which gives sum equal to target
        """
        def search(new_list, target, nums):
            """
            :param new_list: list - where will be find numbers
            :param target: int - sum of numbers
            :param nums: list
            :return: list with index elements which gives sum equal to target
            """
            if len(new_list) > 1:
                first_number = new_list.pop(0)
                for number in new_list:
                    if first_number + number == target:
                        return [nums.index(first_number), nums.index(number, nums.index(first_number) + 1)]
                        # Этот return завершает функцию search()
                return search(new_list, target, nums)
        # Получается копия списка, для поиска индексов файлов
        main_nums = nums[:]
        return search(nums, target, main_nums)

solution = Solution()


class TestMyModule(unittest.TestCase):

    def test_1(self):
        # Arrange
        nums = [1, 2, 3]
        sum_of_numbers = 3
        # Act
        actual_output = solution.twoSum(nums, sum_of_numbers)
        # Assert
        self.assertEqual(actual_output, [0, 1])

    def test_2(self):
        # Arrange
        nums = [1, 2, 3, 6]
        sum_of_numbers = 7
        # Act
        actual_output = solution.twoSum(nums, sum_of_numbers)
        # Assert
        self.assertEqual(actual_output, [0, 3])

    def test_3(self):
        # Arrange
        nums = [1, 4, 4, 6]
        sum_of_numbers = 8
        # Act
        actual_output = solution.twoSum(nums, sum_of_numbers)
        # Assert
        self.assertEqual(actual_output, [1, 2])

    def test_4(self):
        # Arrange
        nums = [1, 3, 5, 6]
        sum_of_numbers = 4
        # Act
        actual_output = solution.twoSum(nums, sum_of_numbers)
        # Assert
        self.assertEqual(actual_output, [0, 1])

    def test_5(self):
        # Arrange
        nums = [1, 3, 5, 6]
        sum_of_numbers = 11
        # Act
        actual_output = solution.twoSum(nums, sum_of_numbers)
        # Assert
        self.assertEqual(actual_output, [2, 3])
