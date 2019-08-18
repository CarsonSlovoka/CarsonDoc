@echo off
REM %APPDATA%\Local\Programs\Python\Python37\Scripts\sphinx-build.exe -b html source build
sphinx-build -b html source build
cd build
RMDIR /s /q _sources
index.html
echo "finished"