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

2022-12-08T21:53
Alright after some porridge and mucking around, I sort of get it a little bit. Due to the conflict(s), I ended up running `git pull --rebase`. After that I followed along with all messages to resolve the conflicts.

Running `git status` after `git pull --rebase` shows the following message;
```
interactive rebase in progress; onto 2d2a9c7
Last command done (1 command done):
   pick 11e332c Changed Testing Push and Pull.txt from local machine
Next command to do (1 remaining command):
   pick 8b9ddfa Updated README.md
  (use "git rebase --edit-todo" to view and edit)
You are currently editing a commit while rebasing branch 'master' on '2d2a9c7'.
  (use "git commit --amend" to amend the current commit)
  (use "git rebase --continue" once you are satisfied with your changes)
```

The process is manual and tedious of sort. 

The first one was with regards to `Testing push and pull.txt`. Opening the file, git has editted the content with visual indicators to mark conflicted content. Basically, look for `<<<<<<<`, `=======` and `>>>>>>>` to know where to make changes. I edited the file until I'm satisfied and I consider the conflict resolved. Then I do a `git add` and `git commit -m` for the changes. After which, I ran the `git rebase --continue` to move on to the next conflict until I see `Successfully rebased and updated refs/heads/master.`. Finally, when everythin is done, I pushed the local repository to the remote.

This experiment has made me realised the importance of knowing when and what to commit. And it had me wondering how to write commit messages. 

Fri  9 Dec 18:05:20 +08 2022
Made a quick edit to the feature/devlog-scritpts to practice switching and working on another branch. As a reminder, to see other branches use the `git branch` command. To switch to another branch, `git checkout <branch>`. And then the usual `git add`, `git commit -m` and `git push`.

In brief, I wrote what I think would be a feature requirements document in the devlog.spec file. To see the update, go to the branch and read it. lol.

In any case, I've learnt that running `:r !date` in nvim would insert the date on a newline. This is much more pleasant that typing it out manually. Right now, the date format is different from previous format. But I think the broke convention is small price to pay for convenience. It's also possible to configure the format used by the `date` command but that would mean more typing. So for now, I'll stick with `:r !date`.


Fri  9 Dec 19:34:43 +08 2022
Out of curiosity, I tried using cli-gh to create issue via `gh issue create`. The issue was created but I didn't know how to use nano to compose the body for the issue. Every keystroke presented gibberish on the screen. And I didn't know what to do. In any case, it would seem that it is possible to at least create and view GitHub issues from the cli. I probably just need to learn a bit more. But let's put off the deep dive into cli-gh for later.

Fri  9 Dec 22:43:17 +08 2022
Watched Video: Example workflow from Meta's Version Control course. Can't say the content was meaningful.It covered commands that was already touched on previously. Namely, `git checkout -b "feature/new-branch"` to create and switch to a new branch. It also introduced the `git add .` command but it didn't even explain what it does. I found out by googling that it is used to add everything in the current directory and all files within it recursively.

The lesson also used `git commit -m "chore: created new branch with new README file"`. The way the commit message was written caught my eye. I went ahead to find out what some tips are on writing commit mesages.

Notably, [Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/) is a good resource to get started. From there, I got to know that commit messages can include multi-paragraph and multiple footers.

Also worth noting is that best practices varies from project to project. Some projects would define their own conventions, while others don't at all.

This article [How to Write Good Commit Messages: A Practical Git Guide](https://www.freecodecamp.org/news/writing-good-commit-messages-a-practical-guide/) from freecodecamp is also pretty handy.

It showed me how to configure the default editor for commit messages via `git config --global core.editor nano`. In my case, I switched nano to nvim. Now everytime I run `git commit`, I will be directed to a nvim buffer to write my commit message.

I just have to remember that **the first line is the short description and that it has to be around 50 characters or less**. After an empty line break, everything will be added as the extended description.

In trying to understand how to write better commit messages, I found out that it is necessary to know the different types of commit. Some example include;
- feat
- fix
- style
- refactor
- test
- docs
- chore
- revert

I feel like git commit messages should have been covered in the course. It gives context to when to know to make commits. I suppose based on the list above, most of my commits doesn't fall into any type category. I think for now, I'll prefix my messages with `nani:` to refer to commits that I make that doesn't fall into any type category. 

Fri  9 Dec 23:26:11 +08 2022
Watched Video: HEAD from Meta's Version Control course. I have no idea what was the point of this video. XD

The lesson showed us the hidden `.git` folder, how to access it and how to run cat on some files to show the ID or something something. What the fuck was the point of all this? To begin with, I feel like a lesson on the `.git` folder could have given some context. Heck, it's week 3 of the Version Control course, I think we're about due for some explanations on the inner workings of git.

Wew, I took a breather. I sounded agitated a few lines ago. Which is true. I am annoyed. In any case, I read up [A Detailed Explanation of the Underlying Data Structures and Principles of Git](https://www.alibabacloud.com/blog/a-detailed-explanation-of-the-underlying-data-structures-and-principles-of-git_597391#:~:text=There%20are%20four%20major%20types,data%20structure%20of%20each%20object.). Also see [Git Internals - Git Objects](https://git-scm.com/book/en/v2/Git-Internals-Git-Objects) and [Git Internals - Git References](https://git-scm.com/book/en/v2/Git-Internals-Git-References).


Sat 10 Dec 01:46:10 +08 2022
Watched Video: Diff Commands from Meta's Version Control course. Alright, this lesson was pretty decent. I followed along and practiced some ways to use the command.

I learnt how to use the command to check between different versions of commits.

`git diff HEAD <filename>` as shown from the course, comapares the file version in the working tree with the file version last commmited in the remote repository i.e STAGING AREA VS REMOTE AREA.

If only one pointer(?) is given, the comparison will be against the STAGING AREA.

We can compare a file between two different commits with `git diff <commit> <commit> <filename>`.

We can compare between two diffent commits simply by excluding a filepath.

The `<commit>` argument mentioned above can be found by running `git log --pretty=oneline` command. An example of the output;
```
9812143c5ce72e1e34d602d2466d4db8aba248fa (HEAD -> master) nani: Added new file to practice diff commands
f965b745b66027e5d8a58abc5c0c902a49273b15 nani: watched HEAD from the course
18924ab6742a7eb228f7853f48f8870b08494f6c (origin/master) nani: of workflow and good commit messages
c814ef1ac04abf6c055dce130f2e6a1ac7ef2300 Attempted to use cli-gh to create issue with partial success.
aa090fb636c739cdfde1a89a4d3e5bcaf10cdce5 From now onwards, the timestamp follows the defaul output of date command.
476e9a2fff0df094941370556422e4e7ebabadca Finished this experiment with push and pull.
290648fa99c42e5fdfa40cbb0f1e7d63fe024839 Resolved conflict in README.md
6a81d6181cc78a49cab7edea57a57049328dea96 Not sure why there's a conflict with README.md
6ad0f27bac2eb1c869703d54e7949adbb026a8e4 Resolved Conflict: Testing Push and Pull.tx
```

That massively long string is what we want. By the way that shit is called the **commit hash** and serves like unique id for each commit.

This got me wondering if there's an easier way to get the hash. So I went diggin a little and read [Git Basics - Viewing the Commit History](https://git-scm.com/book/en/v2/Git-Basics-Viewing-the-Commit-History). I learnt that I could use `git log --pretty=format:"%h -  %cr : %s"` This will return;

```
❯ git log --pretty=format:"%h -  %cr : %s"
9812143 -  27 minutes ago : nani: Added new file to practice diff commands
f965b74 -  3 hours ago : nani: watched HEAD from the course
18924ab -  3 hours ago : nani: of workflow and good commit messages
c814ef1 -  6 hours ago : Attempted to use cli-gh to create issue with partial success.
aa090fb -  8 hours ago : From now onwards, the timestamp follows the defaul output of date command.
476e9a2 -  28 hours ago : Finished this experiment with push and pull.
290648f -  28 hours ago : Resolved conflict in README.md
6a81d61 -  28 hours ago : Not sure why there's a conflict with README.md
6ad0f27 -  28 hours ago : Resolved Conflict: Testing Push and Pull.tx
2d2a9c7 -  30 hours ago : Changed "Testing Push and Pull.txt" from GitHub
f331f21 -  30 hours ago : Added Testing Push and Pull.txt
720aec2 -  2 days ago : Tadaima, from the other branch
32d399a -  2 days ago : Preparing to create new branch
bc3ff06 -  2 days ago : Practice Add, Restore, Commit and Push.
0abda30 -  3 days ago : Getting my head around commits.
c66762a -  3 days ago : Initial commit
```

I would still have to manually type 7 characters for the hash but it's better than what I had to deal with previously.

Also, it is possible to run `git diff <branch> <branch>`. Just throwing it out there. While I now understand how to use these commands. I don't quite get when to use them practically. 

Sat 10 Dec 16:47:59 +08 2022
Watched Video: Blame from Meta's Version Control course. `git blame` is command for keeping track of who did what and when. 

The official documentation defines it as "git-blame Show what revision and author last modified each line of a file."

It returns information in the following format `<ID><Author><Time><Line Number><Content>` by default. The format of the output can be changed with some flags. The video lesson used `-l` as an example, showing that it will return a more detailed output. Though I'm not quite sure why we would want that.

I would probably need to see for practical examples of how others use git blame.

One particularly not worthy flag used in the video was the `-L` flag, which is used for specifying range. Using `git blame <filename>` will show all the revision information which can get pretty long. To narrow the scope to a few lines, we can do `git blame -L <start line>,<end line> filename`. We can use numberals or regular expressions to specify the line range. 

`git blame` is often used in conjunction with `git log`. The former will display the point where changes were made and the latter will give more detail of the change. The workflow is to use `git blame` to identify the commit id and then use it with `git log`.


After the video, I went ahead and read up the [Official Reference for Git Blame](https://git-scm.com/docs/git-blame). I've come to realised that the official reference is a better source of learning that the course itself. I find that the official reference grouped content more sensibly. For example, `git blame` is filed under Debugging, and `git log`, `git diff` are filed under Inspection and Comparison. I think it's worthwhile to go read through the official reference to get a better grasp of git. Also, [Git Immersion](https://gitimmersion.com/) provide a far better experience of follow along and learn that the course. 

Oh wells.




