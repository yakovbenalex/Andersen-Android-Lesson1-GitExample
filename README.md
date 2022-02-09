Andersen Android Lesson1 - Git Example

Git commands sequence:

# create git local
git init
type NUL > "Convert time seconds count to normal format.py"
git add .
git commit -m "Initial commit"
#git log

# push to remote
git remote add origin https://github.com/yakovbenalex/Andersen-Android-Lesson1-GitExample.git
git branch -M main
git push -u origin main

# create new branch
git checkout -b develop
# some changes in file ...
git commit -a -m "tsk0001 add main script funtional"
# some changes in file ...
git commit -a -m "tsk0002 add copy to clipboard functional"

# merge branches
git checkout main
git fetch
git merge develop
