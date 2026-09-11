@echo off
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
pause