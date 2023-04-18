fruits = ['pomegranate', 'cherry', 'apricot', 'apple',
'lemon', 'kiwi', 'orange', 'lime', 'watermelon', 'guava',
'papaya', 'fig', 'pear', 'banana', 'tamarind', 'persimmon',
'elderberry', 'peach', 'blueberry', 'lychee', 'grape', 'date' ]

f0 = []
for f in fruits:
    result = f.upper()
    f0.append(result)
print(f"f0: {f0}\n")

#      result            iterable
f1 = [f.upper() for f in fruits]   # list comprehension
print(f"f1: {f1}\n")

#  results = [obj.attr for obj in list_of_objs]

f2 = [f.upper() for f in fruits if f.startswith('p')]
print(f"f2: {f2}\n")

#  select or modify elements into a new list
f3 = [f for f in fruits if f.startswith('a')]
print(f"f3: {f3}\n")

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'), 
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Grace', 'Hopper', 'COBOL', '1906-12-09'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Thomas', 'Kurtz', 'BASIC', '1928-02-28'),
    ('Ada', 'Lovelace', 'Analytical Engine', '1815-12-10'),
    ('Grace', 'Hopper', 'COBOL', '1906-12-09'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

dobs = [p[-1] for p in people]
print(f"dobs: {dobs}\n")

names = [(p[0], p[1]) for p in people]
print(f"names: {names}\n")

ranks = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
suits = 'Clubs Diamonds Hearts Spades'.split()

cards = [(r, s) for s in suits for r in ranks]
print(f"cards: {cards}\n")

f4 = [f.upper() for f in fruits if f.startswith('p') if len(f) > 6]
print(f"f4: {f4}\n")

fruit_gen = (f.upper() for f in fruits if f.startswith('p'))
print(f"fruit_gen: {fruit_gen}\n")
for fruit in fruit_gen:
    print(fruit)

# gen = (x for x in iterable ...)     generator expressions
# list = [x for x in iterable ...]    list comprehension
# dict = {k, v for x in iterable ... }  dictionary comprehension
# set = {x for x in iterable ...}     set comprehension

