# AutoDirSorter

An automatic directory organization tool that organizes files in specified directories according to preset rules.

## Project Purpose

This project aims to help users automate the organization of messy directories and improve file management efficiency. Through simple configuration files, users can customize classification rules to automatically move different types of files to corresponding subdirectories. For example, images, documents, and videos can be moved to `images`, `documents`, `videos` subdirectories respectively.

## Features

* Supports multiple file type classifications, including but not limited to images, documents, videos, audio, compressed files, etc.
* Customizable classification rules, supporting classification based on file extensions, filename pattern matching, file size, and other conditions.
* Supports recursive subdirectory processing.
* Provides configuration files for easy customization of classification rules and target directories.
* Provides command-line interface, easy to use.
* Cross-platform support (Linux, macOS, Windows).
* Open source and free, MIT license.

## Implementation

This project is written in Python, utilizing standard libraries such as `os`, `shutil`, `yaml` for file operations and configuration reading. The core logic is to read user-defined configuration files, traverse files in specified directories, match according to rules defined in the configuration files, and move matching files to corresponding target directories.

## Installation

Enter the project directory and execute pip install -r requirements.txt