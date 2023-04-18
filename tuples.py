
person = "Bill", "Gates", "Microsoft", "1955-10-28"

x = {1, 2, 3}  # set
x = [1, 2, 3]  # list
x = 1, 2, 3    # tuple   also x = (1, 2, 3)
m = 5,  # tuple with one value
n = ()  # tuple with zero values

print(f"person: {person}")
print(f"person[0]: {person[0]}")
print(f"person[1]: {person[1]}")

first_name, last_name, product, dob = person   # iterable unpacking
print(first_name, last_name)
print()

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

print(f"people[0]: {people[0]}")
print(f"people[0][0]: {people[0][0]}")
print(f"people[0][0][0]: {people[0][0][0]}")

for person in people:
    print(person)
print('-' * 60)

for first_name, last_name, product, dob in people:
    #  first_name, last_name, product, dob = next-value-of-people
    print(f"{first_name:8s} {last_name}")
print('-' * 60)

info = [('NC', 'Raleigh'), ('MD', 'Annapolis'), ('CA', 'Sacramento')]

for state, capital in info:
    print(f"{capital:10s} {state}")


values = ['alpha', 'bravo' 'charlie', 'delta', 'echo', 'foxtrot']

x, y, *z = values
print(x, y, z)

x, *y, z = values
print(x, y, z)

*x, y, z = values
print(x, y, z)
