#!/bin/bash
git config --global core.mergeoptions --no-edit
BRANCH=$(git status | head -n 1 | awk '{ print $3 }')

git checkout master
git merge $BRANCH

git checkout next
git merge $BRANCH

git checkout production
git merge $BRANCH

git checkout master
git push origin master

git checkout next
git push origin next

git checkout production
git push origin production

git checkout $BRANCH
