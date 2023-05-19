import logging

from datetime import datetime
from pathlib import Path


def filename_from_path(filename):
  return filename.split("/")[-1]


class FileTransporter(object):
  def __init__(self, destination_path, current_date=datetime.today(), logger=logging):
    self._destination_path = destination_path
    self._current_date = current_date
    self._logger = logger

  @property
  def target_month_dir(self):
    return self._current_date.strftime('%m-%Y')

  @property
  def target_directory(self):
    return f"{self._destination_path}/{self.target_month_dir}"

  def create_target_dir(self):
    Path(self.target_directory).mkdir(parents=True, exist_ok=True)

  def move_file_to_target(self, filepath: str):
    filename_suffix = filename_from_path(filepath)

    try:
      return Path(filepath).rename(f"{self.target_directory}/{filename_suffix}")
    except FileNotFoundError as e:
      self._logger.error("Unfortunately the given file was not found")
    finally:
      self._logger.info(f"The file has successfully been moved to {self.target_directory}")
