# YouTube Downloader

A command-line tool to download videos and audio from YouTube.

## Features

* Downloads both video (mp4) and audio (mp3) from YouTube.
* Supports downloading single videos and playlists.
* Uses `yt-dlp` for the actual downloading.
* Uses `questionary` for user-friendly prompts in the terminal.

## Prerequisites

* **Python:** Ensure you have Python 3.8 or higher installed.
* **Dependencies:** You need the dependencies specified in `pyproject.toml`.  It is recommended to use a virtual environment.

## Installation

1.  **Clone the Repository:**
    ```bash
    git clone <your_repository_url>
    cd <your_repository_name>
    ```

2.  **Set up a Virtual Environment (Recommended):**
    * Using `venv`:
        ```bash
        python -m venv .venv
        source .venv/bin/activate  # On Linux/macOS
        .venv\Scripts\activate  # On Windows
        pip install -r requirements.txt
        ```
     * Using `uv`:
        ```bash
        uv venv .venv
        source .venv/bin/activate  # On Linux/macOS
        .venv\Scripts\activate  # On Windows
        uv pip sync pyproject.toml
        ```
    * If you have a `requirements.txt`, use that, otherwise use `uv pip sync pyproject.toml`

3.  **Install Dependencies:**
    ```bash
    #  pip install -r requirements.txt # if you have a requirements.txt
    #  OR
    uv pip sync pyproject.toml # if you are using uv
    ```

## Running the Script

To run the downloader, execute the `main.py` script:

```bash
uv run main.py
```

## Usage
The program will guide you through a series of prompts:

Enter the YouTube video or playlist URL: Provide the URL of the YouTube content you want to download.

Select download format: Choose between "mp4" (video) and "mp3" (audio).

The download will start, and you'll see the progress in the terminal.

You'll be asked if you want to download another video/playlist.

## Important Notes
CTRL+C to Exit: You can press CTRL+C at any time to stop the program and exit.

Output Directory: Downloaded files are saved in a directory named "downloads" within the project directory.