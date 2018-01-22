#!/bin/bash

REPONAME=${PWD##*/}
# Get user input
read -p "Git Username:" GITHUBUSER
read -p "Repo Description:" DESCRIPTION

# Curl some json to the github API oh damn we so fancy
curl -u ${GITHUBUSER} https://api.github.com/user/repos -d "{\"name\": \"${REPONAME}\", \"description\": \"${DESCRIPTION}\", \"private\": false, \"has_issues\": true, \"has_downloads\": true, \"has_wiki\": false}"

git remote add origin https://github.com/${GITHUBUSER}/${REPONAME}

