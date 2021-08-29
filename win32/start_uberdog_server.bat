@echo off
title Toontown Mystery - UberDOG Server
cd..


"panda/python/python.exe" -m toontown.uberdog.UDStart --base-channel 1000000 ^
               --max-channels 999999 --stateserver 4002 ^
               --astron-ip 127.0.0.1:7199 --eventlogger-ip 127.0.0.1:7197
pause
