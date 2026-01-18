import os
from google.genai import types
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
  
schema_write_file = types.FunctionDeclaration(
  name="write_file",
  description="Reads a file in the specified path relative to the working directory and returns its contents as a string",
  parameters=types.Schema(
      type=types.Type.OBJECT,
      properties={
          "file_path": types.Schema(
              type=types.Type.STRING,
              description="Path to the file, relative to the working directory",
          ),
          "content": types.Schema(
              type=types.Type.STRING,
              description="Text that is to be written to the file.",
          ),
      },
      required=["file_path", "content"],
  ),
)