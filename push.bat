@echo off
:loop
echo Running Python script to generate playlist...
python generate.py

echo.
echo Pulling latest changes from GitHub...
git pull origin main --rebase

echo.
echo Adding changes to git...
git add .

echo.
echo Committing changes...
git commit -m "Auto update playlist"

echo.
echo Pushing changes to GitHub...
git push origin main

echo.
echo Done! All tasks completed successfully.

:: ৩০ মিনিট পর পর চলার জন্য সময় (১৮০০ সেকেন্ড = ৩০ মিনিট)
timeout /t 1800 /nobreak > nul
goto loop