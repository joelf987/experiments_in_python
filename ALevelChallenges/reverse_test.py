import unittest
import reverse

class MyTestCase(unittest.TestCase):
    def test_should_reverse_string(self):
        text = "hello there!"
        result = reverse.reverse(text)
        self.assertEqual(result, "!ereht olleh")  # add assertion here


if __name__ == '__main__':
    unittest.main()
