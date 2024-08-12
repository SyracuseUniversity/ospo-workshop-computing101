# Exercise 1: Evaluting Conditionals

Write a bash script named `greeting` that greets you with `${SALUTATION} ${USER}!` when it is run. Here `${USER}` is the current username and `${SALUTATION}` depends on a `TIME` variable. The `${SALUTATION}` should be:
  * `Good morning` if the `TIME` is between 5:00 and 11:59;
  * `Good afternoon` if the `TIME` is between 12:00 and 16:59;
  * `Good evening` if the `TIME` is between 17:00 and 23:59;
  * `Go to bed` if the `TIME` is between 00:00 and 4:59.
The script should take the `TIME` variable as optional input. If the `TIME` is given, then the salutation should be based on that. If the `TIME` is not given, then it should use the current time.

For example, if it is currently 15:42 then running:
```
$ bash greeting
```
should yield
```
Good afternoon <username>!
```
while running
```
$ bash greeting 10:00
```
should yield
```
Good morning <username>!
```
regardless of the current time.

Hints:
  * For this you'll need to use if statements. Note that you only need to base the conditional on the current hour; the minutes are irrelevant. For a good primer on conditional statements in bash, see [this website](https://acloudguru.com/blog/engineering/conditions-in-bash-scripting-if-statements).
  * To get the current time, use the `date` command. In particular, `date +%H` will return the current hour (try it!).
  * You'll also need to be able to parse command-line inputs with your script. There are a few different ways to do that. [This website](https://www.baeldung.com/linux/use-command-line-arguments-in-bash-script) is a good tutorial on how to do that.

*Bonus challenge:* have the script print an error message and exit with code 1 if a time that is not between 00:00 and 23:59 is provided. Google "bash exit codes" for more details. 

*If you get stuck, see `.solution` for a solution.*
