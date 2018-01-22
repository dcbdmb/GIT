#!/bin/bash

REPONAME=${PWD##*/}
# Get user input
read -p "Git Username:" GITHUBUSER
read -p "Repo Description:" DESCRIPTION
read -p "Override current directory name?::" answer
while true
do
  case $answer in
   [yY]* ) read -p "Enter new RepoName:" REPONAME
           break;;
   [nN]* ) exit;;
  esac
done

curl -u ${GITHUBUSER} https://api.github.com/user/repos -d "{\"name\": \"${REPONAME}\", \"description\": \"${DESCRIPTION}\", \"private\": false, \"has_issues\": true, \"has_downloads\": true, \"has_wiki\": false}"

git remote add origin https://github.com/${GITHUBUSER}/${REPONAME}

