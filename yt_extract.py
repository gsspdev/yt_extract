import subprocess
import json
import sys
import re
import os

def get_yt_metadata(link):
    """
    Run the 'yt --metadata <link>' command and return the JSON output.

    Args:
    link (str): The YouTube video link to fetch metadata for.

    Returns:
    dict: Parsed JSON metadata or None if an error occurs.
    """
    try:
        result = subprocess.run(['yt', '--metadata', link],
                                capture_output=True,
                                text=True,
                                check=True)
        metadata = json.loads(result.stdout)
        return metadata
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {e}", file=sys.stderr)
        print(f"Error output: {e.stderr}", file=sys.stderr)
        return None
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}", file=sys.stderr)
        return None

def sanitize_filename(title):
    """
    Sanitize the title to create a valid filename.

    Args:
    title (str): The original title.

    Returns:
    str: A sanitized version of the title suitable for use as a filename.
    """
    sanitized = re.sub(r'[\\/*?:"<>|]', "", title)
    sanitized = sanitized.replace(" ", "_")
    return sanitized[:255]

def save_metadata_to_file(metadata, title):
    """
    Save the metadata dictionary to a JSON file in the 'transcripts' folder.

    Args:
    metadata (dict): The metadata to save.
    title (str): The title to use for the filename.
    """
    # Create the 'transcripts' directory in the root if it doesn't exist
    transcripts_dir = os.path.join(os.path.expanduser("~"), "yt_transcripts")
    os.makedirs(transcripts_dir, exist_ok=True)

    sanitized_title = sanitize_filename(title)
    filename = f"{sanitized_title}.json"
    filepath = os.path.join(transcripts_dir, filename)

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(metadata, f, ensure_ascii=False, indent=2)
    print(f"Metadata saved to {filepath}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <youtube_link>")
        sys.exit(1)

    link = sys.argv[1]
    metadata = get_yt_metadata(link)

    if metadata:
        title = metadata.get('title', 'Untitled')
        save_metadata_to_file(metadata, title)
    else:
        print("Failed to retrieve metadata.")
