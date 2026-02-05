# smart_organiser.py
import argparse
from pathlib import Path

# --- Configuration ---
FILE_EXTENSIONS = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".heic", ".tiff", ".bmp", ".svg"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".rtf", ".odt", ".xls", ".xlsx", ".ppt", ".pptx"],
    "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg", ".m4a"],
    "Video": [".mp4", ".mov", ".avi", ".mkv", ".wmv", ".flv"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
    "Scripts": [".py", ".js", ".sh", ".bat", ".html", ".css"],
    "Executables": [".exe", ".msi"],
    "Other": []  # fallback category
}

# Create a reverse lookup dict: extension -> folder
EXTENSION_MAP = {ext: folder for folder, exts in FILE_EXTENSIONS.items() for ext in exts}

def organise_folder(target_directory: Path):
    """Organises files in the target directory into subdirectories based on their extension."""
    if not target_directory.is_dir():
        print(f"Error: '{target_directory}' is not a valid directory.")
        return

    print(f"Organising files in: {target_directory}\n")

    # Create all category folders at once
    for folder_name in FILE_EXTENSIONS.keys():
        (target_directory / folder_name).mkdir(exist_ok=True)

    script_name = Path(__file__).name

    for item in target_directory.iterdir():
        if item.is_dir() or item.name == script_name:
            continue

        folder_name = EXTENSION_MAP.get(item.suffix.lower(), "Other")
        destination = target_directory / folder_name

        try:
            item.rename(destination / item.name)
            print(f"Moved: {item.name} -> {folder_name}")
        except Exception as e:
            print(f"Error moving {item.name}: {e}")

    print("\nOrganisation complete!")

def main():
    parser = argparse.ArgumentParser(
        description="A smart file organiser that sorts files into categorised folders based on their extension."
    )
    parser.add_argument("target_directory", type=str, help="Path to the directory to organise.")
    args = parser.parse_args()

    organise_folder(Path(args.target_directory))

if __name__ == "__main__":
    main()

