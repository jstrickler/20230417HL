import re

s = """lorem ipsum M-302 dolor sit amet, consectetur r-99 adipiscing elit, sed do
 eiusmod tempor incididunt H-476 ut labore et dolore magna Q-51 aliqua. Ut enim 
ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex  
ea commodo z-883  consequat. Duis aute irure dolor in reprehenderit in URANIUM-232
voluptate velit esse cillum dolore U901 eu fugiat nulla pariatur. Y-239393 
Excepteur sint occaecat A-110 cupidatat non proident, sunt in H-332 culpa qui 
officia deserunt Y-45 mollit anim id est laborum"""

pattern = r'\b[A-Z]-\d{2,3}\b'  # store pattern in raw string

if re.search(pattern, s):  # search returns True on match
    print("Found pattern.")
print()

# groups 0, 1, 2, 3
#  group 0 -- entire match
#  group 1 -- first set of ()     'foo(.*)bar'
#  group 2 -- second set of ()
m = re.search(pattern, s)  # search actually returns match object
print(m)
if m:
    print("Found:", m.group(0))  # group(0) returns text that was matched by entire expression (or just m.group())
print()

for m in re.finditer(pattern, s):  # iterate over all matches in string:
    print(m.group())
print()

matches = re.findall(pattern, s)  # return list of all matches
print("matches:", matches)

# re.match()  '^' + pattern   
# re.fullmatch()  '^' + pattern + '$'

