# Exercise 2: Permissions and setting environment variables

-------------------------------------------------------------------------------
*Note:* This exercise depends on completing Exercise 1. If you did not complete
Exercise 1, just copy the `.solution` file there and call it `greeting`. In
other words, do the following (assuming you are currently in this directory):
```
cp ../exercise1/.solution ../exercise1/greeting
```
You can then do this exercise.

-------------------------------------------------------------------------------

1. Create a directory called `bin` in your repository and copy the `greeting` script you created in Exercise 1 into there. 
2. Make sure the interpreter instruction `#!/usr/bin/env bash` is at the top of your `greeting` script, in case you did not do that in Exercise 1.
3. Change the permissions on `greeting` so that it is an executable.
4. Make another directory in your repository called `etc`. In that directory, create a bash script called `srcgreeting.sh` that prepends the `bin` directory to your `PATH` environment variable. By prepend, I mean it should be at the beginning of the list of possible paths in `PATH`. Note that you must use the `bin` directory's absolute path when adding it to the `PATH` variable.
5. Source `srcgreeting.sh` so that your PATH variable is updated.
6. Test that it works by running:
```
$ which greeting
$ greeting
```
   The first command should return the absolute path to your `greeting` script, while the second should return the output of `greeting`.

*If you get stuck, see `.solution`.*
