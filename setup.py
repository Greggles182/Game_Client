import sys
from cx_Freeze import setup, Executable
base = None
if sys.platform == 'win32':
    base = 'Win32GUI'
opts = {'include_files' : ["img/", "img2/", "levels/", "music/"], 'includes' : ['passlib.handlers.sha2_crypt']}

setup(
    name = "Game_CLIENT",
    version = "1.0",
    description = "A game made by Gregory, Rory and Sam for Y7 Asessment",
    options = {'build_exe': opts},
    executables = [
        Executable("main.py", base=base),
        Executable("resetonline.py", base=base)])