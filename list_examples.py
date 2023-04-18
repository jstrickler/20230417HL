list1 = list() # empty list
print(f"list1: {list1}")
list2 = ['red', 'brown', 'purple', 'orange']
print(f"list2: {list2}")
list3 = []   # empty list
print(f"list3: {list3}")
print()

cities = ['Dubai', 'Los Angeles', 'Silver Spring', 'Durham']
print(f"cities: {cities}")
print(f"cities[2]: {cities[2]}")
cities.insert(0, 'New York')
print(f"cities: {cities}")
cities.insert(2, 'Tokyo')
print(f"cities: {cities}")
cities.append('Dallas')
cities.append("Albany")
print(f"cities: {cities}")

more_cities = ['Pittsburgh', 'Richmond', 'Miami']
cities.extend(more_cities)
print(f"cities: {cities}")

# LIST.insert(pos, obj)  LIST.append(obj)  LIST.extend(iterable)

del cities[2]
print(f"cities: {cities}")

cities.remove('Silver Spring')
print(f"cities: {cities}")

c = cities.pop()
print(f"c: {c}")
print(f"cities: {cities}")

c = cities.pop(3)
print(f"c: {c}")
print(f"cities: {cities}")

# del LIST[pos]    LIST.remove(value)   LIST.pop(pos=-1)

cities[1] = 'Cairo'
print(f"cities: {cities}")

print(f"cities[1]: {cities[1]}")
print(f"cities[6]: {cities[6]}")
print(f"cities[-1]: {cities[-1]}")  # len(cities) - 1
print(f"cities[-2]: {cities[-2]}")
print(f"cities[-7]: {cities[-7]}")
# print(f"cities[-8]: {cities[-8]}")  # out of range

print(f"cities[0:4]: {cities[0:4]}")
#  START:STOP  START:STOP:STEP
print(f"cities[2:5]: {cities[2:5]}")

s = "Houlihan Lokey"
print(f"s[5:8]: {s[5:8]}")

print(f"cities[-5:]: {cities[-5:]}")
print(f"cities[-5:len(cities)]: {cities[-5:len(cities)]}")
print(f"cities[:3]: {cities[:3]}")
print('-' * 60)

# for VAR in ITERABLE:
for city in cities:
    # city = next-value-of-cities
    print(city)
print()

for city in cities[:4]:
    print(city)
print()

for letter in "abc":
    print(letter.upper())
print()




















