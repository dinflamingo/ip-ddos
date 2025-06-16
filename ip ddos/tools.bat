@echo off
:menu
cls
echo 1. Ping en IP
echo 2. Hent EXIF fra billede
echo 3. Discord token info
echo 4. Afslut
set /p c=Vælg: 
if "%c%"=="1" goto ping
if "%c%"=="2" goto exif
if "%c%"=="3" goto discord
if "%c%"=="4" exit
goto menu

:ping
set /p ip=Indtast IP:
ping %ip%
pause
goto menu

:exif
set /p img=Sti til billede:
python get_exif.py "%img%"
pause
goto menu

:discord
set /p token=Indtast Discord token:
python discord_info.py "%token%"
pause
goto menu
