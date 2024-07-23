@echo off

rem Delete existing virtual environment (if exists)
if exist env (
    echo Deleting existing virtual environment...
    rmdir /s /q env
)

rem Create a new virtual environment
echo Creating new virtual environment...
python -m venv env

rem Activate the virtual environment
echo Activating virtual environment...
call env\Scripts\activate

rem Install dependencies from requirements.txt
echo Installing dependencies...
pip install -r requirements.txt

echo Setup complete

rem running app.py
echo Running app.py in the virtual environment...
python app.py