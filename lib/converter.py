import ffmpeg
from typing import Protocol
from pathlib import Path


def converter_for(file_path_to_convert: Path):
  file_type = file_path_to_convert.suffix

  if file_type != '.mp3':
    return ToMp3Converter(file_path_to_convert.absolute(), file_type, bitrate='320k')

  return NullConverter(file_path_to_convert, file_type)


class Converter(Protocol):
  file_to_convert: Path
  file_extension: Path

  def __init__(self, file_to_convert, file_extension, **kwargs):
    self.file_to_convert = file_to_convert
    self.file_extension = file_extension

  def convert(self) -> None:
    return


class ToMp3Converter(Converter):
  MP3 = 'mp3'

  def __init__(self, file_to_convert, file_extension, bitrate='320k'):
    super().__init__(file_to_convert, file_extension)
    self.bitrate = bitrate
    self.input_file_extension = file_extension
    self.output_extension = self.MP3

  @property
  def file_to_output(self):
    return f"{str(self.file_to_convert).removesuffix(self.file_extension)}.{self.output_extension}"

  def convert(self):
    print(self.file_to_convert)
    print(self.file_to_output)
    ffmpeg.input(self.file_to_convert).output(self.file_to_output).run()


class NullConverter(Converter):
  pass
