import unittest
import regex_query

class RegexQueryTest(unittest.TestCase):
    def test_valid_regex(self):
        result = regex_query.checkString("Hello! How are you?", "H[\\w]+")
        self.assertEqual(["Hello", "How"], result)  # add assertion here

    def test_invalid_regex(self):
        try:
            regex_query.checkString("wewewe", "[?")
        except Exception as e:
            self.assertEqual("unterminated character set at position 0", str(e))  # add assertion here

    def test_invalid_input(self):
        try:
            regex_query.checkString("", "")
        except Exception as e:
            self.assertEqual("Input string cannot be empty!", str(e))  # add assertion here

if __name__ == '__main__':
    unittest.main()
