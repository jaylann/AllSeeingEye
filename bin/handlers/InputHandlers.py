import re


def sanitize_input(input_string):
    # Removes any characters that are not alphanumeric or standard punctuation
    sanitized_input = re.sub(r'[^\w\s.,!?@+-]', '', input_string)
    return sanitized_input.strip()


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
