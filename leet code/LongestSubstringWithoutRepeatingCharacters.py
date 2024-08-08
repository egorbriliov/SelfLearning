import unittest


class Solution(object):
    def lengthOfLongestSubstring(self, stroke):
        """
        :type s: str
        :rtype: int
        """
        # Проверка, чтобы строка не была пустой
        # Если не пустая
        if stroke:
            # Создаётся множество
            longest_elements_lens = set()
            # Цикл, который работает, пока длинна строки
            while stroke:
                # Создаётся строка с первым элементом из предыдущей строки
                new_stroke = stroke[0]
                # Индекс повышается на 1, потому что первый элемент уже был добавлен
                index = 1
                # Если длинна строки больше возможного index
                if len(stroke) > index:
                    # Новая строка заполняется, пока следующий элемент ещё не входит в новую строку
                    while stroke[index] not in new_stroke:
                        # Строка дополняется новым символом
                        new_stroke += stroke[index]
                        # Если возможный новый индекс может быть применён к строке
                        if index + 1 < len(stroke):
                            # Устанавливается новый индекс для
                            index += 1
                        # Если возможный новый индекс не может быть применён к строке
                        else:
                            # Добавляется последняя строка
                            longest_elements_lens.add(len(new_stroke))
                            # Цикл строки заканчивается
                            stroke = False
                            # Остановка текущего цикла
                            break
                    # Когда следующий элемент будет входить в строку
                    else:
                        # Добавляется новая длинна строки
                        longest_elements_lens.add(len(new_stroke))
                        # Строка на одну букву
                        stroke = stroke[1:]
                # Если длинна строки равна единице
                elif len(stroke) == index:
                    # В список длин добавляется новая длинна равная единице
                    longest_elements_lens.add(1)
                    # Цикл останавливается
                    break

            # Когда цикл отработал из множества выбирается максимальное значение
            return max(longest_elements_lens)
        # Если строка пустая
        else:
            # Возвращается пустое значение
            return 0


solution = Solution()


class TestMyModule(unittest.TestCase):

    def test_1(self):
        self.assertEqual(solution.lengthOfLongestSubstring("zzz"), 1)

    def test_2(self):
        self.assertEqual(solution.lengthOfLongestSubstring("zzxc"), 3)

    def test_3(self):
        self.assertEqual(solution.lengthOfLongestSubstring("abcabcbb"), 3)

    def test_4(self):
        self.assertEqual(solution.lengthOfLongestSubstring(" "), 1)

    def test_4(self):
        self.assertEqual(solution.lengthOfLongestSubstring("abcabcbb"), 3)

    def test_5(self):
        self.assertEqual(solution.lengthOfLongestSubstring("dvdf"), 3)
