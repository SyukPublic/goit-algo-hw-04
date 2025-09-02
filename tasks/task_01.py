# -*- coding: utf-8 -*-

"""
HomeWork Task 1
"""

import argparse
import shutil
from pathlib import Path
from typing import Optional, Union


def get_absolute_path(path: Union[Path, str], current_dir: Optional[Union[Path, str]] = None) -> Path:
    """Return the absolute path for the given path and the current directory

    :param path: specified path (str, Path, mandatory)
    :param current_dir: current directory (str, Path, optional)
    :return: absolute path (Path)
    """
    if not path:
        # The path can not be None or an empty string
        raise ValueError('The path can not be empty')

    if Path(path).is_absolute():
        # If the specified path is an absolute - return it
        return Path(path)

    if current_dir is not None and isinstance(current_dir, str):
        # If the current directory is not specified, use the current working directory
        current_dir = Path(current_dir)

    # Construct an absolute path and return
    return (current_dir if current_dir is not None else Path.cwd()) / path


def file_path_build(file: Path, dest: Path) -> Path:
    """Build a new file name based on the destination folder and file extension

    :param file: Absolute path of the existing file (Path, mandatory)
    :param dest: Destination folder (Path, mandatory)
    :return: New file absolute path (Path)
    """

    # Build a new file name based on the destination folder and file extension
    file_extension: str = file.suffix[1:] if file.suffix.startswith(".") else file.suffix
    file_name: str = file.stem
    new_file_name: Path = dest / (file_extension or "without_extension") / f"{file_name}.{file_extension}"

    # Verify if a file with the same name already exists
    rename_tries: int = 0
    while new_file_name.exists():
        rename_tries += 1
        # Build a new file name with index of copy
        new_file_name = new_file_name.with_stem(f"{file_name} ({rename_tries})")

    return new_file_name


def folder_copy(source: Path, dest: Path) -> None:
    """Recursively sort by extension and copy all the files from the source folder to the destination folder

    :param source: Source folder (Path, mandatory)
    :param dest: Destination folder (Path, mandatory)
    """

    print(f"Process folder: {source}")

    try:
        for child in source.iterdir():
            if child.is_dir():
                folder_copy(child, dest)
            else:
                # Build a new file name based on the destination folder and file extension
                file_name = file_path_build(child, dest)
                try:
                    # Create a new folder if it does not already exist
                    file_name.parent.mkdir(parents=True, exist_ok=True)
                    # Copy the file
                    shutil.copy(child, file_name)
                    print(f"File: {child} copied to {file_name}")
                except OSError as e:
                    print(f"Failed to copy file \"{child}\" to \"{file_name}\": {str(e)}")
    except OSError as e:
        print(f"Failed to process folder \"{source}\": {str(e)}")


def cli() -> None:
    try:
        parser = argparse.ArgumentParser(
            description="Copy and sort the files from source folder to destination folder",
            epilog="Good bye!")
        parser.add_argument("-s", "--source", type=str, required=True, help="Source folder")
        parser.add_argument("-d", "--destination", type=str, default="dist", help="Destination folder (default \"dist\")")

        args = parser.parse_args()

        folder_copy(get_absolute_path(args.source), get_absolute_path(args.destination))
    except Exception as e:
        print(e)

    exit(0)
