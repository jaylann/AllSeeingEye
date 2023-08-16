import os


def get_content_root() -> str:
    """
    Retrieves the project root directory.

    :return: Path to the project root directory.
    """
    # Get the directory of the current file
    current_file_path = os.path.abspath(__file__)
    # Navigate up to the project root (modify as needed for your directory structure)
    project_root = os.path.dirname(os.path.dirname(os.path.dirname(current_file_path)))
    return project_root