import pandas as pd

list1 = ['red', 'blue', 'purple', 'green', 'orange', 'red', 'black', 'red']
list2 = ['pink', 'purple', 'lilac', 'black', 'green', 'green', 'pink']

set1 = set(list1)
set2 = set(list2)

set1.add('orange')
set1.add('navy blue')
set2.add('blue')

print(f"set1: {set1}")
print(f"set2: {set2}")
print()

print("Common:", set1 & set2)  # intersection
print("Not common:", set1 ^ set2)  # xor
print("All:", set1 | set2)  # union
print("Just set1:", set1 - set2)
print("Just set2:", set2 - set1)

for color in sorted(set1 | set2):
    print(color)

s1 = pd.Series(list1)
print(f"s1: {s1}")
series_set = set(s1)
print(f"series_set: {series_set}")

df = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]])
print(f"df: {df}")
df_set = set(df.iloc[:,2])
print(f"df_set: {df_set}")





