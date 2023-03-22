import logging
import os
import sys

from datetime import datetime
from pathlib import Path

from lib.file_transporter import FileTransporter

LOG_DESTINATION = f"{Path(__file__).parent}/log"
USER_HOME = os.getenv("HOME", "/Users/joelbiffin")
GLOB_MUSIC_DIR = f"{USER_HOME}/Music/Music"

if __name__ == "__main__":
  log_format = "%(levelname)s - %(message)s"
  logging.basicConfig(
    filename=f"{LOG_DESTINATION}/{datetime.now().isoformat()}.log",
    format=log_format,
    level=logging.INFO,
  )

  logging.info(f'ARGS: {sys.argv}')
  _, path_of_file_to_process = sys.argv

  logging.info(f"Attempting to move the file, {path_of_file_to_process}")

  transporter = FileTransporter(destination_path=GLOB_MUSIC_DIR, logger=logging)
  transporter.create_target_dir()
  transporter.move_file_to_target(filepath=path_of_file_to_process)
