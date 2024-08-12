# Session 2: More `bash`, Environments, and Conda

**Purpose**: Learn about UNIX permissions, variables, and environments.

### Pre-requisite: Install `conda`

Exercise 4 needs `conda` to be installed. There are several different ways to install `conda` (Anaconda, Miniconda, Miniforge); we will use [Miniforge](https://github.com/conda-forge/miniforge?tab=readme-ov-file). To install, do the following:

1. From your home directory, run
```
wget "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"
bash Miniforge3-$(uname)-$(uname -m).sh
```
The first command (`wget`) will download the installer script you need to install `conda`; the second script installs it.

2. Follow the onscreen instructions. It's best to answer "yes" to all the prompts: this will install `conda` to the default location (`~/miniforge3`) and will cause conda to be active everytime you open up a terminal.

3. Open a new terminal window for the installation to take effect. If the installation was successful, you should see `(base)` to the left of your command prompt. This means that you're in the `base` environment.

## Exercises

* [Exercise 1: Evaluating Conditionals](exercise1)
* [Exercise 2: Permissions and setting environment variables](exercise2)
* [Exercise 3: Using a `for` loop](exercise3)
* [Exercise 4: Using conda and mamba to create environments and install packages](exercise4)
* [Exercise 5: `tar` and scripting OS operations](exercise5)
