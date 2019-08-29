@echo off
echo ===== %~nx0 Begin =======

Set /p "rebuild_flag=rebuild?(Y/N)"

if %rebuild_flag% == Y (

	call "sphinx_build(html).bat"
)
git add docs/*.* -f
echo ===== %~nx0 End ======= & pause > nul