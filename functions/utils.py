import os
from typing import Tuple, Optional


def validate_path(
    working_directory: str, path: str, mode: str = "r"
) -> Tuple[Optional[str], Optional[str]]:
    """
    Validates that a path is within the working directory.
    Returns a tuple of (absolute_target_path, error_message).
    If validation fails, absolute_target_path is None and error_message is set.
    """
    try:
        abs_working_dir = os.path.abspath(working_directory)
        target_path = os.path.normpath(os.path.join(abs_working_dir, path))
        err_str = "access" if mode == "r" else "write to"
        if os.path.commonpath([abs_working_dir, target_path]) != abs_working_dir:
            return (
                None,
                f'Error: Cannot {err_str} "{path}" as it is outside the permitted working directory',
            )

        return target_path, None
    except Exception as e:
        return None, f"Error: Invalid path: {e}"
