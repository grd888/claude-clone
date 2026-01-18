import os
from .utils import validate_path


def get_files_info(working_directory, directory="."):
    try:
        target_dir, error = validate_path(working_directory, directory)
        if error:
            return error
        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'
        files_info = []
        for filename in os.listdir(target_dir):
            filepath = os.path.join(target_dir, filename)
            is_dir = os.path.isdir(filepath)
            file_size = os.path.getsize(filepath)
            files_info.append(
                f"- {filename}: file_size={file_size} bytes, is_dir={is_dir}"
            )
        return "\n".join(files_info)
    except Exception as e:
        return f"Error listing files: {e}"
