# MediaFire Bypass

A bypass to download files and folders from MediaFire without the need for a subscription to their premium plans.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
  - [Download Individual File](#download-individual-file)
  - [Download Entire Folder](#download-entire-folder)
- [Examples](#examples)
- [Contributions](#contributions)
- [License](#license)
- [Contact](#contact)
- [Acknowledgements](#acknowledgements)

## Introduction

MediaFire Bypass allows users to download entire files and folders from MediaFire without the need for a subscription to their premium plans. This project is designed to facilitate bulk downloading of content, bypassing the restrictions imposed by MediaFire.

## Features

- Download individual files from MediaFire.
- Download entire folders from MediaFire.
- No subscription to MediaFire required.
- Command-line interface for ease of use.
- Support for multi-threaded downloads.
- Automatic verification of file integrity using SHA-256.
- Color-coded status messages for easy readability.

## Requirements

- Python 3.7 or higher
- pip (Python package manager)
- Internet connection

## Installation

Follow these steps to install MediaFire Bypass:

```bash
# Clone the repository
git clone https://github.com/AxthonyV/Mediafire_Bypass.git

# Navigate to the project directory
cd Mediafire_Bypass

# Install the dependencies
pip install -r requirements.txt

## Usage

After installation, you can use MediaFire Bypass from the command line. Here are some basic commands:

# Download an individual file
python mediafire.py "https://www.mediafire.com/file/example"

# Download an entire folder
python mediafire.py "https://www.mediafire.com/folder/example"

## Download Individual File

python mediafire.py "https://www.mediafire.com/file/example" -o /output/path

## Download Entire Folder

python mediafire.py "https://www.mediafire.com/folder/example" -t 5
