actor = "Chris Hemsworth"
print(f"actor: {actor}")
s = actor.upper()
print(f"s: {s}")
print(f"len(actor): {len(actor)}")
print(f"type(actor): {type(actor)}")

print(f"actor.count('h'): {actor.count('h')}")
print(f"actor.count('H'): {actor.count('H')}")
print(f"actor.lower().count('h'): {actor.lower().count('h')}")

print(f"actor.startswith('Chris'): {actor.startswith('Chris')}")
print(f"actor.startswith('Liam'): {actor.startswith('Liam')}")

file_name = "blech.yaml"
plain_name = file_name.removesuffix(".yaml")
print(f"plain_name: {plain_name}")

print(f"actor.replace('Chris', 'Liam'): {actor.replace('Chris', 'Liam')}")
s = "Missippippi"
print(f"s.replace('p','P'): {s.replace('p','P')}")
print(f"s.replace('p','P', 2): {s.replace('p','P', 2)}")

s = "I have a bad feeling about this"
print(f"s.split(): {s.split()}")
s = "1|Washington|George|VA"
fields = s.split('|')
print(f"fields: {fields}")

s = "        Python is the best!      "
print(s + "|")
print(s.lstrip() + "|")
print(s.rstrip() + "|")
print(s.strip() + "|")
print()

value = '00000003.98'
print(f"value.lstrip('0'): {value.lstrip('0')}")
s = "my stuff.....,,,,...."
print(f"s.rstrip(',.'): {s.rstrip(',.')}")

names = ["James", "Earl", "Ray"]

name = " ".join(names)
print(f"name: {name}")

name = "/".join(names)
print(f"name: {name}")










