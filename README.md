> [!NOTE]
> This repository is a clone from [the original GitLab repo](https://gitlab.com/dmxsoftware/file-organiser). However, this one **will be the one in current maintenance.** Consider the one on GitLab *deprecated*.
---
![logo](https://gitlab.com/uploads/-/system/project/avatar/71627009/FO_Icon.jpg?width=128) <!-- File Organiser logo --> 
# File Organiser

A simple yet powerful Python script to automatically organise files in a directory into categorised subfolders based on their file extension. Perfect for cleaning up messy `Downloads` or `Documents` folders.

## Features

- **Automatic Categorisation:** Sorts files into predefined categories like `Images`, `Documents`, `Video`, `Audio`, and more.
- **Customisable:** Easily extend or change the categories and file types by modifying the `FILE_EXTENSIONS` dictionary in the script.
- **Safe:** Automatically creates necessary folders and skips any items that are already directories.
- **Fallback Category:** Any file type not explicitly defined will be moved to an `Other` folder, ensuring no file is left behind.
- **Command-Line Interface:** Easy to use from the terminal, just point it at a directory.

## Prerequisites

- Python 3.6 or higher. *No external libraries are needed!*

## How to Use

1.  **Clone the repository or download the script:**
    ```bash
    git clone github.com/dmx3377/file-organiser
    cd file-organiser
    ```

2.  **Run the script from your terminal:**

    The script takes one argument: the full path to the directory you want to organise.

    ```bash
    python smart_organiser.py "/path/to/your/folder"
    ```

    **Examples:**


    * To organise your **Downloads** folder on Windows:
        ```bash
        python smart_organiser.py "C:\Users\YourUsername\Downloads"
        ```

    * To organise your **Documents** folder on Linux:
        ```bash
        python smart_organiser.py "/home/yourusername/Documents"
        ```

    The script will print the name of each file as it moves it.

## How it Works

The script scans all files in the specified `target_directory`. For each file, it checks its extension (e.g., `.pdf`, `.jpg`, `.mp4`) and compares it against the categories defined in the `FILE_EXTENSIONS` dictionary. It then moves the file to the corresponding category folder. If a category folder doesn't exist, it creates it first.

## Customisation

You can easily customise the organisation logic by editing the `FILE_EXTENSIONS` dictionary at the top of the `smart_organiser.py` script in an IDE or text editor.

For example, if you want to add a new category for `Fonts` and sort `.ttf` and `.otf` files into it, you would modify the dictionary like this:

```python
FILE_EXTENSIONS = {
    "Images": [".jpg", ".jpeg", ".png", ...],
    "Documents": [".pdf", ".docx", ...],
    "Audio": [".mp3",...],
    "Video": [".mp4",...],
    "Archives": [...],
    "Scripts": [".lua", ".py", ...],
    "Executables": [".exe",...],
    "Fonts": [".ttf", ".otf"], # <-- New Category
    "Other": [] # <-- Other things can go here if they do not fit the above categories.
}
```

## Licensing
This project is licensed under the *BSD 3-Clause License*. For more information, see [LICENSE.md](/LICENSE.md).
___
### [Changelog](/CHANGELOG.md)
### [Contributing Guidelines](/CONTRIBUTING.md)
