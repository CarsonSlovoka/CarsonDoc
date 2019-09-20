@echo off

REM RUN THIS SCRIPTS IN CASE YOU FORGET TO DO SOMETHING!

set "ruby_dir=C:\Ruby25-x64\bin\"

cd _build
set "src_dir=%cd%"

cd ../docs
set "out_dir=%cd%"

echo src_dir = %src_dir%\scss_language.scss
echo out_dir = %out_dir%\scss_language.css
echo "sass.bat --style compressed src_dir\scss_language.scss out_dir\scss_language.css"
REM C:\Ruby25-x64\bin\sass.bat
call sass.bat --style compressed "%src_dir%\select_language.scss" "%out_dir%\select_language.css"
del "%out_dir%\select_language.css.map"
rmdir /s /Q "%out_dir%\.sass-cache"
echo select_language.css is ready!


cd %~dp0
echo git add docs/*
git add docs/* -f
git st

cmd.exe %dp0