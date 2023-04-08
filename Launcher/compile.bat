@echo off
title GalaxieFN Launcher compiller

echo file direcory : %CD%/
goto downloadntk
goto compile

:downloadntk
py -m pip install nuitka

:compile
echo.
echo 		press enter if you want to compile with nuitka
echo.
pause
py -m nuitka launcher.py --onefile --mingw64 --follow-imports --lto=no --enable-plugin=tk-inter --windows-disable-console --windows-company-name="GalaxieFN" --windows-product-name="GalaxieFN Launcher" --windows-product-version="1.2" --windows-icon-from-ico=%CD%/assets\logo.ico --remove-output --include-data-dir=%CD%/assets=.
goto end

:end
echo launcher compilled! 
pause