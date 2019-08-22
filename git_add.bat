@echo off
git add .
git reset docs/*
gitk --all
cmd.exe %~dp0