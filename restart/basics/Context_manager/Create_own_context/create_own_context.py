import os

from pathlib import Path
from uuid import uuid4
from shutil import rmtree

class Temp:
	def __init__(self):
		self._original_path = Path.cwd()
		self._temp_path =  Path("/temp") / str(uuid4())

	def __enter__(self):
		self._temp_path.mkdir()
		os.chdir(self._temp_path)
		return self

	def __Exit__(self,*args):
		os.chdir(self.orignal_path)
		rmtree(self._temp_path)

	@property
	def path(self):
		return self._temp_path
