@echo off
:: Check if Python is installed
python --version
IF %ERRORLEVEL% NEQ 0 (
    echo Python is not installed. Please install Python before running this script.
    pause
    exit /B
)

:: Create a virtual environment called 'env'
python -m venv env

:: Activate the virtual environment
call env\Scripts\activate

:: Upgrade pip to the latest version
python -m pip install --upgrade pip

:: Install the required libraries
pip install pandas openpyxl

:: Confirmation message
echo Virtual environment setup complete and required libraries installed.
pause
