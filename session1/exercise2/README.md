# Exercise 2: vim practice

The file `add.py` is a Python script, but it's broken! The script should define a function `add()` that takes in two numbers and returns their sum. But there are two problems with it: the two lines following the `def` should be indented, and `return` should precede `a+b`; i.e., it should look like this:

```python
def add(a, b):
    """Function that adds a and b."""
    return a+b
```

To fix this, use `vim` to open `add.py` and:

1. Indent the two lines following the `def` line (but not the `print` line). Try to use line highlight mode to do this.

2. Use insert mode to add the word `return` before the `a+b`.

3. Save and exit the file. Then test it by running `python add.py`; `2` should be printed to the screen.

4. Modify `add.py` and add another print line that adds `2+3`; i.e., add `print(2, 3)` on a new line, after the `print(1, 1)` line. Do this by copying and pasting the `print(1, 1)` line, then using replace mode to overwrite the `1`, `1`. Save and exit, then test by running `python add.py`. You should get:
```
2
5
```
