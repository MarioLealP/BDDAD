@echo off
:: Check if the virtual environment exists
if not exist "env\Scripts\activate" (
    echo Virtual environment not found. Please run setup.bat first to create the environment.
    pause
    exit /B
)

:: Activate the virtual environment
call env\Scripts\activate

:: Run the Python script (replace 'your_script.py' with the actual name of your Python script)
python ExcelToInsert.py

:: Confirmation message
echo Script execution complete.
pause
