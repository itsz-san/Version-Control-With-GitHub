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

2022-12-07T22:03
Alright after spending a hot minute in the other branch I am back. I made a typo with the branch name. And I'm wondering how to change a branch name.

Apparently, it's possible with `git branch -m new-branch name` But I will have to switch back to that branch first before renaming. So let's leave those worries, along with the worry of conflicts, out of this branch. 

Also, in order to view branches. Use the `git branch` to list local repos. `-r` flag will list remote repos. `-a` will list ALL(both local and remote) repos.

Any hows, I realised that the Video lesson included the merge workflow. But ergh, I'll do that later. Time to move on to the next lesson.

2022-12-08T17:45
Watched up Video: Remote vs Local from Meta's Version Control course. A short and quick video which I feel could have been introduced earlier. The recurring sentiment is that the course could have been structured differently. It's a sentiment that many in the discussion forum share. 

A local and remote repository is self-explanatory. In any case, `git remote` lists the associated URLS of a git repo. `git remote add <url>` will add an upstream remote. Only with an upstream remote can we run `git push`, `git pull`, `git fetch` commands. As of now, we haven't covered `git fetch` yet. We have practised `git push`. But not `git pull` yet. As, we haven't really had a reason to do that yet. 

ASIDE: I'm using nvim to edit this file. I've been using the arrow down key to scroll down to the end of the file before making entries. I figure, it's worth while to learn some basic vim motions to help me move the cursor around faster.

G -> To jump to the last line
CTRL-End -> Moves the cursor to the end of the last line
    But I don't have an END key on my mechanical keyboard. lol
G+A -> Move to bottom of the file and switch to insert mode.
$ -> Shift cursor to end of line.
0 -> Shift cursor to start of line.

Also since, I have relative line numbers set up, I can jump to different lines by <Number>+j/k. 

Having said that, the most important thing is - `nvim README.md`, then `G+A` to get the ball rolling.

2022-12-08T18:04
I feel the need to clarify with myself the concepts of git areas(?). This wasn't explained clearly in the course and the vocabulary used doesn't seem consistent.

After reading through some articles and resources, I found that [The Three States and Areas of Git](https://snipcademy.com/git-fundamentals) gives the clearest and succinct introduction.

Further readings include;
-[Git Working Areas](https://blog.knoldus.com/git-working-areas/#3-repository-area)


In my own words, content in a git system moves through four areas.
1. Working Area (including Stash Area)
    This is the workspace area or also known as the working directory. The Stash Area, made through the `git stash` commands, is something I should look into more.
2. Staging Area
    This is where content that is ready for commits live. Content that has been `git add` is moved to the Staging Area.
3. Local Area
    This is the snapshot of the local repository.
4. Remote Area
    And this is the snapshot of a remote repository.

Fully understanding how git works would probably help ease my anxiety. The Medium article [Understanding Git - Index](https://konrad126.medium.com/understanding-git-index-4821a0765cf) by Zvonimir Spajic covers quite a bit and is quite easy to follow. The article is part of his Understanding Git series on Medium, and it is a much appreciated resource.


2022-12-08T20:15
Watched Video: Push and Pull from Meta's Version Control course. Fundamentally, the concept is easy to follow. The `git push` and `git pull` commands are used to manipulate content back and forth between two git areas; Local Area and Remote Area. As a reminder, the term area is synonymous with repository.

However, I find myself still unclear of what happens when conflicts arise. To illustrate my concerns; imagine two versions of a single file `Testing Push and Pull.txt`.

On the local repo the file contains the following;
```
This is a file to help me understand git push and pull workflows.

This line is written, staged and commited from my local machine.
```

On the remote repo the file contains the following;
```
This is a file to help me understand git push and pull workflows.

This line is written, staged and commited from Github website.
```

My question is what happens when I do either `push/pull`? Will the lines disappear? Let me test this out.

2022-12-08T21:00
Tried running `git pull --rebase` and the following message was returned;
```
Auto-merging Testing Push and Pull.txt
CONFLICT (content): Merge conflict in Testing Push and Pull.txt
error: could not apply 11e332c... Changed Testing Push and Pull.txt from local machine
hint: Resolve all conflicts manually, mark them as resolved with
hint: "git add/rm <conflicted_files>", then run "git rebase --continue".
hint: You can instead skip this commit: run "git rebase --skip".
hint: To abort and get back to the state before "git rebase", run "git rebase --abort".
Could not apply 11e332c... Changed Testing Push and Pull.txt from local machine
```

2022-12-08T20:32
With the abovementioned scenario, I tried running `git push`. The command failed with the following error message;
```
 ! [rejected]        master -> master (fetch first)
error: failed to push some refs to 'https://github.com/itsz-san/Version-Control-With-GitHub.git'
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref. You may want to first integrate the remote changes
hint: (e.g., 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
```
Folowing the message, I am going to try running `git pull` but I am wondering if it will overwrite what I have right now locally.

Running `git pull` showed the following error message;
```
hint: You have divergent branches and need to specify how to reconcile them.
hint: You can do so by running one of the following commands sometime before
hint: your next pull:
hint:
hint:   git config pull.rebase false  # merge (the default strategy)
hint:   git config pull.rebase true   # rebase
hint:   git config pull.ff only       # fast-forward only
hint:
hint: You can replace "git config" with "git config --global" to set a default
hint: preference for all repositories. You can also pass --rebase, --no-rebase,
hint: or --ff-only on the command line to override the configured default per
hint: invocation.
fatal: Need to specify how to reconcile divergent branches.
```

So currently, I cannot push changes to the remote repository. Nor can I pull changes from the remote repository to my local repository. And the question now is, What should I do?

2022-12-08T20:50
Completed Reading: Resolving Conflicts from Meta's Version Control course. It did absolutely nothing to help in the previous situation. Seriously, getting annoyed with the course quality. T_T

The reading introduced the concept of conflict and merging and rebasing. But does very little to elaborate. I am now even more confused. In trying to figure things out, I'm learning about the `git fetch` command which hasn't been mentioned so far. Let me muck around until I get this sorted.
