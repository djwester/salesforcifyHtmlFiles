# -*- coding: utf-8 -*-

# A very simple setup script to create a single executable
#
# hello.py is a very simple 'Hello, world' type script which also displays the
# environment in which the script runs
#
# Run the build process by running the command 'python setup.py build'
#
# If everything works well you should find a subdirectory in the build
# subdirectory that contains the files needed to run the script without Python

from cx_Freeze import setup, Executable

executables = [
    Executable('salesforcifyHtmlFiles.py')
]

setup(name='salesforcifyHtmlFiles',
      version='0.2',
      description='converts html files output by flare into something ready to be embedded in salesforce',
      executables=executables
      )
