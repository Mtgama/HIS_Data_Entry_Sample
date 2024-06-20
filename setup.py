import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {
    "includes": ["atexit", "PyQt5.QtCore", "PyQt5.QtGui", "PyQt5.QtWidgets",
                 "sqlite3", "codecs", "PyQt5.QtWebEngineWidgets",
                 "socket", "cryptography.fernet", "requests", "speech_recognition",
                 "os", "openpyxl", "PyPDF2", "docx", "difflib", "enchant"],
    "packages": ["PyQt5.QtCore", "PyQt5.QtGui", "PyQt5.QtWidgets"],
    "include_files": ['data.json'],
    "excludes": [],
    "optimize": 2,
    "include_msvcr": True,
}

# GUI applications require a different base on Windows (the default is for a console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [
    Executable("main.py", base=base, targetName="HIS.exe", icon="icon.ico")
]

setup(
    name="HIS",
    version="1.0",
    description="An application built with Python aimed at data entry and information security. Utilizes OCR for text extraction from images and voice typing. Features include username definition and the ability to detect changes in output files. Allows connection to an expert through `serverchat.exe` and scanning of documents.",
    options={"build_exe": build_exe_options},
    executables=executables
)
