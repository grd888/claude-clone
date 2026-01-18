import os
from .utils import validate_path

def write_file(working_directory, file_path, content):
  try:
    target_dir, error = validate_path(working_directory, file_path, "w")
    if error:
        return error
    os.makedirs(os.path.dirname(target_dir), exist_ok=True)
    with open(target_dir, "w") as file:
      file.write(content)
    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
  except Exception as e:
    return f"Error: something went wrong: {e}"