@echo off
cd /d "%~dp0"
title Iniciador - Taller 2 FastAPI y MongoDB
echo ========================================================
echo   INICIANDO TALLER 2 (FASTAPI + MONGODB + DJANGO)
echo ========================================================
echo.

echo 1. Levantando Backend FastAPI en el puerto 8000...
start "FastAPI Backend (Puerto 8000)" cmd /k "if exist .venv\Scripts\activate call .venv\Scripts\activate && uvicorn app.main:app --reload --port 8000"

timeout /t 2 /nobreak >nul

echo 2. Levantando Frontend Django en el puerto 8080...
start "Django Frontend (Puerto 8080)" cmd /k "if exist .venv\Scripts\activate call .venv\Scripts\activate && cd frontend && python manage.py runserver 8080"

timeout /t 2 /nobreak >nul

echo.
echo ========================================================
echo Servidores en ejecucion:
echo  - Aplicativo Web:     http://127.0.0.1:8080/
echo  - Swagger Docs API:   http://127.0.0.1:8000/docs
echo ========================================================
echo.
echo Abriendo aplicativo web en el navegador...
start http://127.0.0.1:8080/
