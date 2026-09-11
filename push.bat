@echo off
py generate.py
git add .
git commit -m "Auto update playlist"
git push origin main
pause