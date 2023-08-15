import dotenv

def load_env_vars(env_file_path: str):
    """Load all environment variables from the specified .env file."""
    dotenv.load_dotenv(env_file_path)
