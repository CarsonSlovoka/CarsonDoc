@echo off
REM %APPDATA%\Local\Programs\Python\Python37\Scripts\sphinx-build.exe -b html source build
sphinx-build -b html source docs
cd docs
RMDIR /s /q _sources
index.html
echo "finished"
pause > nul