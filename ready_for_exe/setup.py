application_title = "Library"
main_python_file = "index.py"

import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32" :
    base = "Win32GUI"

include_files=['themes']
includes = []

build_exe_options = {"includes" : includes ,"include_files": include_files}


setup(
    name = application_title,
    version = "0.1",
    description = "sample library application",
    options = {"build_exe": build_exe_options},
    executables = [Executable(main_python_file, base = base)]
)