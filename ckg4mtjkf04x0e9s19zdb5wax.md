## scp command in Linux 💻

Secure Copy command or simply known as a "scp" command is a command-line utility that allows you to securely copy files and directories between two locations.

Using scp, you can copy a file:

- From your local system to a remote system.
- From a remote system to your local system.

When transferring data with scp, the file is encrypted so that anything sensitive will not get tampered on the way.

In this tutorial, we will see how we can use the scp command through practical examples, its alternative command - rsync, differences between these two commands & where to prefer one over the other.

![lin_meme_1.jpg](https://cdn.hashnode.com/res/hashnode/image/upload/v1602389177212/7HUGLyS8J.jpeg)

# scp Command Syntax

The scp command syntax looks like this:

```
scp <OPTION> source_file_name username@destination_host:destination_folder
```

Where OPTION is [scp options](https://linux.die.net/man/1/scp) such as :

-P : Specifies the remote host ssh port.

-p : Preserves files modification and access times.

-q : Option to suppress the progress meter and non-error messages.

-C : Option for compressing the data as it is sent to the destination machine.

-r : Option to copy directories recursively.

–v : Verbose mode. Option to print debugging messages about their progress. This is helpful in debugging connection, authentication, and configuration problems.


Note that the scp command relies on ssh for data transfer, so it requires an ssh key or password to authenticate on the remote systems. 
Also in order to copy files, you must have read permissions on the source file and write permission on the destination system.

# Copy a Local File to a Remote System

To copy a file from a local to a remote system run the following command:

```scp <fileName.txt> <remote_username>@<remote_ip_address>:<absolute_path>```


Where fileName.txt is the name of the file we want to copy, remote_username is the user on the remote server, remote_ip_address is the server IP address. The absolute_path is the path to the directory you want to copy the file to. If you do not specify any remote directory, the file will be copied to the remote user home directory.

You will be prompted to enter the user password, post which the transfer process will start.
```
ubuntuadmin@10.176.144.9's password:
example.txt                             100%    0     0.0KB/s   00:00
```
If you want to save the file under a different name, you need to specify the new file name:

```
scp file.txt remote_username@10.10.0.2:/remote/directory/newfilename.txt
```
If SSH on the remote host is listening on a port other than the default 22 then you can specify the port using the -P argument:

```
scp -P 2322 file.txt remote_username@10.10.0.2:/remote/directory
```
The command to copy a directory is similar to copying files. The only difference is that you need to use the -r flag for recursive.

To copy a directory from a local to remote system, use the -r option:

```
scp -r /local/directory remote_username@10.10.0.2:/remote/directory
```

# rsync Command

rsync is also a command-line utility for synchronizing files between two locations over a remote shell. It provides faster file transfer by transferring only the differences between the source and the destination.

rsync can be used for incremental backups, copying files between systems, and as a replacement for scp , sftp , and cp commands.

It also has a simple syntax :
```
rsync <OPTION> dir1/ dir2
```

where in option we can use  '-r' which means recursive, which is necessary for directory syncing.

We could also use the -a flag instead.

The -a option is a combination flag. It stands for “archive” and syncs recursively and preserves symbolic links, group, owner, and permissions. It is more commonly used than -r. If you want to explore more options consider giving [this](https://linux.die.net/man/1/rsync) a read

# So what's the difference between SCP and Rsync 🤔

1. scp copies files from local machine to a remote machine over a secure SSH connection. Whereas rsync allows you to syncronise remote folders.

2. scp basically reads the source file and writes it to the destination. It performs a linear copy, locally, or over a network.
rsync also copies files locally or over a network. But it uses a special delta transfer algorithm and a few optimizations to make the operation a lot faster. 

3. scp is always secure, whereas rsync must travel over SSH to be secure.

4. If you want to transfer large files, and if the transfer is disconnected before completion, rsync will pick it up where it left off. Whereas scp doesn't. Therefore use scp if you want to transfer couple of files or directories and go with rsync for multi GB size data.

5. rsync compares the files at each end and transfers only the changed parts of changed files. When you transfer files the first timeo it behaves pretty much like scp, but for a second transfer, where most files are unchanged, it will push a lot less data than scp. It's also a convenient way to restart failed transfers - you just reissue the same command and it will pick up where it left off the time before, whereas scp will start again from scratch.

In summary, use scp for your everyday tasks as It's simpler to use.
For recurring tasks, like cron jobs, use rsync. As mentioned, on multiple invocations it will take advantage of data already transferred, performing very quickly and saving on resources. It is an excellent tool to keep two directories synchronized over a network.
Also, when dealing with large files, use rsync with the -P option. If the transfer is interrupted, you can resume it where it stopped by reissuing the command.

![lin_meme.jpg](https://cdn.hashnode.com/res/hashnode/image/upload/v1602389197680/a1p8kwlv-.jpeg)

# Other articles you may like 😊

- [Different ways to authenticate your APIs](https://apoorvtyagi.tech/different-ways-to-authenticate-your-apis) - Learn about some common ways to secure you APIs access.
- [Understanding Linear Regression](https://apoorvtyagi.tech/understanding-linear-regression) - One of the most popular algorithm in machine learning that every data scientist should know.
- [GIT INIT (Part-1)](https://apoorvtyagi.tech/git-init-part-1) - A series on GIT for beginners.
- [Bitcoin Mining](https://apoorvtyagi.tech/let-us-mine) -  Learn about what exactly happens in bitcoin mining.
- [Improving Time Complexity](https://apoorvtyagi.tech/improving-time-complexity) - Understanding how to improve the time complexity of your code