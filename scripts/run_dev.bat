@echo off
REM Windows quick start. Usage:  scripts\run_dev.bat
cd /d %~dp0..
if not exist .venv (
    echo [run_dev] creating venv...
    python -m venv .venv
)
call .venv\Scripts\activate.bat
pip install -q -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
