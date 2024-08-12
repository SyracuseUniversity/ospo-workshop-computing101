# Exercise 5: `tar` and scripting OS operations

The file `data.tar.gz` is a compressed [archive file](https://en.wikipedia.org/wiki/Tar_(computing)) (also known as a "tarball") that contains multiple files. Archive files are convenient for sharing an entire directory of files with others. For example, tagged versions of software packages on GitHub will be downloaded as `tar.gz` archive files. (Zip files --- which typically end in `.zip` --- are another popular method for archiving files.) In this case, `data.tar.gz` contains files from a hypothetical analysis of some data.

Let's unpack it to see what it contains; run:
```
tar -xzvf data.tar.gz
```
(Here, the `x` means to "extact"; see the `man` page for `tar` if you want to know what the other flags do.) When it's done, you should have a directory called `data` that contains 24 files. The files names have the structure:
```
${NAME}_run${NUM}_${FTYPE}.${EXT}
```
where `NAME` is alpha, bravo, charlie, or delta; `NUM` is 1 or 2; `FTYPE` is results, analysis, or config, and `EXT` is ini, sh, or dat. For example, the first file in the directory is named `alpha_run1_analysis.sh`. (Note that all of these files are empty; this is the result of some pretend hypothetical analysis.)


Suppose these were the results from an analysis you did that took weeks to complete. You want to send them to your colleagues, but you don't like that all of the files are in the same directory. It makes it hard to separate out the results for a particular name. (Your colleage Otto is particularly grumpy about directory structures. The last time you sent him results like this, all he did was complain that it was hard to look at the results for Bravo.) You decide to restructure the data to make it easier for your colleagues to peruse.

1. Create a new directory called `restructured_data`.

2. Copy the results in data into `restructured_data`, but change the directory structure so that the files are stored as:
```
restructured_data/${NAME}/run${NUM}/${FTYPE}.ext
```
For example, `data/alpha_run1_analysis.sh` would be copied to `restructured_data/alpha/run1/analysis.sh`.

*Hint:* The `awk` command is useful for this. Try running `echo alpha_run1_analysis.sh | awk -F_ '{print $1}'`. What does it return?

3. Create a tarball of `restructured_data` by running:
```
tar -czvf restructured_data.tar.gz restructured_data/*
```
Note the here we provide the `c` flag (for create) instead of `x` and we have to give the name of the new tarball as the first argument.

4. Test that your new tarball is correct by creating a directory called `test`, copying `restructured_data.tar.gz` into `test`, and extracting it. You should have `test/restructured_data` with the desired directory structure.

You can now send `restructured_data.tar.gz` to Otto!

*Note: if you want to remove the directories once you're done, run*
```
rm -r restructured_data
rm -r test
rm -r data
```

-----

*If you get stuck, see `.solution` for a solution to this problem.*
