@echo off
title Toontown Mystery - Game Client
cd..


set TTOFF_LOGIN_TOKEN=dev
:main
"panda/python/python.exe" -m toontown.launcher.TTOffQuickStartLauncher
pause
goto main
