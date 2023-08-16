import unittest
from bin.handlers.objects.GPTModels import Model
from bin.handlers.objects.GPTModelsCost import ModelCost
from bin.handlers.objects.GPTResponse import GPTResponse


class TestGPTResponse(unittest.TestCase):

    def setUp(self):
        self.sample_data = {
            "id": "<PLACEHOLDER_ID>",
            "object": "chat.completion",
            "created": 1692183013,
            "model": "gpt-3.5-turbo-0613",
            "choices": [
                {
                    "index": 0,
                    "message": {
                        "role": "assistant",
                        "content": "<PLACEHOLDER_MESSAGE_1>"
                    },
                    "finish_reason": "stop"
                },
                {
                    "index": 1,
                    "message": {
                        "role": "assistant",
                        "content": "<PLACEHOLDER_MESSAGE_2>"
                    },
                    "finish_reason": "stop"
                }
            ],
            "usage": {
                "prompt_tokens": 291,
                "completion_tokens": 111,
                "total_tokens": 402
            }
        }
        self.gpt_response = GPTResponse.from_dict(self.sample_data, "Sample Prompt", "Sample System Prompt")

    def test_from_dict(self):
        self.assertEqual(self.gpt_response.id, "<PLACEHOLDER_ID>")
        self.assertEqual(self.gpt_response.object, "chat.completion")
        self.assertEqual(self.gpt_response.created, 1692183013)
        self.assertEqual(self.gpt_response.model, "gpt-3.5-turbo-0613")
        self.assertEqual(self.gpt_response.messages, ["<PLACEHOLDER_MESSAGE_1>", "<PLACEHOLDER_MESSAGE_2>"])
        self.assertEqual(self.gpt_response.prompt_tokens, 291)
        self.assertEqual(self.gpt_response.completion_tokens, 111)
        self.assertEqual(self.gpt_response.total_tokens, 402)
        self.assertEqual(self.gpt_response.prompt, "Sample Prompt")
        self.assertEqual(self.gpt_response.system_prompt, "Sample System Prompt")

    def test_cost_calculation(self):
        # Using the sample data, the cost should be calculated based on the model and tokens used
        expected_cost = ((291 * ModelCost.GPT3_5_TURBO_4K_INPUT.value) +
                         (111 * ModelCost.GPT3_5_TURBO_4K_OUTPUT.value)) / 1000
        self.assertEqual(self.gpt_response.cost, expected_cost)

    def test_setters(self):
        self.gpt_response.id = "new_id"
        self.assertEqual(self.gpt_response.id, "new_id")

        self.gpt_response.object = "new_object"
        self.assertEqual(self.gpt_response.object, "new_object")

        self.gpt_response.created = 1629300000
        self.assertEqual(self.gpt_response.created, 1629300000)

        self.gpt_response.model = Model.GPT4_0613.value
        self.assertEqual(self.gpt_response.model, Model.GPT4_0613.value)

        self.gpt_response.messages = ["New", "Messages"]
        self.assertEqual(self.gpt_response.messages, ["New", "Messages"])

        self.gpt_response.prompt_tokens = 10
        self.assertEqual(self.gpt_response.prompt_tokens, 10)

        self.gpt_response.completion_tokens = 20
        self.assertEqual(self.gpt_response.completion_tokens, 20)

        self.gpt_response.total_tokens = 30
        self.assertEqual(self.gpt_response.total_tokens, 30)

        self.gpt_response.prompt = "New Prompt"
        self.assertEqual(self.gpt_response.prompt, "New Prompt")

        self.gpt_response.system_prompt = "New System Prompt"
        self.assertEqual(self.gpt_response.system_prompt, "New System Prompt")

    def test_invalid_model_cost(self):
        # Test for a model that doesn't exist in the model_costs dictionary
        self.gpt_response.model = "non_existent_model"
        self.assertEqual(self.gpt_response.cost, 0)