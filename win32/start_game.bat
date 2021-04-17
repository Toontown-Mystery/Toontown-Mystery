@echo off
title Toontown Online - Game Client
cd..

rem Read the contents of PPYTHON_PATH into %PPYTHON_PATH%:
set /P PPYTHON_PATH=<PPYTHON_PATH

set TTOFF_LOGIN_TOKEN=dev

"panda/python/python.exe" -m toontown.launcher.TTOffQuickStartLauncher
pause
