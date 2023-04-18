
words = ["dog", "bites", "man"]

rev = reversed(words)

print(f"rev: {rev}")
for word in rev:
    print(word)
print()

print("round 2:")
for word in rev:
    print(word)

rev = reversed(words)
print(list(rev))
print(list(rev))
print()

first_names = ["Billy", 'Sierra', 'Molly']
last_names = ['Strings', 'Hull', 'Tuttle']
colors = ['pink', 'orange', 'brown', 'purple', 'blue']

names = zip(first_names, last_names, colors)
for name in names:
    print(name)
print()


