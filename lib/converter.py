import ffmpeg
import logging

from typing import Protocol
from pathlib import Path


class InfoLogger(Protocol):
  def info(self, message):
    return


class Converter(Protocol):
  file_to_convert: Path
  file_extension: Path
  _logger: InfoLogger

  def __init__(self, file_to_convert, file_extension, logger=logging, **kwargs):
    self.file_to_convert = file_to_convert
    self.file_extension = file_extension
    self._logger = logger

  def convert(self) -> None:
    return


def converter_for(file_path_to_convert: Path) -> Converter:
  print(file_path_to_convert)
  file_type = file_path_to_convert.suffix

  if file_type != '.mp3':
    return ToMp3Converter(file_path_to_convert.absolute(), file_type, bitrate='320k', logger=logging)

  return NullConverter(file_path_to_convert, file_type, logger=logging)


class ToMp3Converter(Converter):
  MP3 = 'mp3'

  def __init__(self, file_to_convert, file_extension, bitrate='320k', logger=logging):
    super().__init__(file_to_convert, file_extension, logger=logger)
    self.bitrate = bitrate
    self.input_file_extension = file_extension
    self.output_extension = self.MP3

  @property
  def file_to_output(self):
    return f"{str(self.file_to_convert).removesuffix(self.file_extension)}.{self.output_extension}"

  def convert(self):
    ffmpeg.input(self.file_to_convert).output(self.file_to_output, audio_bitrate=self.bitrate).run()


class NullConverter(Converter):
  def convert(self) -> None:
    self._logger.info("No need to convert the file")
