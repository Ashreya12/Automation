@echo off
setlocal

cd "C:\Users\USER\Desktop\GitHub Repos"
set /p username=Enter GitHub username:
set /P "=_" < NUL > "Enter password"
findstr /A:1E /V "^$" "Enter password" NUL > CON
del "Enter password"
set /P "password="
cls
color 07
set /p repoName=Name of repository:
python gitrepo.py %repoName% %username% %password%
mkdir %repoName%
cd %repoName%
git init
git remote add origin https://github.com/Ashreya12/%repoName%.git
type nul > readme.md
git add .
git commit -m "Initial Commit"
git push -u origin master
code .
