import math
import sys

def get_message():
    return "Hello, HL world"

msg = get_message()
print(f"msg: {msg}")

def display_message():
    message = get_message()
    print(message)

result = display_message()
print(f"result: {result}")

def hello(whom="world"):
    print(f"Hello, {whom}")

hello("world")
hello("HL")
hello()

def circle_area(diameter):
    radius = diameter / 2
    return math.pi * radius ** 2

x = circle_area(10)
print(f"x: {x}")

def double(thing):
    return thing * 2

print(f"double(5): {double(5)}")
print(f"double(8.97): {double(8.97)}")
print(f"double('mint'): {double('mint')}")

def double(thing1, thing2):
    return 2 * (thing1 + thing2)

print(f"double(5, 10): {double(5, 10)}")
print(f"double('nana', 'batman'): {double('nana', 'batman')}")

b = 100

def spam():
    print(f"x: {x}")
    
    b = 20
    return b

def ham():
    b = 30
    c = spam()
    print(f"b: {b}")
    print(f"c: {c}")

ham()
print(f"b: {b}")
 
m = 10

abc = "foo"

def changeit(param: int):
    # if not isinstance(param, int):
    #     raise TypeError('param should be an int')
    return param * 10

m = changeit(m)
m = changeit(abc)

fruit = "mango"

def apple(color):
    def print(*args, **kwargs):
        sys.stdout.write("HA HA HA\n")
    shape = "round"
    def banana():
        fruit = "banana"
        shape = 'square'
        print(f"the {shape} {fruit} is {color}")
    
    return banana

#  local -> nonlocal -> (file)global -> builtin

f = apple('pink')
f()
f = apple("blue")
f()




def grep(search_term, *file_paths):
    for file_path in file_paths:
        with open(file_path) as file_in:
            for raw_line in file_in:
                if search_term in raw_line:
                    print(f"{file_path} {raw_line.rstrip()}")


grep('rabbit', '../DATA/alice.txt', '../DATA/words.txt')
print('-' * 60)
grep('wombat')

# not for day-to-day coding
def generic(*args, **kwargs):
    print(args)
    print(kwargs)

generic(1, 2, 3, 4, 5, color="blue", country="Burkina Faso")


















