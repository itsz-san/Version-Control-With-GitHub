We are using this file to practice diff commands.

This line will be removed.

git-diff - Show changes between commits, commit and working tree, etc.

We will be practicing using the `git diff HEAD 'Test - Diff Commands.md'`. 

Scenario 1: Create New File
If we were to run the command after creating this file, it returns nothing. This makes sense,as the file hasn't even been added to the git repository for tracking. Hence, we have to run the `git add 'Test - Diff Commands.md'`.

Scenario 2: File has been moved to the staging area.
If we were to run the command now, it will output the entirety of the file content.

One thing to note is that each line is prepended with either a `+` or `-` symbol. The plus symbol is used to indicate what exists in the file currently. The minus symbol is used to indicate what it originally was.

Since, there is nothing to compare with, all lines will have the plus symbol at this point in time.


