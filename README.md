# Soulfix

This repository contains some basic scripts to help move downloaded
audio files from a given path into a datestamped folder directory on
your local machine.

In the future, I aim to implement some basic second-stage tagging and
audio conversion features, so that, as a downloader, you don't need to
worry about downloading AIFF, WAV or FLAC files - this tool will just
convert them automatically for you.

## Usage

1. Clone the git repo
2. Install Python (version > 3.9 should do)
3. Run `pip install -r requirements.txt` to download the project's dependencies
4. Ensure you have setup your `.env` file correctly (use `.env.test` as a guide)
5. Identify the output directory of your choice, e.g. "/Users/johnsmith/Music"
6. Run `python main.py $FILE_YOU_WANT_TO_PROCESS`

## Contributing

At the moment, this project is for personal use only, however if you have any suggestions for features then please feel free to open an Issue (or even PR) and we can work on including the feature together.
