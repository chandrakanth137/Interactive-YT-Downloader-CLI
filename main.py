import yt_dlp
import questionary
import os
import sys

def download_video_or_audio(url, file_format, output_path="downloads"):
    """
    Downloads the video or audio from the given URL. Supports both single videos and playlists.
    The videos are stored in the specified output directory.

    Args:
        url (str): The URL of the video or playlist.
        file_format (str): The desired file format ("mp4" or "mp3").
        output_path (str): The path where the downloaded files should be saved.
    """
    os.makedirs(output_path, exist_ok=True)

    if file_format == "mp3":
        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": f"{output_path}/%(title)s.%(ext)s",
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }],
            "quiet": False
        }
    else:  # mp4
        ydl_opts = {
            "format": "bestvideo+bestaudio/best",
            "outtmpl": f"{output_path}/%(title)s.%(ext)s",
            "merge_output_format": "mp4",
            "quiet": False
        }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def safe_ask_text(message):
    """
    Safely asks a question and returns the answer. Handles KeyboardInterrupt silently.

    Args:
        message (str): The question to ask the user.

    Returns:
        str: User input, or None if KeyboardInterrupt is caught.
    """
    try:
        answer = questionary.text(message).ask()
        return answer
    except (KeyboardInterrupt, EOFError):
        return None

def safe_ask_select(message, choices):
    """
    Safely asks a question with multiple choices and returns the selected choice.
    Handles KeyboardInterrupt silently.

    Args:
        message (str): The question to ask the user.
        choices (list): A list of choices for the user to pick from.

    Returns:
        str: The selected choice, or None if KeyboardInterrupt is caught.
    """
    try:
        answer = questionary.select(message, choices=choices).ask()
        return answer
    except (KeyboardInterrupt, EOFError):
        return None

def main():
    """
    Main program loop: Asks the user for a YouTube URL, download format, and initiates the download.
    Handles graceful exit on KeyboardInterrupt.
    """
    print("🎵 YouTube Downloader")
    print("Press CTRL+C to exit.\n")

    try:
        while True:
            url = safe_ask_text("Enter the YouTube video or playlist URL:")
            if url is None:  # User pressed CTRL+C during text input
                print("\n👋 See you later!")
                break

            if not url.startswith("http"):
                print("⚠️ Invalid URL. Must start with 'http'.")
                continue

            format_choice = safe_ask_select(
                "Select download format:",
                choices=["mp4", "mp3"]
            )
            if format_choice is None:  # User pressed CTRL+C during select
                print("\n👋 See you later!")
                break

            print("\n📥 Starting download...")
            download_video_or_audio(url, format_choice)
            print("✅ Download completed!")

            another = safe_ask_select(
                "Do you want to download another video/playlist?",
                choices=["Yes", "No"]
            )
            if another != "Yes" or another is None: # Handle CTRL+C in the final question
                print("\n👋 See you later!")
                break
    except KeyboardInterrupt:
        # This catch is for interruptions outside of questionary prompts (though less likely here)
        print("\n👋 See you later!")

if __name__ == "__main__":
    main()