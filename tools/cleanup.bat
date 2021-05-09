@echo off
title Toontown cleaner
cd ..
:main
"panda/python/python.exe" -m tools.cleanup
pause
goto main
