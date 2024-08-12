# Exercise 3: search and replace

**This exercise has multiple parts. Solutions to each part can be found in the files `.solutionX` where `X` corresponds to the part.**

The file `names.txt` contains a list of 50 names in random order, preceeded by a count.

Do the following:

1. Make a copy of `names.txt`; call the copy `names-seven.txt`. Next, use `sed` to replace all instances of the number `7` with the word `seven`. Do the replacement in place, so that `names-seven.txt` has the `7` replaced.

2. Make a copy of `names.txt`; call the copy `names-mod.txt`. Use `vim` to remove all the leading numbers in `names-mod.txt`, then save the changes.

3. Sort the names in `names-mod.txt` by alphabetical order and write the output to `names-sorted.txt`. *Hint:* `bash` *has a command called* `sort`. *Run* `man sort` *to see how it works.*

4. (Challenge) Write a single-line bash command that, starting with `names.txt`, will remove the leading numbers and sort the names alphabetically, writing the result out to `names-sorted2.txt`. The original `names.txt` should remain unchanged. Check that `names-sorted.txt` and `names-sorted2.txt` are the same by running
  ```
  diff names-sorted.txt names-sorted2.txt
  ```
  There should be no differences between them.
