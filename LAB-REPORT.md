# Lab Report: Student Task Manager

**Name:** Laiba Amir
**Reg. No:** FA23-BSE-067
**Course:** CSC418 DevOps for Cloud Computing
**Repository:** https://github.com/laibaamir-21/student-task-manager
**Release:** https://github.com/laibaamir-21/student-task-manager/releases/tag/v1.0.0

## 1. Git vs GitHub; add, commit and push

Git is a version control tool that runs on my computer. It records changes to my files as commits so I can see the history and go back if needed. GitHub is a website that hosts Git repositories online and adds teamwork features such as Issues, Pull Requests and Actions.

- **git add** moves the changes I choose into the staging area, ready for the next commit.
- **git commit** saves the staged changes as a snapshot in my local history, with a message describing it.
- **git push** uploads my local commits to the remote repository on GitHub.


## 2. Branches, Pull Requests and merge conflicts

Branches let me build a feature separately without touching the stable main branch. I made three: add-task, complete-task and delete-task, each with two commits. A Pull Request asks to merge a branch into main and lets someone review the changed files and leave comments first. I linked each one to an Issue with "Closes #N". A merge conflict happens when two branches change the same lines of a file differently, so Git cannot decide which version to keep and asks me to choose.

In my conflict demo, two branches started from the same README commit and both changed the line "Project status: Planning" to different text. After the first merged, merging the second conflicted. I removed the conflict markers, kept the correct line, staged the file and committed.


## 3. Fetch vs pull; merge vs rebase

- **fetch** downloads new commits from the remote but does not change my working files or current branch.
- **pull** is fetch plus merge, so it downloads and combines the changes into my current branch straight away.
- **merge** joins two branches with a merge commit and keeps the real history, including where the branches split.
- **rebase** replays my commits on top of another branch to give a straight, linear history. It rewrites the commits, so it should not be used on branches other people share.

## 4. How GitHub Issues and Actions help a team

Issues keep tasks, bugs and ideas in one place with labels and discussion, so everyone knows what needs doing and what is finished. GitHub Actions runs automated steps, such as the unit tests, on every push and Pull Request. This catches mistakes early and gives reviewers confidence before merging. In my project the first run failed because I broke a test on purpose, and the second passed after I fixed it.


## 5. A difficulty I faced and how I solved it

While making the feature branches, my feature/complete-task branch was created from the wrong place, so it contained the add-task commit, and one edit stayed uncommitted and followed me onto main. I found it with `git log --graph --all`. I committed the stray change on the correct branch, deleted the wrong branch, and recreated it from main. Later some of my edit scripts silently changed nothing, because Windows line endings (CRLF) did not match my search patterns. I fixed this by normalising the line endings first and checking that each script printed DONE.

## 6. Release

I published release v1.0.0 with notes describing the features, the development workflow and the documentation.

