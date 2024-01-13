import unittest
import converter


class MyTestCase(unittest.TestCase):
    def test_should_convert_10(self):
        testNum = 10
        result = converter.convertToHex(testNum)
        assert result == "A"

    def test_should_convert_a_bigger_number_correctly(self):
        testNum = 234857623
        result = converter.convertToHex(testNum)
        assert result == "DFFA497"


if __name__ == '__main__':
    unittest.main()
