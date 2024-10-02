from unittest import TestCase, main
from lab_1 import gauss_determinant


class FieldFillingTest(TestCase):
    def test_gauss_determinant(self):
        test_matrix = [
            [8.3, 3.04, 4.1, 1.9],
            [3.92, 8.45, 7.36, 2.46],
            [3.77, 7.63, 8.04, 2.28],
            [2.21, 3.23, 1.69, 6.69],
        ]

        result = gauss_determinant(test_matrix)
        potencial_result = 444.065

        self.assertTrue(result, potencial_result)


if __name__ == "__main__":
    main()
