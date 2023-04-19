import logging

logging.basicConfig(
    filename="hl.log",
    level=logging.DEBUG,
)

FILE_PATH = "DATA/wombats.txt"

try:
    with open(FILE_PATH) as file_in:
        for line in file_in:
            print(line.rstrip())
except FileNotFoundError as err:
    logging.exception(err)


with open('DATA/breakfast.txt') as food_in:
    food_list = food_in.read().splitlines()
    print(f"food_list: {food_list}")
    print()
    try:
        print(dict(food_list))
        print(f"food_list[99]: {food_list[99]}")
    except IndexError as err:
        print(err)
    except ValueError as err:
        print(err)


result = None
numbers = [0, 0,  5, 8, 0, 19, "47", 12, 0, 7, -3, 4]
for n in numbers:
    try:
        logging.debug("processing number %s", n)
        result = 35 / n
    except (TypeError, ZeroDivisionError) as err:
        print(err)
        break
    else:
        print(result)

print(f"result: {result}")

import sqlite3

conn = None
try:
    with sqlite3.connect('wombatland/cheeseworld/spam.db') as conn:
        cursor = conn.cursor()
except sqlite3.OperationalError as err:
    print(err)
else:
    pass
    # execute SQL here ...
finally:
    if conn is not None:
        conn.close()






print("ALL DONE")
    