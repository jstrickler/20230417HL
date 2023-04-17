s1 = "spam\n"   # \n \t \f \b \uXXXX \??
print(f"len(s1): {len(s1)}")
s2 = 'spam\n'
s3 = """spam\n"""
s4 = '''spam\n'''

print("Guido's the ex-BDFL of Python")
print('Guido is the ex-"BDFL" of Python')
print("""Guido's the ex-"BDFL" of Python""")

query = """
select *
from customers
where state is 'IOWA'
order by sales_ytd
"""




