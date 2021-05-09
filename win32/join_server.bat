@echo off
title Toontown Mystery - Developer Mini-Server Launcher
cd..

echo Toontown Mystery Mini-Server Launcher

set /P TTOFF_LOGIN_TOKEN="Username (default: dev): " || ^
set TTOFF_LOGIN_TOKEN=dev

set /P TTOFF_GAME_SERVER="Miniserver (default: 127.0.0.1): " || ^
set TTOFF_GAME_SERVER=127.0.0.1

"panda/python/python.exe" -m toontown.launcher.TTOffQuickStartLauncher
pause
