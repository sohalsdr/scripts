@ECHO OFF
SETLOCAL ENABLEEXTENSIONS
SET parent=%~dp0
SET choice=%1
python3 %parent%\csv_to_md.py %choice%