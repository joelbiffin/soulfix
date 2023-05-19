import logging
import os
import sys

from datetime import datetime
from pathlib import Path

from lib.converter import converter_for
from lib.file_transporter import FileTransporter


def env_vars():
  from dotenv import load_dotenv
  load_dotenv()

  output_directory = os.getenv("SOULFIX_OUTPUT_DIR")
  log_destination = os.getenv("SOULFIX_LOG_DIR", f"{Path(__file__).parent}/log")

  return output_directory, log_destination


if __name__ == "__main__":
  output_directory, log_destination = env_vars()

  logging.basicConfig(
    filename=f"{log_destination}/{datetime.now().isoformat()}.log",
    format="%(levelname)s - %(message)s",
    level=logging.INFO,
  )

  if output_directory is None:
    logging.error("Missing SOULFIX_OUTPUT_DIR environment variable")
    raise RuntimeError("Please set a SOULFIX_OUTPUT_DIR environment variable")

  _, path_of_file_to_process = sys.argv
  logging.info(f"Attempting to move the file, {path_of_file_to_process}")

  transporter = FileTransporter(destination_path=output_directory, logger=logging)
  transporter.create_target_dir()
  destination = transporter.move_file_to_target(filepath=path_of_file_to_process)

  converter_for(destination).convert()

