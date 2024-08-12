#!/usr/bin/env python
import time
import platform
import numpy
current = time.time()
print("Current time: ", current)
print("Python version: ", platform.python_version())
npvers = numpy.__version__
print("Numpy version: ", npvers)
