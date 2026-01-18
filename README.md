# Claude Clone: AI Code Assistant

A command-line AI coding assistant powered by Google's Gemini 2.0 Flash model. This tool allows the AI to interact with your codebase by reading files, writing code, and running Python scripts.

## Features

- **Gemini 2.0 Integration**: Uses the latest `gemini-2.0-flash` model for fast and intelligent code generation.
- **Function Calling**: The AI can actively interact with the filesystem through a set of tools:
  - `get_files_info`: List files and directories to understand project structure.
  - `get_file_content`: Read the contents of specific files.
  - `write_file`: Create or modify files with generated code.
  - `run_python_file`: Execute Python scripts and capture output/errors.
- **Loop-based Problem Solving**: Automatically handles multi-step tasks by iterating through function calls and responses (up to 20 iterations).
- **Verbose Mode**: Provides detailed token usage and function call logs for transparency.

## Tech Stack

- **Language**: Python 3.12+
- **LLM**: Google Gemini (via `google-genai`)
- **Environment Management**: `python-dotenv`
- **Build System**: `uv`

## Installation

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/claude-clone.git
    cd claude-clone
    ```

2.  **Install dependencies**:
    Using `uv`:
    ```bash
    uv sync
    ```

3.  **Set up environment variables**:
    Create a `.env` file in the root directory and add your Gemini API key:
    ```env
    GEMINI_API_KEY=your_api_key_here
    ```

## Usage

Run the assistant by providing a prompt:

```bash
python main.py "Create a calculator app in the calculator directory"
```

### Options

- `user_prompt`: The instruction you want the AI to follow.
- `--verbose`: Enable detailed output including token counts and function call arguments.

## Project Structure

- `main.py`: Entry point for the CLI application.
- `functions/`: Contains the logic and schemas for the AI's toolset.
- `prompts.py`: Defines the system instructions for the AI agent.
- `calculator/`: Default working directory for the AI's file operations.

## Security Note

The AI is configured to operate within a specific working directory (`./calculator`) for security. Ensure that any sensitive files are outside this scope if you are testing untrusted prompts.
