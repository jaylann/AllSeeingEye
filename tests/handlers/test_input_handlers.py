import unittest

from bin.handlers.InputHandlers import sanitize_input, get_user_input
from unittest.mock import patch

class TestGetUserInput(unittest.TestCase):
    @patch('builtins.input', return_value='  abc  ')
    def test_whitespace_sanitization(self, mock_input):
        result = get_user_input('Enter something')
        self.assertEqual(result, 'abc')  # Expecting sanitized input without whitespace

    @patch('builtins.input', side_effect=['', '', 'abc'])
    def test_multiple_empty_inputs(self, mock_input):
        result = get_user_input('Enter something', required=True)
        self.assertEqual(result, 'abc')

    @patch('builtins.input', return_value='123')
    def test_integer_conversion(self, mock_input):
        result = get_user_input('Enter a number', input_type=int)
        self.assertEqual(result, 123)

    @patch('builtins.input', side_effect=['abc', '123'])
    def test_invalid_integer_conversion(self, mock_input):
        result = get_user_input('Enter a number', input_type=int)
        self.assertEqual(result, 123)

    @patch('builtins.input', return_value='abc!@+-.,?')
    def test_sanitization_with_punctuation(self, mock_input):
        result = get_user_input('Enter something')
        self.assertEqual(result, 'abc!@+-.,?')  # Expecting input with allowed punctuation

    @patch('builtins.input', return_value='')
    def test_optional_input(self, mock_input):
        result = get_user_input('Enter something (optional)')
        self.assertIsNone(result)


class TestSanitizeInput(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(sanitize_input(''), '')

    def test_alphanumeric(self):
        self.assertEqual(sanitize_input('abc123'), 'abc123')

    def test_punctuation(self):
        self.assertEqual(sanitize_input('abc!@+-.,?'), 'abc!@+-.,?')

    def test_whitespace(self):
        self.assertEqual(sanitize_input('  abc  '), 'abc')

    def test_invalid_characters(self):
        self.assertEqual(sanitize_input('abc#$%^'), 'abc')

if __name__ == '__main__':
    unittest.main()
