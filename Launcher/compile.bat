@echo off
title GalaxieFN Launcher compiller

echo file direcory : %CD%/
goto compile

:compile
py -m nuitka launcher.py --onefile --mingw64 --follow-imports --lto=no --enable-plugin=tk-inter --windows-disable-console --windows-company-name="GalaxieFN" --windows-product-name="GalaxieFN Launcher" --windows-product-version="1.0.1" --windows-icon-from-ico=%CD%/assets\logo.ico --remove-output --include-data-dir=%CD%/assets=.
goto end

:end
echo launcher compilled! 
pause