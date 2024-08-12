# Exercise 4: Using `conda` and `mamba` to create environments and install packages.

*Note: This task requires that you have conda installed already. Follow the instructions in `../README.md` to do that if you have not done so already.*

1. Create a conda environment called `conda-test`.

2. Activate your `conda-test` environment and install `numpy` into it.

3. Print your `$PATH`; you should see that the first couple of paths point to a conda directory with the name of your environment (`conda-test`) in it.

4. See what version of Python and numpy you installed by running the included `check_versions.py` script:
```
./check_versions.py
```
   This will print out the current time followed by the versions of Python and numpy you are using.

5. Suppose that you need to use an older version of Python and numpy for a project. Create another conda environment called `conda-test2` and install Python version 3.9 and numpy 1.24.1 into it.

6. Activate `conda-test2` and run check versions to vrify that you have the desired versions.

7. Miniforge comes with a faster re-implementation of `conda` called `mamba`. Generally, you can use `mamba` in the same way you use `conda` -- it takes the same arguments -- just replace `conda` with `mamba`. Redo steps 1-6 using `mamba` (call the environments `mamba-test` and `mamba-test2`). Is it faster?

8. Different repositories or "[channels](https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/channels.html)" exist within the conda ecosystem from which you can download and install packages. The default channel for Miniforge is the [conda-forge](https://conda-forge.org/) channel. Generally, conda-forge has many of the packages you will need. However, there are some specialized packages that you need to go to other channels to download. For example, the [Bioconda](https://bioconda.github.io/) contains many packages that are used in biomedical research. Let's illustrate that by trying to install the [gofast](https://github.com/virus-evolution/gofasta) package. Lets start by searching for the package. Run:
```
mamba search gofasta
```
(*Note: here and below I'll use `mamba`, but you can use `conda` instead.*) You should get `No match found for: gofasta` followed by suggestions of what else to do. The package couldn't be found because your installation of mamba/conda searches `conda-forge` by default, but `gofasta` is not in conda-forge.

9. Let's search the `bioconda` channel instead. Run:
```
mamba search -c bioconda gofasta
```
You should see that `gofasta` is available, along with the version.

10. Create an environment called `biotest` and install `gofasta` in it using the `bioconda` channel. (You can specify the channel for `mamba create` and/or `mamba install` using the `-c` flag, just as we did the in search command above.)

11. Activate the `bioconda` channel and test that `gofasta` is installed by running:
```
gofasta --help
```
You should get a help message giving information about `gofasta`.

12. Lets uninstall some of the environments we created to save space. You can see all the environments you have installed by running:
```
mamba info --envs
```
Let's uninstall the conda-test environment. First, if you are not in the base environment, go to it by running `mamba deactivate`. This will take you to your last active environment. Keep deactivating until you see `(base)` on the left of the prompt. Alternatively, just type `mamba activate` (with no environment name) to go directly to the `base` environment. Now let's remove the `conda-test` environment by running:
```
mamba remove --all -n conda-test
```
Now run `mamba info --envs` again to check that the environment is installed. Repeat for any other environments you'd like to remove.
