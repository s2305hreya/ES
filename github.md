# GitHub Commands Cheat Sheet

## 1. Configure Git

### Check Git version
git --version
Use: Shows the installed Git version.

### Set username
git config --global user.name "Your Name"
Use: Sets your Git username.

### Set email
git config --global user.email "your@email.com"
Use: Sets your Git email.

### Check configuration
git config --list
Use: Displays all Git configurations.

---

## 2. Initialize Repository

### Initialize Git
git init
Use: Creates a new local Git repository.

### Clone Repository
git clone <repository-link>
Use: Copies a remote repository to your computer.

Example:
git clone https://github.com/user/project.git

---

## 3. Check Status

### Check repository status
git status
Use: Shows changed, staged, and untracked files.

---

## 4. Add Files

### Add one file
git add filename
Use: Adds a specific file to staging area.

### Add all files
git add .
Use: Adds all files to staging area.

---

## 5. Commit Changes

### Commit with message
git commit -m "Your message"
Use: Saves staged changes with a message.

---

## 6. Branch Commands

### Show branches
git branch
Use: Lists all branches.

### Create new branch
git branch branch-name
Use: Creates a new branch.

### Switch branch
git checkout branch-name
Use: Switches to another branch.

### Create and switch branch
git checkout -b branch-name
Use: Creates and switches to new branch.

### Rename branch
git branch -M main
Use: Renames current branch to main.

---

## 7. Remote Repository Commands

### Connect local repo to GitHub
git remote add origin <repository-link>
Use: Links local repository to GitHub repository.

### Check remote repositories
git remote -v
Use: Displays connected remote repositories.

---

## 8. Push Commands

### Push code first time
git push -u origin main
Use: Uploads code to GitHub and sets upstream branch.

### Push changes
git push
Use: Uploads latest commits to GitHub.

---

## 9. Pull Commands

### Pull latest changes
git pull
Use: Downloads latest code from remote repository.

---

## 10. Fetch Commands

### Fetch changes
git fetch
Use: Downloads changes without merging.

---

## 11. Merge Commands

### Merge branch
git merge branch-name
Use: Merges another branch into current branch.

---

## 12. Undo Changes

### Remove file from staging
git reset filename
Use: Unstages a file.

### Undo last commit
git reset --soft HEAD~1
Use: Removes last commit but keeps changes.

### Delete local changes
git restore filename
Use: Restores file to last committed state.

---

## 13. View History

### View commits
git log
Use: Shows commit history.

### One line history
git log --oneline
Use: Shows compact commit history.

---

## 14. Delete Branch

### Delete local branch
git branch -d branch-name
Use: Deletes a branch locally.

---

## 15. Stash Commands

### Save temporary changes
git stash
Use: Temporarily stores uncommitted changes.

### Restore stashed changes
git stash pop
Use: Restores latest stashed changes.

---

## 16. Useful GitHub Workflow

### Step 1: Initialize repository
git init

### Step 2: Add files
git add .

### Step 3: Commit files
git commit -m "Initial commit"

### Step 4: Connect GitHub repository
git remote add origin <repository-link>

### Step 5: Push code
git push -u origin main

---

## 17. Helpful Extra Commands

### Show current branch
git branch --show-current
Use: Displays current branch name.

### Show differences
git diff
Use: Shows file changes not yet committed.

### Remove tracked file
git rm filename
Use: Deletes file and tracks deletion.

### Create empty commit
git commit --allow-empty -m "message"
Use: Creates an empty commit.

---
