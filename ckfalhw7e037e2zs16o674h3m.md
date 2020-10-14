## GIT INIT (Part-1)

![image.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1599902724355/1ycJ0dNeZ.png)

**Git ** for software engineers is a must if you want to collaborate on a working project. Yes, there are other tools for collaborations & version control but git is the most famous tool out there.

Git can be used for various reasons like :

***- Collaboration***

***- Software Version Controling*** 

***- Tracking issues***

***- Code reusability***


There are also many other common terms associated with git which you should be aware of, these are actually the terms i come across everyday while working with git, let's have a look at them first.

## **Terminologies**

**Repository ** - The digital storage where all your files are stored.

**Commit ** - Whenever you make any significant changes in a code you create a snapshot of it. This a called a commit.

**Snapshot ** - It records all your files at a given point of time so that you can look up at them anytime later.

**Branch ** - Git follows a tree like analogy for keeping track of code, when several people are collaborating on a project, the general procedure is to make a branch from the master branch, do the changes there and make a request to the master branch to merge the code.

**Head ** - The reference to the most recent commit is called Head.

**Pull Request** - Every change is being recorded in form of snapshots which helps tracking of code. Now, whenever you want to make a change, you make a new branch make changes and submit the code to be merged, this submission can be done through a pull request(PR) or a merge request(MR)

**Cherry Picking** - Cherry picking is the way to apply some commit from one branch into another branch. For eg : if you you've committed a change into the wrong branch, but do not want to merge the whole branch. You can revert the commit and cherry-pick it on another branch.

**Clone** - Clone is used to make a copy of the target repository. If I want a local copy of my repository from GitHub, i would have to write *git clone <repository_url>*
 
**Origin** - In Git, origin is a reference to the remote repository from a project was initially cloned.

**Stash** - This is one my favorite, as i always get into a situation where i want to switch the branches, but i am also working on an incomplete part of my current project. In this case i don't want to make a commit of half-done work. Git stashing allows you to do so. The git stash command enables you to switch branch without committing the current branch.


Those 10 above were some of the common terms that you will hear & see everyday while working with git.
Now, let's GIT going and have a look at the most common but important git commands that will set you up for your first contribution.(I am assuming you all have some prior git experience & have already setup & configured your git bash)

## **GIT Commands**

Let's say you have your project files in a folder on your PC & you want upload those to your git repo, follow these steps:

>git init

This means we have initialized a local repository in that directory

>git remote add origin <repo link>

Doing this we now have connect our repository with the remote git repository


Now that your local folder is all set up & configured with the remote repository, it's time to upload your files.
This can be done with the following commands:

>git status

> git add [file name] or git add .
 
>git commit -m [commit message]

>git push -u origin master

The above 4 commands are just enough to do your first contribution.

- *git status* will lists all new or modified files which are not 
already commited

- *git add [filename]* will take the snapshots of all files. Also instead of adding the files individually, we can add all of them by adding a .(dot) after add

- *git diff --staged* will let you see the changes you made in the file as compared to previous version

- *git commit -m [commit message]* will Records file snapshots permanently in the version history. Here -m is the message flag, whenever we commit our changes, we've to add a message along with it.

- *git push -u [remote] [branch]* will push your changes to the specified branch (your current branch by default) of remote (origin by default). Here -u stands for upstream.
![image.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1599908417856/0EmyJ_DqY.png)

## **Get More GIT**

These were some basic git stuffs, we will move on to little advance topics like branching in the next part of this git series.

## **Other articles that you might like**

- [Bitcoin Mining](https://apoorvtyagi.tech/let-us-mine) -  Learn about what exactly bitcoin mining is.
- [Improving Time Complexity](https://apoorvtyagi.tech/improving-time-complexity) - Understanding how to improve the time complexity of your code.
- [GPT-3](https://apoorvtyagi.tech/gpt3) - A large open source state-of- 
   the-art language model with more than 175 billion parameters by 
   OpenAI. 
