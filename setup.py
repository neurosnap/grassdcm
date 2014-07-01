import re
from setuptools import setup, find_packages, Extension
from glob import glob

setup(
	name='grassdcm',
	version='0.0.1',
	author='Eric Bower',
	author_email='neurosnap@gmail.com',
	packages=find_packages(),
	ext_modules=[Extension("gdcm", glob("source/Common/*.cxx") + glob("source/DataDictionary/*.cxx") + glob("source/DataStructureAndEncodingDefinition/*.cxx") + glob("source/InformationObjectDefinition/*.cxx") + glob("source/MediaStorageAndFileFormat/*.cxx"))],
	url='http://pypi.python.org/pypi/grassdcm/',
	license='LICENSE',
	#headers=["source/Common/gdcmConfigure.h", "source/DataDictionary", "source/DataStructureAndEncodingDefinition", "source/InformationObjectDefinition", "source/MediaStorageAndFileFormat"]
)