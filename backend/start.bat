@echo off
echo Starting Naamveda Backend...
echo.

REM Activate virtual environment
if exist venv\Scripts\activate.bat (
    call venv\Scripts\activate.bat
) else (
    echo Virtual environment not found!
    echo Please run: python -m venv venv
    echo Then run: venv\Scripts\activate
    echo Then run: pip install -r requirements.txt
    pause
    exit
)

echo Virtual environment activated!
echo.
echo Starting FastAPI server...
echo Backend will be available at: http://localhost:8000
echo API Docs will be available at: http://localhost:8000/docs
echo.
echo Press Ctrl+C to stop the server
echo.

uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
