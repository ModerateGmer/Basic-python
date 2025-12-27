# Basic command Git
## git init
```
git init is a fundamental Git command used to initialize a new Git repository. This command transforms a standard directory into a Git-versioned project, enabling Git to track changes, manage versions, and facilitate collaboration. 
```
## git add
```
The git add command is a fundamental part of the Git version control system. It is used to add changes from the working directory to the staging area, also known as the "index." The staging area acts as an intermediate holding place for changes that are intended to be included in the next commit. 
Here's a breakdown of what git add does:
Stages Changes: When you modify a file, create a new file, or delete a file in your working directory, Git initially considers these changes as "unstaged." The git add command tells Git to take these changes and prepare them for inclusion in the next commit.
Prepares for Commit: The git commit command, which records changes to the repository's history, only considers files that are present in the staging area. Therefore, git add is a crucial step before making a commit. It allows you to carefully select which changes will be part of a particular snapshot of your project.
Flexibility in Staging: You can use git add to stage individual files, multiple specific files, or all changed files in the current directory (and its subdirectories) using git add . or git add -A. This flexibility allows you to craft precise and meaningful commits, ensuring that each commit represents a logical unit of work.
In essence, git add is the mechanism that allows you to curate the content of your next commit, giving you granular control over the history of your project.
```
### git add [file name]
```
The git add [file name] command is a fundamental Git command used to add changes from the working directory to the staging area (also known as the index). It prepares specific files for inclusion in the next commit. 
Here's a breakdown of its function:
Staging Changes: When you create, modify, or delete a file in your working directory, Git recognizes these changes but does not automatically include them in the next commit. git add [file name] explicitly tells Git to include the current state of that specific file in the staging area.
Preparing for Commit: The staging area acts as a temporary holding place for changes you intend to commit. Only the files that have been explicitly added to the staging area with git add will be included when you subsequently run git commit.
Selective Staging: This command allows for selective staging. You can choose to stage only specific files or parts of files, rather than committing all changes in your working directory at once. This enables you to create more focused and meaningful commits.
Example:
If you have a file named my_document.txt that you have modified and want to include in your next commit, you would execute:
Code

git add my_document.txt
After running this command, the changes in my_document.txt are staged and ready to be committed. You can then use git commit to permanently record these changes in your repository's history.
```

```
## git commit
```
A commit is a snapshot of your Git repository at one point in time. Watch this beginner Git tutorial video to understand how to perform a commit in Git to save file changes to your Git repository. Discover how multiple commits cumulatively form your Git repo's history, and walk through a typical Git workflow.
```
## git branch
```
A git branch is an independent line of development taken from the same source code. Separate branches can be merged into one branch. The diagram below illustrates how development can take place in parallel using branches. Multiple development projects are taking place using the same source code.
```
##Link to GitHub
```
git remote add origin [Link respository of GitHub]
```
## git push
```
git push is a fundamental Git command used to upload local repository content to a remote repository. It effectively transfers commits from your local machine to a remote server, such as GitHub, GitLab, or a self-hosted Git server. 
Here's a breakdown of what git push does:
Uploads local commits: When you make changes in your local repository and commit them, git push sends these new commits to the designated remote repository.
Synchronizes branches: It synchronizes a local branch with its corresponding remote branch, ensuring that the remote repository reflects the latest state of your local work.
Enables collaboration: By pushing your changes to a remote, you make them accessible to other collaborators, allowing for shared development and version control.
Basic Usage:
The most common way to use git push is:
Code

git push <remote> <branch>
<remote>: This typically refers to the name of your remote repository, commonly "origin" for the default remote.
<branch>: This specifies the local branch you want to push to the remote.
Example:
Code

git push origin main
This command pushes the commits from your local main branch to the main branch on the remote repository named origin.
Important Considerations:
Authentication: You usually need write access to the remote repository and will be prompted for authentication (e.g., username and password, or SSH key) unless already configured.
Fast-forwards: git push primarily performs "fast-forward" updates, meaning it adds new commits to the remote branch without overwriting existing history.
Force pushing: In certain situations, you might use git push --force to overwrite remote history, but this should be used with extreme caution as it can lead to data loss or conflicts with other collaborators. git push --force-with-lease offers a safer alternative for force pushing.
Tracking branches: You can set up tracking relationships between local and remote branches to simplify git push commands (e.g., git push -u origin main sets main as the upstream branch for future pushes).
```