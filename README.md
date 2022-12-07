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

2023-12-07T21:21
Watched Video: Branches from Meta's Version Control Course. The video started with a follow-along example of how to use `git checkout` and `git merge`. Curiously, it didn't even explain conceptually what a branch is. I followed along the video, but ended up googling for answers. 

Apparently, according to Atlassian, a "branch represents an independent line of development." From what I can gather, I should create a new branch when working on a specific thing like a feature or issue. I suppose then, that each branch could also be linked to some kind of requirements. But I'm only just guessing.

There are some questions I have. Particularly, how would a solo developer work with git branches. For example, if I was working on multiple things at a same time, I would probably have to switch branches often don't I? It seems a tad of a bother to switch between branches often. I am also wondering what are the naming conventions for naming branches. And while I'm on the topic of convention, I have been wondering what are the best practices for writing commit messages. Or let's back up a little bit, when do we make commits to begin with. Right now, I'm just treating it as saving a file on a whim. 

In any case, I want to try practice this branching thingy. So here's the plan. I will create a new branch called `feature/devlog-scripts`. Hypothetically, I will be working on developing a shell script to make logging from the cli easier. As it is, I am using nvim to write this. And I feel it would be better, if I could make create new entries on the fly from the cli. Especially with regards to adding the timestamp. Currently, I am typing the timestamp manually. I believe that by writing a shell script, it would reduce the barrier to making jots and let me make log entries more often.

In this branch, I will add an empty `devlog.spec` file. Or maybe I'll just write some initial ideas for the feature. Don't mind the file extension. I think it just looks cool that way.

So...
`git branch feature/devlog-scripts`
`touch devlog.spec`
`git add devlog.spec`
`git commit -m "Speccing the devlog feature"`
`git push -u origin feature/devlog-scripts`

By the end of this, I should be able to see the branch in the project's github page. To make it less complicated, I will first commit this latest entry. So in the `feature/devlog-scripts` branch, this log entry will be the last update. It gets confusing otherwise.

2022-12-07T21:57
Alright, it has been successful. But I fucked up the name of the branch. LOL! There is typo. But whatever. Ok, so the question I have is as I work on this feature, I add new entries here. I do the `git add`, `git commit`, `git push` and etc as usual. But This will only be in this branch. I wouldn't be able, for example, to see this entry if I switch to the main branch.

And then, what happens if I made new entries that only exists in the main branch? When I complete this feature and try to merge this branch with the main, what happens?

It's easy enough to understand that the new files will be added to the main branch. But what about conflicts? Alright that's enough wondering here. Let me try to get back to the main branch by using `git checkout main`.
