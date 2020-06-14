from cx_Freeze import setup, Executable


includefiles = [ 'data', 'resume', 'transform_data.py','get_url.py', 'script.py','config.ini']

build_exe_options = {"namespace_packages": ["zope"],
                     "excludes": ["tkinter"],
                     'include_files':includefiles}


setup(  name = "guifoo",
        version = "0.1",
        description = "My GUI application!",
        options = {"build_exe": build_exe_options},
        executables = [Executable("code_runer.py", base='Console')])