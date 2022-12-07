This repository is used to document my learning journey as I try to wrap my head around Git and GitHub, a I follow along Meta's Version Control course on Coursera.

## DEVLOG
This section shall be used for institial journaling, where I document my thoughts during my learning journey.

2023-12-07T00:19
Honestly, I have stopped using Meta's Version Control course as reference to learn about Git and GitHub. The course material has been disappointing so far. I'll skip my gripes for later.

For now, what I have been able to do;
1. Install GitHub CLI in my Ubuntu WSL.
2. Authenticate to use GitHub CLI.
3. Initialise a new git repository and then use `gh repo create` within the repository's directory to put it in my GitHub.
4. git add README.md to start tracking it.
5. git commit -m to well...commit with a message.
6. git push to push the changes upstream to my GitHub.

It is all pretty much a blur right now, but hopefully as I continue I can make better sense of it. But being able to push changes to GitHub feels great. It's almost like uploading a post on Instagram. If that makes any sense.

2023-12-07T00:49
Okay, I take it back. After the first inital commit. I added the previous entry. I then tried `git commit` and then `git push`. Thinking that I can then later see the changes updated on the repo's GitHub page. But unfortunately, it didn't work.

When I try `git log`, a command to see past commits, I don't see my previous commit attempt. I'm not entirely sure what went wrong.

2023-12-07T00:53
Aright, it would seem that I would have to do `git add` again before commits. Obviously, I'm not quite sure of the git workflow. I'll probably stop mucking around for now, and continue on with Meta's Version Control course. As bad as it seemingly is, I want to complete it for the sake of completing it. T_T

2023-12-07T17:45
Watching Video: How Git Works from Meta's Version Control course. Introduced to the three different states in a git workflow; Modified, Staged, Committed.

I think I understand a little why I had troubles in the previous journal entry. Essentially, everytime I want to 'save', I need to ensure that I run the `git add` to include updates to a particular file into the staging area. However, only when I run `git commit` would a snapshot of the changes be created i.e 'saving' it. 

This begs the question, what if I make changes across multiple files? Do I need to run multiple `git add` commands for each changed file? Also, I could quite easily forget which files I make changes to. How could I know which files to add into the staging area.

2023-12-07T17:52
An idea just comes to mind. As you can see, I am using interstitial journaling. It is possible to make commits for every time I make a record entry? Ok that was dumb. Of course, it's possible. It should be possible to write a shell script for this. But the question is do I want to? lol.

2023-12-07T18:01
Watched Video: Add and Commit from Meta's Version Control course. The video also introduced the command `git status` which answers my previous question. Using that command, git will print information on the statuses of the current git directory. Essentially, before running `git commit` I could use `git status` to review and remind myself which files I want to add into the staging area.

I also learnt that if I want to remove a file from the staging area, I could use `git restore --staged untrack.txt`.

The video also covered `git commit` and `git push`, but I guess I'm already doing that now. In fact, let me make a commit and push after this.

Also not to self, currently there is an untrack.txt file in my working directory. I created it using the `touch` command. Then I added it into the staging area with `git add untrack.txt`. Then I ran `git restore --staged untrack.txt` to remove it from the staging area. This is why the remote repo wouldn't have the `untrack.txt` file. 

Finally, I then ran `git add README.md` and `git commit -m "Practiced Add, Restore, Commit and Push".`
And pomodoro break.
