@echo off
REM %1: input.scss
REM %2: output.css
REM sass --style compressed "%1" "%2"
cd ../docs
sass --style compressed "%~dp0/select_language.scss" "select_language.css"
