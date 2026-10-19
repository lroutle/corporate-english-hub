@echo off
title Deploy Tatra Sales Suite to Firebase Hosting
cd /d "%~dp0"

echo ======================================================================
echo    Deploy Tatra Sales and Engineering Suite to Firebase Hosting
echo ======================================================================
echo.

echo Step 1: Checking Firebase Authentication...
call npx -y firebase-tools login
echo.

set /p PROJECT_ID="Enter your Firebase Project ID (from console.firebase.google.com): "

if "%PROJECT_ID%"=="" (
    echo [ERROR] No Project ID entered. Exiting.
    pause
    exit /b 1
)

echo.
echo Deploying tatra-sales-engineering to https://%PROJECT_ID%.web.app ...
call npx -y firebase-tools deploy --only hosting --project %PROJECT_ID%

echo.
echo ======================================================================
echo Deployment completed!
echo Live URL: https://%PROJECT_ID%.web.app
echo ======================================================================
pause
