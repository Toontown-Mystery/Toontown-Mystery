@echo off

taskkill /f /im astrond.exe
taskkill /f /im ppython.exe
taskkill /f /fi "windowtitle eq Toontown Mystery - UberDOG Server"
taskkill /f /fi "windowtitle eq Toontown Mystery - Astron Server"
taskkill /f /fi "windowtitle eq Toontown Mystery - AI (District) Server"
taskkill /f /fi "windowtitle eq Toontown Mystery - Game Client"

start start_astron_server.bat

ping 127.0.0.1 -n 1 > nul
start start_uberdog_server.bat

ping 127.0.0.1 -n 1 > nul
start start_ai_server.bat

ping 127.0.0.1 -n 3 > nul
start start_game.bat
