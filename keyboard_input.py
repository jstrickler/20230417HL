
user_name = input("What is your name: ")
quest = input("What is your quest? ")
print("{} seeks {}".format(user_name, quest))

raw_num = input("Enter number: ")  # input is always a string
num = float(raw_num)  # convert to numbers as needed

print("2 times {} is {}".format(num, 2 * num))

value_list = input("Enter 3 values, separated by commas (no spaces): ")
values = value_list.split(',')
print(f"values: {values}")