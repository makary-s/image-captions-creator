@echo off

SET VENV_PATH=".venv"

IF EXIST "%VENV_PATH%\Scripts\activate" (
    CALL "%VENV_PATH%\Scripts\activate"
) ELSE (
    python -m venv "%VENV_PATH%"
    CALL "%VENV_PATH%\Scripts\activate"
    pip install -r requirements.txt
)

python main

deactivate

pause