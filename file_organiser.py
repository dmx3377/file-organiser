import argparse
from pathlib import Path
from collections import Counter

# --- Configuration ---
# These are examples, you can add, remove, or change any of the file extensions to suit you!
FILE_EXTENSIONS = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".heic", ".tiff", ".bmp", ".svg", ".webp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".rtf", ".odt", ".xls", ".xlsx", ".ppt", ".pptx", ".csv"],
    "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg", ".m4a"],
    "Video": [".mp4", ".mov", ".avi", ".mkv", ".wmv", ".flv", ".webm"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
    "Scripts": [".py", ".js", ".sh", ".bat", ".html", ".css", ".lua", ".go", ".c", ".cs"],
    "Executables": [".exe", ".msi", ".apk", ".app"],
    "Other": []  # fallback category
}

# Create a reverse lookup dict: extension -> folder
EXTENSION_MAP = {ext: folder for folder, exts in FILE_EXTENSIONS.items() for ext in exts}


def get_unique_path(destination_dir: Path, file_name: str) -> Path:
    """
    Ensures no files are overwritten. If 'file.txt' exists, 
    returns a path for 'file_1.txt', 'file_2.txt', etc.
    """
    target_path = destination_dir / file_name
    if not target_path.exists():
        return target_path

    # Extract name and extension
    stem = target_path.stem
    suffix = target_path.suffix
    counter = 1

    # Keep incrementing until we find an available filename
    while True:
        new_name = f"{stem}_{counter}{suffix}"
        new_path = destination_dir / new_name
        if not new_path.exists():
            return new_path
        counter += 1


def organise_folder(target_directory: Path, dry_run: bool = False):
    """Organises files in the target directory into subdirectories based on their extension."""
    if not target_directory.is_dir():
        print(f"❌ Error: '{target_directory}' is not a valid directory.")
        return

    mode_text = "[DRY RUN - No files will be moved]" if dry_run else "[ACTIVE MODE]"
    print(f"\n{mode_text} Organising files in: {target_directory.resolve()}\n")

    script_name = Path(__file__).name
    stats = Counter()

    for item in target_directory.iterdir():
        # Skip directories, the script itself, and hidden files
        if item.is_dir() or item.name == script_name or item.name.startswith('.'):
            continue

        folder_name = EXTENSION_MAP.get(item.suffix.lower(), "Other")
        destination_dir = target_directory / folder_name
        
        # Get a collision-safe destination path
        final_destination = get_unique_path(destination_dir, item.name)

        stats[folder_name] += 1

        if not dry_run:
            try:
                # Lazy folder creation: only create if we actually need it
                destination_dir.mkdir(exist_ok=True)
                item.rename(final_destination)
                
                # If renamed due to collision, show the new name
                if item.name != final_destination.name:
                    print(f"Moved & Renamed: {item.name} -> {folder_name}/{final_destination.name}")
                else:
                    print(f"Moved: {item.name} -> {folder_name}/")
                    
            except Exception as e:
                print(f"Error moving {item.name}: {e}")
                stats[folder_name] -= 1 # Remove from stats if failed
        else:
            # Dry run output
            print(f"Would move: {item.name} -> {folder_name}/" + 
                  (f"{final_destination.name}" if item.name != final_destination.name else ""))

    # --- Print Summary ---
    print("\n" + "="*30)
    print("📊 ORGANISATION SUMMARY")
    print("="*30)
    if not stats:
        print("No files found to organise.")
    else:
        for category, count in stats.most_common():
            print(f"{category:<15} : {count} file(s)")
    print("="*30 + "\n")


def main():
    parser = argparse.ArgumentParser(
        description="A smart file organiser that sorts files into categorised folders safely.",
        epilog="Example: python file_organiser.py ./Downloads --dry-run"
    )
    parser.add_argument("target_directory", type=str, help="Path to the directory to organise.")
    parser.add_argument("--dry-run", action="store_true", help="Preview changes without moving any files.")
    
    args = parser.parse_args()

    organise_folder(Path(args.target_directory), args.dry_run)

if __name__ == "__main__":
    main()