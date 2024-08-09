import unittest
from counter.counter import count_less_or_equal_brute_force, count_less_or_equal_numpy


class TestCountLessOrEqual(unittest.TestCase):
    test_cases = {
        "general_case": {
            "equipo_a": [1, 2, 3, 4],
            "equipo_b": [3, 4],
            "expected": [3, 4],
        },
        "no_elements_less_or_equal": {
            "equipo_a": [5, 6, 7],
            "equipo_b": [1, 2, 3],
            "expected": [0, 0, 0],
        },
        "all_elements_less_or_equal": {
            "equipo_a": [1, 2, 3],
            "equipo_b": [3, 3, 3],
            "expected": [3, 3, 3],
        },
        "empty_lists": {
            "equipo_a": [],
            "equipo_b": [],
            "expected": [],
        },
    }

    def test_count_less_or_equal_opt1(self):
        for case_name, case_data in self.test_cases.items():
            with self.subTest(case_name=case_name):
                result = count_less_or_equal_brute_force(case_data["equipo_a"], case_data["equipo_b"])
                self.assertEqual(result, case_data["expected"])

    def test_count_less_or_equal_opt3(self):
        for case_name, case_data in self.test_cases.items():
            with self.subTest(case_name=case_name):
                result = count_less_or_equal_numpy(case_data["equipo_a"], case_data["equipo_b"])
                self.assertEqual(result, case_data["expected"])


if __name__ == '__main__':
    unittest.main()
