@echo off
echo Building Chemical Visualizer Desktop App...

REM Activate Environment
call ..\backend\venv\Scripts\activate

REM Install PyInstaller
pip install pyinstaller

REM Build EXE
echo Creating Executable...
pyinstaller --noconfirm --onedir --windowed --name "ChemicalVisualizer" --add-data "ui;ui" --hidden-import "PyQt5" --collect-all "reportlab" main.py

echo.
echo ===================================================
echo BUILD SUCCESSFUL!
echo ===================================================
echo Your app is ready at: desktop-app\dist\ChemicalVisualizer\ChemicalVisualizer.exe
echo You can zip the 'ChemicalVisualizer' folder and share it with generic laptops!
echo.
pause
