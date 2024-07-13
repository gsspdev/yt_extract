import subprocess
import json
import sys

def get_yt_metadata(link):
    """
    Run the 'yt --metadata <link>' command and return the JSON output.
    
    Args:
    link (str): The YouTube video link to fetch metadata for.
    
    Returns:
    dict: Parsed JSON metadata or None if an error occurs.
    """
    try:
        # Run the command and capture its output
        result = subprocess.run(['yt', '--metadata', link], 
                                capture_output=True, 
                                text=True, 
                                check=True)
        
        # Parse the output as JSON
        metadata = json.loads(result.stdout)
        return metadata
    except subprocess.CalledProcessError as e:
        # Handle errors if the command fails
        print(f"Error running command: {e}", file=sys.stderr)
        print(f"Error output: {e.stderr}", file=sys.stderr)
        return None
    except json.JSONDecodeError as e:
        # Handle errors if the output is not valid JSON
        print(f"Error parsing JSON: {e}", file=sys.stderr)
        return None

def save_metadata_to_file(metadata, filename):
    """
    Save the metadata dictionary to a JSON file.
    
    Args:
    metadata (dict): The metadata to save.
    filename (str): The name of the file to save the metadata to.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(metadata, f, ensure_ascii=False, indent=2)
    print(f"Metadata saved to {filename}")

if __name__ == "__main__":
    # Check if a link was provided as a command-line argument
    if len(sys.argv) < 2:
        print("Usage: python script.py <youtube_link>")
        sys.exit(1)
    
    # Get the YouTube link from command-line arguments
    link = sys.argv[1]
    
    # Fetch the metadata
    metadata = get_yt_metadata(link)
    
    if metadata:
        # Save the metadata to a file
        save_metadata_to_file(metadata, "yt_metadata.json")
    else:
        print("Failed to retrieve metadata.")
