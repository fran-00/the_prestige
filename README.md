# The Prestige - Image processor

This simple script resizes all images in a folder so that they do not exceed the specified resolution. It's pretty useful when you need to resize many large images quickly.

## How to Install

To get started, clone this repo:

    git clone git@github.com:fran-00/the_prestige.git

Create a new virtual environment with Python 3.12 and activate it. For example, on Windows with PowerShell I use [venv](https://docs.python.org/3/library/venv.html):

    python -m venv venv
    venv/Scripts/Activate.ps1

Install requirements (or just install [Pillow](https://pypi.org/project/Pillow/)):

    pip install -r requirements.txt

## Usage

Run the script:

    py app.py

You will be prompted to enter the folder path: it must contain subfolders with images. For now, further nested folders are not permitted. The script creates a backup copy of the image and processes the original: if something goes wrong it restores the original to avoid corrupting the file.
