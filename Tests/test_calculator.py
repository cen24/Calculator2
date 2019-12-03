import unittest

from Calculator.calculator import calculator
from CSVreader.csvreader import csvreader

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, calculator)

    def test_addition(self):
        test_data = csvreader('Tests/csvdata/UnitTestAddition.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.addition(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)


    def test_subtraction(self):
        test_data = csvreader('Tests/csvdata/UnitTestSubtraction.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.subtraction(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result,result)

    def test_times(self):
        test_data = csvreader('Tests/csvdata/UnitTestMultiplication.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.multiply(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)

    def test_div(self):
        test_data = csvreader('Tests/csvdata/UnitTestDivision.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertAlmostEqual(self.calculator.division(row['Value 1'], row['Value 2']), result)
            self.assertAlmostEqual(self.calculator.result, result)

    def test_square(self):
        test_data = csvreader('Tests/csvdata/UnitTestSquare.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.square_(row['Value 1']), result)
            self.assertEqual(self.calculator.result, result)

    def test_sqrt(self):
        test_data = csvreader('Tests/csvdata/UnitTestSquareRoot.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertAlmostEqual(self.calculator.sqrt_(row['Value 1']), result)
            self.assertAlmostEqual(self.calculator.result, result)

    def test_results_property(self):
        self.assertEqual(self.calculator.result, 0)

if __name__ == '__main__':
    unittest.main()


