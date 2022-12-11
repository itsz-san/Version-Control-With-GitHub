It would seem that that version of the cli-gh on Ubuntu's Advanced Packaging Tool(APT) is outdated. We could check it via running `apt info gh`. When I ran this, I found that the version number is `2.4.0+dfsg1-2`. The latest version, as of the time of this writing, is `2.20.2`. You can find the latest version at their [release page](https://github.com/cli/cli/releases).

## Context
Actually, to say that the version is outdated is an understatement. It's a good idea to update and install the latest version to get all the new improvements. My motivation to update is to get access to new commands, particularly `gh issue develop`.

Currently, my workflow for using cli-gh is as follow
```
gh issue list

Showing 3 of 3 open issues in itsz-san/Version-Control-With-GitHub

#3  Add GitHub CLI                     about 18 minutes ago
#2  [Feature] Improve...  enhancement  about 2 days ago
#1  [Feature] File Fo...  enhancement  about 2 days ago

gh issue develop --checkout 3
```

The `gh issue develop --checkout 3` command will create a new branch from the current branch and associate the branch for that particular issue.

## Installation Instructions
The installation instructions can be found [here](https://github.com/cli/cli/blob/trunk/docs/install_linux.md). But essentially, we just have to run;

```
type -p curl >/dev/null || sudo apt install curl -y
curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg \
&& sudo chmod go+r /usr/share/keyrings/githubcli-archive-keyring.gpg \
&& echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null \
&& sudo apt update \
&& sudo apt install gh -y
```

I'm actually not sure if running `sudo apt update` will update `gh` to the latest version from now on. So, I decided to write the above code as a bash script. That way, I can just run it whenever I want to update. Or at least that's the idea

The `gh issue develop --checkout 3` command will create a new branch from the current branch and associate the branch for that particular issue.

## Installation Instructions
The installation instructions can be found [here](https://github.com/cli/cli/blob/trunk/docs/install_linux.md). But essentially, we just have to run;

```
type -p curl >/dev/null || sudo apt install curl -y
curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg \
&& sudo chmod go+r /usr/share/keyrings/githubcli-archive-keyring.gpg \
&& echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null \
&& sudo apt update \
&& sudo apt install gh -y
```

I'm actually not sure if running `sudo apt update` will update `gh` to the latest version from now on. So, I decided to write the above code as a bash script. That way, I can just run it whenever I want to update. Or at least that's the idea.
