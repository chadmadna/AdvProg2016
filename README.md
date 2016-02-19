Advanced Programming 2016
=========================

Welcome to the code repository for Advanced Programming 2016 course. 
This repository hosts weekly tutorial codes and other, course-related 
code snippets.

Initial Setup
-------------

1. Clone this exercise into your local machine. Git command: 
`git clone https://gitlab.com/AdvProg2016/weekly-exercises.git <PATH>` 
E.g. `git clone https://gitlab.com/AdvProg2016/weekly-exercises.git D:\AdvProg2016-exercises` 
will create a new directory called `AdvProg2016-exercise` in `D:` 
drive and clone the content of repository into the new directory.
2. Add new remote called **source** that points to this GitLab 
repository. Git command: `git remote add source https://gitlab.com/AdvProg2016/weekly-exercises.git`
3. To pull/update current local copy with latest version from 
`AdvProg2016/weekly-exercises` repository, use: `git pull source` 
This repository will contain latest code templates and exercise 
description files.
4. Create a new project on GitLab using your own account. Make sure 
that your project visibility level is set to **Internal** or 
**Public**.
5. Inform your GitLab username and project repository name to 
the teaching team.

Submission Guide
----------------

1. Ensure that the **origin** remote is pointing to your own GitLab 
project repository. Git command: `git remote set-url origin 
<URL_TO_REPO>`
2. Commit your work. Git command: `git commit <FILES_TO_COMMIT> -m 
"<COMMIT_MESSAGE>"` E.g. `git commit foo.py -m "Initial commit."` or 
`git commit foo.py bar.py xyz.py -m "Commit 3 files."`
3. Push your work. For first push attempt, use Git command: `git push 
--set-upstream origin master`. For subsequent pushes, use Git command: 
`git push`, or more explicitly: `git push origin`

