import unittest
from unittest.mock import patch, Mock

from bin.handlers.GPTHandler import GPTHandler
from bin.handlers.objects.GPTResponse import GPTResponse


class TestOpenAIAPI(unittest.TestCase):

    @patch('os.getenv')  # Mock the os.getenv method
    @patch('bin.handlers.ConfigHandler.load_env_vars')  # Mock the load_env_vars method
    def setUp(self, mock_load_env_vars, mock_getenv):
        mock_getenv.return_value = "fake_api_key"
        self.api = GPTHandler()

    def test_load_api_key_success(self):
        self.assertEqual(self.api.api_key, "fake_api_key")

    @patch('os.getenv', return_value=None)  # Mock the os.getenv method to return None
    def test_load_api_key_failure(self, mock_getenv):
        with self.assertRaises(ValueError):
            GPTHandler()

    @patch('tiktoken.get_encoding')
    def test_count_tokens(self, mock_get_encoding):
        mock_encoder = Mock()
        mock_encoder.encode.return_value = [1, 2, 3, 4]
        mock_get_encoding.return_value = mock_encoder
        self.assertEqual(self.api.count_tokens("test text"), 2)

    @patch('openai.ChatCompletion.create')
    def test_generate_text(self, mock_chat_completion):
        mock_response = {
            "id": "chatcmpl-xyz",
            "object": "chat.completion",
            "choices": [{"message": {"role": "assistant", "content": "Hello!"}}],
            "usage": {
                "prompt_tokens": 5,
                "completion_tokens": 10,
                "total_tokens": 15
            }
        }
        mock_chat_completion.return_value = mock_response

        response = self.api.generate_text("Hello, assistant!")
        self.assertIsInstance(response, GPTResponse)
        self.assertEqual(response.id, "chatcmpl-xyz")
        self.assertEqual(response.messages, ["Hello!"])
        self.assertEqual(response.prompt_tokens, 5)
        self.assertEqual(response.completion_tokens, 10)
        self.assertEqual(response.total_tokens, 15)

    @patch('openai.ChatCompletion.create')
    def test_generate_text_with_system_prompt(self, mock_chat_completion):
        mock_response = {
            "id": "chatcmpl-xyz",
            "object": "chat.completion",
            "choices": [{"message": {"role": "assistant", "content": "Hello, user!"}}],
            "usage": {
                "prompt_tokens": 5,
                "completion_tokens": 10,
                "total_tokens": 15
            }
        }
        mock_chat_completion.return_value = mock_response

        response = self.api.generate_text("Hello, assistant!", system_prompt="System: Start")
        self.assertIsInstance(response, GPTResponse)
        self.assertEqual(response.id, "chatcmpl-xyz")
        self.assertEqual(response.messages, ["Hello, user!"])
        self.assertEqual(response.prompt_tokens, 5)
        self.assertEqual(response.completion_tokens, 10)
        self.assertEqual(response.total_tokens, 15)

if __name__ == '__main__':
    unittest.main()
