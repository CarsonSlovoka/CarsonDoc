@echo off
echo ===== %~nx0 Begin =======
REM %APPDATA%\Local\Programs\Python\Python37\Scripts\sphinx-build.exe -b html source build

Set /p "rebuild_flag=rebuild?(Y/N)"

if "%rebuild_flag%" == "Y" (
	echo sphinx-build -E -b html source docs/temp
	sphinx-build -E -b html source docs/temp
) else (
	echo sphinx-build -b html source docs/temp
	sphinx-build -b html source docs/temp
)


cd docs/temp
REM RMDIR /s /q _sources
index.html
cd %~dp0
echo %cd%
echo ===== %~nx0 End ======= & pause > nul