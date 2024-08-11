## Exercise 2: Permissions and setting environment variables

1. Create a directory called `bin` in your repository and copy the `greeting` script you created in Exercise 1 into there. 
   **Note**: if you skipped Exercise 1, or were unable to complete it, copy `exercise1/.solution` (and rename it `greeting`) instead.
2. Make sure the interpreter instruction `#!/usr/bin/env bash` is at the top of your `greeting` script, in case you did not do that in Exercise 1.
3. Change the permissions on `greeting` so that it is an executable.
4. Make another directory in your repository called `etc`. In that directory, create a bash script called `srcgreeting.sh` that prepends the `bin` directory to your `PATH` environment variable. By prepend, I mean it should be at the beginning of the list of possible paths in `PATH`. Note that you must use the `bin` directory's absolute path when adding it to the `PATH` variable.
5. Source `srcgreeting.sh` so that your PATH variable is updated.
6. Test that it works by running:
```
$ which greeting
$ greeting
```
   The first command should return the absoluate path to your `greeting` script, while the second should return the output of `greeting`.

*If you get stuck, see `.solution` for the answer.*
