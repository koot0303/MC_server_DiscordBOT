@echo off

echo 仮想環境を有効化します...
call .\env\Scripts\activate.bat

echo Botを起動します...
python bot.py

pause