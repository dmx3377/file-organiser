> [!NOTE]
> This repository is in a low-activity state. While new features are unlikely, important fixes may still be applied.

---

![logo](https://gitlab.com/uploads/-/system/project/avatar/71627009/FO_Icon.jpg?width=128) 

# File Organiser

A simple yet powerful Python script to automatically organise files in a directory into categorised subfolders based on their file extension. Perfect for cleaning up messy `Downloads` or `Documents` folders.

## Features

- **Smart Categorisation:** Sorts files into predefined categories like `Images`, `Documents`, `Video`, `Scripts`, and more.
- **Collision Safety:** Automatically renames files (e.g., `file_1.txt`) if a naming conflict exists in the destination folder.
- **Dry Run Mode:** Preview your organisation results before any files are actually moved.
- **Lazy Folder Creation:** Only creates category folders if there are files present to fill them.
- **Customisable:** Easily extend the `FILE_EXTENSIONS` dictionary to suit your workflow.
- **Summary Report:** Displays a final count of moved files per category.

## Prerequisites

- Python 3.6 or higher.
- *No external libraries are needed!*

## How to Use

1. **Clone the repository:**
   ```bash
   git clone [github.com/dmx3377/file-organiser](https://github.com/dmx3377/file-organiser)
   cd file-organiser
   ```
2. **Run the script:**

Pass the directory path as the first argument.

* Safe Preview *(Dry Run)*:
`python file_organiser.py "/path/to/folder" --dry-run`

* Execute Organisation:
`python file_organiser.py "/path/to/folder"`

## How it Works
The script scans the `target_directory` and performs a reverse-lookup on file extensions. It handles edge cases like hidden files and the script's own file name to ensure only *your* data is moved.

If a destination file already exists, it calculates a unique name using a counter to ensure zero data loss.

## Customisation
Modify the `FILE_EXTENSIONS` dictionary at the top of `file_organiser.py` to add new categories.

```python
FILE_EXTENSIONS = {
    "Images": [".jpg", ".jpeg", ".png", ".webp"],
    "Scripts": [".py", ".js", ".lua", ".go", ".c"], 
    "Fonts": [".ttf", ".otf"], # <-- Example of adding a new category
    "Other": [] 
}
```

## Licensing
This project is licensed under the BSD 2-Clause License. For more information, see LICENSE.md.


<!-- line break -->
[Changelog](CHANGELOG.md) | [Contributing Guidelines](CONTRIBUTING.md)