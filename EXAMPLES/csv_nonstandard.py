import csv

with open('../DATA/computer_people.txt') as computer_people_in:
    rdr = csv.reader(computer_people_in, delimiter=';')  # specify alternate field delimiter

    for first_name, last_name, known_for, birth_date in rdr:  # iterate over rows of data -- csv reader is a generator
        print('{}: {}'.format(last_name, known_for))
