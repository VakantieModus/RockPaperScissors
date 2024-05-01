@echo off
REM Check if virtual environment folder exists
IF NOT EXIST venv (
    echo Creating virtual environment...
    python -m venv venv
) ELSE (
    echo Virtual environment already exists.
)

REM Activate the virtual environment
venv\Scripts\activate

REM generate poetry.lock
echo Generating poetry.lock file, this might take a while...
poetry lock

REM install using poetry.lock
echo Installing dependencies from poetry.lock
poetry install

echo Virtual environment setup complete.
