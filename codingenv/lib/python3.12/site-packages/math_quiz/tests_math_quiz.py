import unittest
from math_quiz import generate_random_integer, choose_random_operator, generate_problem


class TestMathGame(unittest.TestCase):

    def test_generate_random_integer(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generate_random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_choose_random_operator(self):
        for _ in range(1000):
            operator = choose_random_operator()
            self.assertIn(operator, ["+", "-", "*"])
        pass

    def test_generate_problem(self):
        test_cases = [(5, 2, "+", "5 + 2", 7), (4, 6, "-", "4 - 6", -2),
                      (5, 5, "*", "5 * 5", 25), (10, 20, "+", "10 + 20", 30), (-7, -7, "*", "-7 * -7)", 49)]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, solution = generate_problem(num1, num2, operator)
            self.assertEqual(problem, expected_problem)
            self.assertEqual(solution, expected_answer)
            pass


if __name__ == "__main__":
    unittest.main()
