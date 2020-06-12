import sys
from cx_Freeze import setup, Executable
import pkg_resources.py2_warn
includefiles = [ 'data', 'resume', 'transform_data.py','get_url.py', 'script.py','config.ini']
# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"namespace_packages": ["zope"], "excludes": ["tkinter"],'include_files':includefiles}

# GUI applications require a different base on Windows (the default is for a
# console application).
#base='Console'
#if sys.platform == "win32":
    #base = "Win32GUI"

setup(  name = "guifoo",
        version = "0.1",
        description = "My GUI application!",
        options = {"build_exe": build_exe_options},
        executables = [Executable("code_runer.py", base='Console')])