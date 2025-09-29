@echo off
echo Installing College Assistant Chatbot dependencies...
echo ================================================
pip install Flask
if %errorlevel% neq 0 (
    echo Failed to install Flask
    pause
    exit /b 1
)
pip install transformers
if %errorlevel% neq 0 (
    echo Failed to install transformers
    pause
    exit /b 1
)
pip install torch
if %errorlevel% neq 0 (
    echo Failed to install torch
    pause
    exit /b 1
)
pip install pandas
if %errorlevel% neq 0 (
    echo Failed to install pandas
    pause
    exit /b 1
)
pip install rapidfuzz
if %errorlevel% neq 0 (
    echo Failed to install rapidfuzz
    pause
    exit /b 1
)
pip install numpy
if %errorlevel% neq 0 (
    echo Failed to install numpy
    pause
    exit /b 1
)
echo ================================================
echo All packages installed successfully!
echo You can now run: python app.py
pause
