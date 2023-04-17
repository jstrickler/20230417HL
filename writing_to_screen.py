print("Hello, world")

name = "Fred Flintstone"
city = "Bedrock"
value = 2.384094

print(name, city, value)
# really
# output    str(name) + " " + str(city) + " " + str(value) + "\n"

print(name, city, value, sep="/")
print(name, city, value, sep="<==>")

print(name, end=" ")
# if ....
#    print(....)
print(city)
print()

print(name, "lives in", city)
print(name, ",", city)

# f-string 
print(f"{name}, {city}")

# f"...{expr}...{expr}...."

print(f"2 + 2 is {2 + 2}")

print(f"value is {value}")
print(f"value is {value:.1f}")

count = 33
print(f"count is {count:04d}")
print(f"count is {count:4d}")


print(f"{name}, {city}")
print("{}, {}".format(name, city))  # python 3 formatting
print("2 + 2 is {}".format(2 + 2))

print("2 + 2 is %d" % (2 + 2))  # python 2 formatting (legacy formatting)



