import os
from setuptools import setup
import sys

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

def conf_path(name):
  if sys.prefix == '/usr':
    conf_path = os.path.join('/etc', name)
  else:
    conf_path = os.path.join(sys.prefix, 'etc', name)
  return conf_path

setup(
    name = "download_weather_boundaries",
    version = "0.0.1",
    author = "Ronald van Haren",
    author_email = "r.vanharen@esciencecenter.nl",
    description = ("A python library to download weather forecast "
                   "and climate data."),
    license = "Apache 2.0",
    keywords = "ERA-Interim GFS",
    url = "https://github.com/ERA-URBAN/boundaries",
    packages=['download_weather_boundaries'],
    scripts=['download_weather_boundaries/scripts/download_interim'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved ::Apache Software License",
    ],
)
