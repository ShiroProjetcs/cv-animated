@echo off
echo --- GIT LOG --- > git_report.txt
git log -n 10 --oneline >> git_report.txt
echo --- GIT REMOTE --- >> git_report.txt
git remote -v >> git_report.txt
echo --- GIT BRANCH --- >> git_report.txt
git branch >> git_report.txt
echo --- DIRECTORY LISTING --- >> git_report.txt
dir >> git_report.txt
