# smart_organiser.py
import os
import shutil
import argparse
from pathlib import Path

# --- Configuration ---
# This dictionary maps folder names to the file extensions they should contain.
# You can easily add more categories or file types. Just type them into the relevant section.
FILE_EXTENSIONS = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".heic", ".tiff", ".bmp", ".svg"],
    "Documents": [".pdf", ".doc", "docx", ".txt", ".rtf", ".odt", ".xls", ".xlsx", ".ppt", ".pptx"],
    "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg", ".m4a"],
    "Video": [".mp4", ".mov", ".avi", ".mkv", ".wmv", ".flv"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
    "Scripts": [".py", ".js", ".sh", ".bat", ".html", ".css"],
    "Executables": [".exe", ".msi", ".dmg", ".app"],
    "Other": [] # A fallback category for everything else
}

def organise_folder(target_directory: Path):
    """
    Organises files in the target directory into subdirectories based on their extension.

    Args:
        target_directory (Path): The path to the folder to be organised.
    """
    if not target_directory.is_dir():
        print(f"Error: The path '{target_directory}' is not a valid directory.")
        return

    print(f"Organising files in: {target_directory}\n")

    # Create the category folders if they don't exist
    for folder_name in FILE_EXTENSIONS.keys():
        folder_path = target_directory / folder_name
        folder_path.mkdir(exist_ok=True) # exist_ok=True prevents an error if the folder already exists

    # Iterate over each item in the target directory
    for item in target_directory.iterdir():
        # Skip if it's a directory or the script itself
        if item.is_dir() or item.name == "smart_organiser.py":
            continue

        # Determine the destination folder for the file
        file_extension = item.suffix.lower()
        destination_folder = None

        for folder, extensions in FILE_EXTENSIONS.items():
            if file_extension in extensions:
                destination_folder = target_directory / folder
                break
        
        # If the file type is not in our main categories, move it to 'Other'
        if destination_folder is None:
            destination_folder = target_directory / "Other"

        # Move the file
        try:
            shutil.move(str(item), str(destination_folder))
            print(f"Moved: {item.name} -> {destination_folder.name}")
        except Exception as e:
            print(f"Error moving {item.name}: {e}")

    print("\nOrganisation complete!")

def main():
    """Main function to parse arguments and run the organiser."""
    # Set up the command-line interface
    parser = argparse.ArgumentParser(
        description="A smart file organizer that sorts files into categorised folders based on their extension.",
        epilog="Example: python smart_organiser.py /path/to/your/Downloads"
    )

    # Add an argument for the target directory
    parser.add_argument(
        "target_directory",
        type=str,
        help="The full path to the directory you want to organise."
    )

    args = parser.parse_args()
    
    # Convert the string path to a Path object for better handling
    directory_to_organise = Path(args.target_directory)
    
    organise_folder(directory_to_organise)

if __name__ == "__main__":
    main()