from distutils.core import setup
import py2exe
import os

setup(windows = ["GalGen.py"],
      py_modules=["GalGenLib",
                  "GalGenGui"]
      )