import unittest


def factorize(x):
    """
    Factorize positive integer and return its factors.
    :type x: int,>=0
    :rtype: tuple[N],N>0
    """
    pass


class TestFactorize(unittest.TestCase):
    def test_wrong_types_raise_exception(self):
        """ аргументы типа float или str вызывают исключение TypeError """
        cases = ['string', 1.5]
        for case in cases:
            with self.subTest(x=case):
                self.assertRaises(TypeError, factorize, case)

    def test_negative(self):
        """ отрицательные числа вызывают исключение ValueError """
        cases = [-1, -10, -100]
        for case in cases:
            with self.subTest(x=case):
                self.assertRaises(ValueError, factorize, case)

    def test_zero_and_one_cases(self):
        """ для простых чисел возвращается кортеж, содержащий одно данное число """
        cases = [0, 1]
        for case in cases:
            with self.subTest(x=case):
                self.assertEqual(factorize(case), (case,))

    def test_simple_numbers(self):
        """ числа для которых функция factorize возвращает кортеж размером 2 """
        cases = [3, 13, 29]
        for case in cases:
            with self.subTest(x=case):
                self.assertEqual(factorize(case), (case, ))

    def test_two_simple_multipliers(self):
        """ числа для которых функция factorize возвращает кортеж размером 2 """
        cases = {
            6: (2, 3),
            26: (2, 13),
            121: (11, 11)
        }
        for case, result in cases.items():
            with self.subTest(x=case):
                self.assertEqual(factorize(case), result)

    def test_many_multipliers(self):
        """ числа для которых функция factorize возвращает кортеж размером >2 """
        cases = {
            1001: (7, 11, 13),
            9699690: (2, 3, 5, 7, 11, 13, 17, 19)
        }
        for case, result in cases.items():
            with self.subTest(x=case):
                self.assertEqual(factorize(case), result)
