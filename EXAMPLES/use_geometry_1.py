from alpha.mathlib import geometry   # load geometry.py
import sys
import os
print(f"os.getenv('PYTHONPATH'):  {os.getenv('PYTHONPATH')}")

# import math  # does not get executed

# import search algorithm
# 1. current folder
# 2. folders in PYTHONPATH  "F;F;F"  "F:F:F"
# 3. predefined folders for this version of Python


a1 = geometry.circle_area(8)
a2 = geometry.rectangle_area(10, 12)
a3 = geometry.square_area(7.9)
print(a1, a2, a3)

print(f"geometry.PI: {geometry.PI}")

# rude!
geometry._not_quite_private()
print()

for path in sys.path:
    print(path)
