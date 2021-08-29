@echo off
title Toontown Mystery - Developer Mini-Server Launcher
cd..

rem Read the contents of PPYTHON_PATH into %PPYTHON_PATH%:
set /P PPYTHON_PATH=<PPYTHON_PATH

echo Toontown Mystery Mini-Server Launcher

set /P TTOFF_LOGIN_TOKEN="Username (default: dev): " || ^
set TTOFF_LOGIN_TOKEN=dev

set /P TTOFF_GAME_SERVER="Miniserver (default: 127.0.0.1): " || ^
set TTOFF_GAME_SERVER=127.0.0.1

%PPYTHON_PATH% -m toontown.launcher.TTOffQuickStartLauncher
pause
