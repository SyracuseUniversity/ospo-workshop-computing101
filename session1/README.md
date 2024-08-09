# Session 1

## Task 1: Basic bash navigation

1. Open up the terminal.

   *Windows users:* Open the terminal by clicking on the Windows/Start Menu, then selecting `Ubuntu`. This will open an Ubuntu terminal window on your computer.

2. When you open the terminal, by default you are placed into your home folder. Check this fact by using the Unix command `pwd` (= print working directory):
```
$ pwd
```
   
   *Note:* Here, `$ ` signifies the command-line prompt and does not need to be typed. Depending on your OS, you may have a `% ` instead: this is what's used for zsh, which is the (new) default terminal in MacOS.

3. Use the Unix command `ls` (= list) to inspect what files and subfolders are in your home directory:
```
$ ls
``` 

Now, as a sanity check, open up your file explorer (the GUI you typically use to view files) and check that you see all the files which are listed with the `ls` command.

   *Windows users:* Your "Ubuntu" OS is in a Windows directory that simulates a full Ubuntu system. There are two ways to view this in a GUI: (1) Type `explorer.exe .` in your terminal window; (2) Open File Explorer from within Windows and navigate to `\\wsl$`.
   
4. Let's create a directory to store your work for this workshop. To do that we will use the `mkdir` command, which creates a directory in your home directory.
```
mkdir computing101
```
   If you type `ls` you should now see the directory; it will also have appeared in your GUI view of your home directory.

5. Navigate into your new directory by using the Unix command `cd` (= change directory):
```
cd computing101
```
  We're going to do all of our work here.

6. Before continuing, notice that you can go up one directory level using `..`:
```
cd ..
```
   Verify that you're back in your home directory by typing `pwd`. In general, `..` refers to the directory one up from where you are, while `.` refers to the current directory. This works with both `cd` and `ls`. For example, you can check what is in the directory above your home directory by typing:
```
ls ..
```
  You can also check what is in the `computing101` directory by typing:
 ```
 ls ./computing101
 ```
 
 7. *Using tab complete*: Now let's go back into our `computing101` directory. However, instead of typing out the full folder name (which can get tedious), we'll use the "tab complete" functionality of bash. Type `cd <tab>`; here `<tab>` means hit the "Tab" key on your keyboard (don't type `<tab>`!). What happens? There are a couple of possibilities:
   * If you have no other files or folders in your home directory, then bash will automatically fill in `computing101` in the command line, giving you `cd computing101`.
   * If you have more than one file or folder in your directory, you will get a chime sound or your terminal will flash. In that case, hit the `<tab>` key again. You will now see all files and folders in the directory (it's like typing `ls`). Now type the first few unique letters of the folder you want to go into, followed by the `<tab>` key. For example, if you have no other file or folder that starts with a `d` simply type `d<tab>`, and bash will automatically fill in `cd computing101`. If you have more than one file or folder that starts with `d` in the directory, then you'll get the chime/flash again. If you hit `<tab>` again, then bash will now show you every file and folder in the directory that starts with `d`. Keep doing this until you get the `computing101` folder to show up.

   **Note how tab complete works**: If you hit `<tab>` bash will try to finish whatever you've typed with what's in the directory. If there is not a unique file or folder that matches what you've typed so far, you will get a chime/flash. You can then type more letters of the file or folder you want and hit `<tab>` again to fill it in, or hit `<tab>` twice to see the possibilities. Using tab in this way can save you lots of time, especially if you have long file names!

8. Use tab complete until you have `cd computing101` on the command line. Then hit enter to move back into the `computing101` directory.

## Task 2: A simple bash script (6 points)

Now let's use some bash tools with our data. We're going to do the relatively simple task of counting the number of occurances of the word "here" in the Gettysburg Address.

1. The program `grep` can be used to search one or more files for the occurance of a word. To illustrate that, try the following:
```
$ grep "here" gettysburg_address.txt 
```
   Note the output: grep returns a line for each instance of "here" that it found in the file. The number of lines returned by `grep` therfore gives the number of occurances of the word "here". (You can verify this yourself by using `cat` to print the file and manually count.)

2. You could just count the number of lines now to get the number of times "here" appears, but let's do this more progrmattically. For that, we'll use the program `wc` (= word count), which can count the number of occurances of a word, line, or characters in a file. What it reports depends on what arguments you give it. Run:
```
wc -l gettysburg_address.txt
```
  You'll get a number back. What does the `-l` do? (Check the `man` page for `wc` if you're not sure.)

3. Above, we gave `wc` the `gettysburg_address.txt` file as input. However, `wc`, like all UNIX programs, can take as input the output of another program. This is done by using the *pipe* operator `|`. For example, run:
```
cat gettysburg_address.txt | wc -l
```
   Note that you get the same value as you got when you ran `wc` directly on the file.

4. Based on what you observed in 1 and 3, write a one-line bash script that uses `grep` and `wc` to to count the number of occurances of "here" in the Gettysburg Address file.

5. Put what you wrote in 4 into a bash script file called `count_here.sh`. To do this, use `vim`, or your favorite text editor. After saving the script, test it by running:
```
bash count_here.sh
```
   Do you get the same output as you did in 4?

6. Let's save the output from your script by redirecting it to a new file. For that we'll use the bash redirection operator `>`. Run:
```
bash count_here.sh > count_here.out
```
   This causes the output of `count_here.sh` to be written to the file `count_here.out`. Verify that by running `cat count_here.out`.
