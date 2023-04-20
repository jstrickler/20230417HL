# 1. doc strings
# 2. shared code
# 3. convenience imports
'''
This is a demo package.

A real package would have a real docstring
'''
import math

PI = math.pi  # available as alpha.PI

from alpha.mathlib.geometry import circle_area

__all__ = ['mathlib', 'dbutil']  #  what to import when using 'import *'
