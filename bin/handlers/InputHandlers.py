import re
from typing import Any, List


def sanitize_input(input_string):
    # Removes any characters that are not alphanumeric or standard punctuation
    sanitized_input = re.sub(r'[^\w\s.,!?@+-]', '', input_string)
    return sanitized_input.strip()

def validate_input(name: str, value: Any, allowed_types: List[type]) -> None:
    """Validate input types for the given value.

    Args:
        name (str): Name of the variable (for error messaging).
        value (Any): The value to be checked.
        allowed_types (List[type]): A list of allowed types for the value.

    Raises:
        ValueError: If the value is not one of the allowed types.
    """
    if value is not None and not any(isinstance(value, t) for t in allowed_types):
        raise ValueError(f"{name} must be one of the types: {', '.join([str(t) for t in allowed_types])}.")

def get_user_input(prompt, required=False, input_type=str):
    user_input = ''
    while True:
        print("\n" + "-" * 40)
        print(f"{prompt}:")
        print("-" * 40)
        user_input = input("> ")
        user_input = sanitize_input(user_input)

        if not user_input.strip() and not required:
            return None

        if not user_input.strip():
            print("This field is required. Please try again.")
            continue

        try:
            return input_type(user_input)
        except ValueError:
            print(f"Invalid input. Please enter a value of type {input_type.__name__}.")
