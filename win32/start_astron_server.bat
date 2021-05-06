@echo off
title Toontown Mystery - Astron Server
cd ../astron
astrond --loglevel info config/astrond.yml
pause
