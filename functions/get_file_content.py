import os
from .utils import validate_path

MAX_CHARS = 10000


def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        target_path, error = validate_path(working_directory, file_path)
        if error:
            return error
        if not os.path.isfile(target_path):
            return f'Error: "{file_path}" is not a file'
        with open(target_path, "r") as file:
            content = file.read(MAX_CHARS)
            if file.read(1):
                content += (
                    f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
                )
            return content
    except Exception as e:
        return f"Error: something went wrong: {e}"
