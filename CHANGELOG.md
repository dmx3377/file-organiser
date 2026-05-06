# File Organiser -- Changelog

## 6th May 2026 - v2.0
Total overhaul of the code:

### New features include:
* **Collision Avoidance:** Files will no longer be overwritten.
    * If image.jpg exists, the script now creates image_1.jpg, image_2.jpg, etc.

* **Dry Run Mode:** Added a `--dry-run` flag to preview organisation.

* **Lazy Folder Creation:** Folders are now created only when a file exists for that category: No more empty "Video" folders if you only have images.

* **Summary Statistics**: A neat table is generated at the end of every run to show exactly what was moved.

* **Expanded Extension Support:** Added support for modern formats in the `FILE_EXTENSIONS` table.


## 30th August 2025 - v1.1
Code optimised and cleaned up.
Slightly improvements to the README.

## 14th July 2025 - v1.0
Initial release.