@echo off
REM ═══════════════════════════════════════════════════════════════════════════════
REM QuizApp v2.0 - Installation Script for Windows
REM Developed by: Noor Hoorain
REM GitHub: https://github.com/noorhoorain44-ship-it
REM ═══════════════════════════════════════════════════════════════════════════════

title QuizApp v2.0 Installer
color 0B

cls
echo.
echo  ╔══════════════════════════════════════════════════════════════════════════════╗
echo  ║                                                                              ║
echo  ║              🚀 QuizApp v2.0 - Windows Installation Script                   ║
echo  ║                                                                              ║
echo  ║              Developed by: Noor Hoorain                                        ║
echo  ║              GitHub: noorhoorain44-ship-it                                     ║
echo  ║                                                                              ║
echo  ╚══════════════════════════════════════════════════════════════════════════════╝
echo.

REM Check Windows version
for /f "tokens=4-5 delims=. " %%i in ('ver') do set VERSION=%%i.%%j
if "%version%" == "10.0" (
    echo [INFO] Windows 10/11 detected
) else if "%version%" == "6.3" (
    echo [INFO] Windows 8.1 detected
) else if "%version%" == "6.2" (
    echo [INFO] Windows 8 detected
) else if "%version%" == "6.1" (
    echo [INFO] Windows 7 detected
) else (
    echo [WARNING] Unknown Windows version
)

REM Check for Python
echo.
echo [*] Checking Python installation...
python --version >nul 2>&1
if %errorlevel% == 0 (
    echo [OK] Python found:
    python --version
    set PYTHON_CMD=python
    goto :PYTHON_FOUND
)

python3 --version >nul 2>&1
if %errorlevel% == 0 (
    echo [OK] Python3 found:
    python3 --version
    set PYTHON_CMD=python3
    goto :PYTHON_FOUND
)

echo [ERROR] Python not found!
echo.
echo [*] Please install Python 3.10 or higher from:
echo     https://www.python.org/downloads/
echo.
echo [*] Make sure to check "Add Python to PATH" during installation.
echo.
pause
exit /b 1

:PYTHON_FOUND
echo.

REM Check Python version compatibility
for /f "tokens=2" %%I in ('%PYTHON_CMD% --version 2^>^&1') do set PYVER=%%I
for /f "tokens=1,2 delims=." %%a in ("%PYVER%") do (
    set PYMAJOR=%%a
    set PYMINOR=%%b
)

if %PYMAJOR% LSS 3 (
    echo [WARNING] Python version %PYVER% may not support match-case statements.
    echo           The app will still work with some feature limitations.
) else if %PYMAJOR% == 3 if %PYMINOR% LSS 10 (
    echo [WARNING] Python %PYVER% detected. Python 3.10+ recommended.
    echo           The app will still work with some feature limitations.
) else (
    echo [OK] Python version is compatible!
)

echo.

REM Create installation directory
set INSTALL_DIR=%USERPROFILE%\QuizApp
echo [*] Creating installation directory: %INSTALL_DIR%
if not exist "%INSTALL_DIR%" mkdir "%INSTALL_DIR%"
if not exist "%INSTALL_DIR%\users" mkdir "%INSTALL_DIR%\users"
if not exist "%INSTALL_DIR%\quizzes" mkdir "%INSTALL_DIR%\quizzes"
if not exist "%INSTALL_DIR%\results" mkdir "%INSTALL_DIR%\results"
if not exist "%INSTALL_DIR%\exports" mkdir "%INSTALL_DIR%\exports"
echo [OK] Directories created
echo.

REM Copy files
echo [*] Installing QuizApp files...
copy /Y "%~dp0quizapp.py" "%INSTALL_DIR%\" >nul
if %errorlevel% neq 0 (
    echo [ERROR] Failed to copy quizapp.py
    echo         Make sure the file exists in the same directory as this installer.
    pause
    exit /b 1
)
echo [OK] Files copied
echo.

REM Create batch launcher
echo [*] Creating launcher...
(
echo @echo off
echo title QuizApp v2.0
echo color 0B
echo %PYTHON_CMD% "%INSTALL_DIR%\quizapp.py" %%*
echo if errorlevel 1 pause
echo exit
echo.
) > "%INSTALL_DIR%\QuizApp.bat"

echo [OK] Launcher created
echo.

REM Create desktop shortcut
echo [*] Creating desktop shortcut...
set DESKTOP=%USERPROFILE%\Desktop
set SHORTCUT="%DESKTOP%\QuizApp.lnk"

powershell -Command "$WshShell = New-Object -ComObject WScript.Shell; $Shortcut = $WshShell.CreateShortcut('%SHORTCUT%'); $Shortcut.TargetPath = '%INSTALL_DIR%\QuizApp.bat'; $Shortcut.WorkingDirectory = '%INSTALL_DIR%'; $Shortcut.Description = 'QuizApp v2.0 by Noor Hoorain'; $Shortcut.IconLocation = 'cmd.exe,0'; $Shortcut.Save()" >nul 2>&1

if exist %SHORTCUT% (
    echo [OK] Desktop shortcut created
) else (
    echo [WARNING] Could not create desktop shortcut
)
echo.

REM Add to PATH (optional)
echo [*] Would you like to add QuizApp to PATH? (Y/N)
set /p ADD_PATH=
if /I "%ADD_PATH%"=="Y" (
    echo [*] Adding to user PATH...
    for /f "tokens=2*" %%a in ('reg query "HKCU\Environment" /v Path 2^>nul ^| find "Path"') do set "USER_PATH=%%b"

    if defined USER_PATH (
        setx PATH "%USER_PATH%;%INSTALL_DIR%" >nul 2>&1
    ) else (
        setx PATH "%INSTALL_DIR%" >nul 2>&1
    )

    if %errorlevel% == 0 (
        echo [OK] Added to PATH. Please restart your terminal.
    ) else (
        echo [WARNING] Could not modify PATH. You may need administrator privileges.
    )
)
echo.

REM Verify installation
echo [*] Verifying installation...
if exist "%INSTALL_DIR%\quizapp.py" (
    echo [OK] Installation verified!
) else (
    echo [ERROR] Installation verification failed!
    pause
    exit /b 1
)

echo.
echo  ╔══════════════════════════════════════════════════════════════════════════════╗
echo  ║                                                                              ║
echo  ║                    ✅ INSTALLATION COMPLETE!                                  ║
echo  ║                                                                              ║
echo  ╚══════════════════════════════════════════════════════════════════════════════╝
echo.
echo  🚀 To start QuizApp:
echo     • Double-click the QuizApp icon on your Desktop
echo     • Or run: %INSTALL_DIR%\QuizApp.bat
echo     • Or run from terminal: QuizApp.bat (if added to PATH)
echo.
echo  📁 Installation location: %INSTALL_DIR%
echo  📊 Data directory: %INSTALL_DIR%
echo.
echo  💡 Tip: Create your own quizzes and challenge your friends!
echo.
echo  🐛 Issues? Report at: https://github.com/noorhoorain44-ship-it/quizapp/issues
echo.
echo  Made with ❤️  by Noor Hoorain
echo.
pause
