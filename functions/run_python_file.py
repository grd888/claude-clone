import os
import subprocess
from .utils import validate_path
from google.genai import types

def run_python_file(working_directory, file_path, args=None):
    try:
        target_dir, error = validate_path(working_directory, file_path, "x")
        if error:
            return error
        if not os.path.isfile(target_dir):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if not target_dir.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'

        abs_working_dir = os.path.abspath(working_directory)
        abs_file_path = os.path.normpath(os.path.join(abs_working_dir, file_path))
        command = ["python", abs_file_path]
        if args:
            command.extend(args)

        result = subprocess.run(command, capture_output=True, timeout=30.0, text=True)
        if result.returncode != 0:
            return f"Error: Process exited with code {result.returncode}"
        if not result.stdout and not result.stderr:
            return "No output produced"
        output_str = ""
        if result.stdout:
            output_str += f"STDOUT: {result.stdout}\n"
        if result.stderr:
            output_str += f"STDERR: {result.stderr}\n"

        return output_str

    except Exception as e:
        return f"Error: executing Python file: {e}"


schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs the specified python file in file_path, relative to the current directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file, relative to the working directory",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(
                    type=types.Type.STRING,
                ),
                description="Arguments to pass to the Python file",
            )
        },
        required=["file_path"]
    ),
)