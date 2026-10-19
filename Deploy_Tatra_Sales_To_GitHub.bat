@echo off
title Deploy Tatra Sales Suite to GitHub Pages
cd /d "%~dp0\tatra-sales-engineering"

echo ======================================================================
echo    Deploy Tatra Sales and Engineering Suite to GitHub Pages
echo ======================================================================
echo.

set /p REPO_NAME="Enter your GitHub Repository Name (e.g., tatra-sales-english): "

if "%REPO_NAME%"=="" (
    echo [ERROR] No repository name entered. Exiting.
    pause
    exit /b 1
)

echo.
echo Initializing git repository in tatra-sales-engineering...
if not exist ".git" (
    git init
    git branch -M main
)

git add .
git commit -m "Deploy Tatra Sales and Engineering testing suite"

echo Setting remote origin...
git remote remove origin 2>nul
git remote add origin https://github.com/lroutle/%REPO_NAME%.git

echo.
echo Pushing to GitHub (https://github.com/lroutle/%REPO_NAME%)...
git push -u origin main --force

echo.
echo ======================================================================
echo Repository pushed successfully!
echo.
echo NEXT STEP (Takes 30 seconds):
echo 1. Open: https://github.com/lroutle/%REPO_NAME%/settings/pages
echo 2. Under 'Build and deployment', set Branch to 'main' and '/ (root)'.
echo 3. Click 'Save'.
echo.
echo Your live site will be ready at:
echo https://lroutle.github.io/%REPO_NAME%/
echo ======================================================================
pause
