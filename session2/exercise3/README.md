## Exercise 3: Using a for loop

-------------------------------------------------------------------------------
*Note:* This exercise depends on completing Exercise 2. If you have not
completed Exercise 2, you can just use the solution given there by running:
```
bash ../exercise2/.solution
```
You can then do this exercise.
-------------------------------------------------------------------------------

The file `test_times.txt` contains a list of times. Write a script called `test_greeting.sh` that uses a `for` loop to cycle over the times listed in `test_times.txt` and runs your `greeting` script for that time. For each time in `test_times.txt` it should print the time to screen followed by the output of `greeting $time`. In other words the output of `test_greeting.sh` should look something like:
```
$ bash test_greeting.sh
7:19 Good morning <username>!
13:44 Good afternoon <username>!
19:00 Good evening <username>!
2:57 Go to bed <username>!
```
where `<username>` is your username.

*If you get stuck, see `.solution` for the answer.*
