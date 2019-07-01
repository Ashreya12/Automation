@echo off
cd "Path to repos folder" 
set /p repoName=Name of repository:
python gitrepo.py %repoName%
mkdir %repoName%
cd %repoName%
git init
::Enter username in remote url
git remote add origin https://github.com/username/%repoName%.git
type nul > readme.md
git add .
git commit -m "Initial Commit"
git push -u origin master
code .
