# Exercise 1: A simple bash script

In this exercise you're going to write a script to count the number of occurances of the word "here" in the Gettysburg Address. This is a speech given by President Lincoln on November 19, 1863 at the dedication of the Gettysburg National Cemetary. It is one of the most famous and signficant speeches in American history. 

1. The speech is in the file `gettysburg_address.txt`. View the text of the speech using cat. If you're not sure how to use cat, type `man cat`.

2. The program `grep` can be used to search one or more files for the occurance of a word. To illustrate that, try the following:
```
$ grep "here" gettysburg_address.txt 
```
   Note the output: grep returns a line for each instance of "here" that it found in the file. The number of lines returned by `grep` therfore gives the number of occurances of the word "here". (You can verify this yourself by using `cat` to print the file and manually count.)

3. You could just count the number of lines now to get the number of times "here" appears, but let's do this more progrmattically. For that, we'll use the program `wc` (= word count), which can count the number of occurances of a word, line, or characters in a file. What it reports depends on what arguments you give it. Run:
```
wc -l gettysburg_address.txt
```
  You'll get a number back. What does the `-l` do? (Check the `man` page for `wc` if you're not sure.)

4. Above, we gave `wc` the `gettysburg_address.txt` file as input. However, `wc`, like all UNIX programs, can take as input the output of another program. This is done by using the *pipe* operator `|`. For example, run:
```
cat gettysburg_address.txt | wc -l
```
   Note that you get the same value as you got when you ran `wc` directly on the file.

5. Based on what you observed in 1 and 3, write a one-line bash script that uses `grep` and `wc` to to count the number of occurances of "here" in the Gettysburg Address file.

6. Put what you wrote in 4 into a bash script file called `count_here.sh`. To do this, use `vim`, or your favorite text editor. After saving the script, test it by running:
```
bash count_here.sh
```
   Do you get the same output as you did in 4?

7. Let's save the output from your script by redirecting it to a new file. For that we'll use the bash redirection operator `>`. Run:
```
bash count_here.sh > count_here.out
```
   This causes the output of `count_here.sh` to be written to the file `count_here.out`. Verify that by running `cat count_here.out`.

**If you get stuck, you can find the solution in the hidden file `.solution.sh`!**
