# The Mood DJ

[![Tests](https://github.com/tmady/IS4010-Final-The-Mood-DJ/actions/workflows/tests.yml/badge.svg)](https://github.com/tmady/IS4010-Final-The-Mood-DJ/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)

A command-line application that analyzes your mood from a picture and suggests a playlist to match.

## Features

- Analyzes mood from an image file.
- Suggests a music playlist based on the detected mood.
- Supports a "Dev Mode" for testing without full dependencies.

## Installation

1.  **Clone this repository:**
    ```bash
    git clone https://github.com/tmady/IS4010-Final-The-Mood-DJ.git
    cd IS4010-Final-The-Mood-DJ
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

Run the application with the path to an image:

```bash
python -m src.main --image-path /path/to/your/image.jpg
```

To run in "Dev Mode" (uses mock data):
```bash
python -m src.main --image-path /path/to/your/image.jpg --dev-mode
```

## Testing

Run the test suite with pytest:

```bash
pytest
```

For verbose output:
```bash
pytest -v
```

## AI-Assisted Development

This project was developed with assistance from AI tools. For details on how AI was used, see [AGENTS.md](AGENTS.md).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.