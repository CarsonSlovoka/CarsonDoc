@echo off
echo ===== %~nx0 Begin =======
REM %APPDATA%\Local\Programs\Python\Python37\Scripts\sphinx-build.exe -b html source build
sphinx-build -b html source docs
cd docs
RMDIR /s /q _sources
index.html
cd ..
echo ===== %~nx0 End =======