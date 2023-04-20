from carddeck import CardDeck
from jokerdeck import JokerDeck

d1 = CardDeck("Alex")
print(f"type(d1): {type(d1)}")
print(f"d1: {d1}")

d2 = CardDeck("Robin")

print(f"d1.dealer: {d1.dealer}")

d1.dealer = "Bob"

print(f"d1.dealer: {d1.dealer}")

# d1.dealer = 47

print(f"CardDeck.SUITS: {CardDeck.SUITS}")

d1.shuffle()
print(f"d1.cards: {d1.cards}")
print('-' * 60)

for i in range(5):
    print(f"d1.draw(): {d1.draw()}")

print(f"d1.get_suits(): {d1.get_suits()}")
print(f"CardDeck.get_suits(): {CardDeck.get_suits()}")

CardDeck.bark()

# Don't do this:
#print(f"CardDeck.draw(d1): {CardDeck.draw(d1)}")

print('-' * 60)
j1 = JokerDeck('Jerry')
print(f"j1: {j1}")
j1.shuffle()
for _ in range(5):
    print(f"j1.draw(): {j1.draw()}")
print(f"j1.cards: {j1.cards}")

print(f"d1: {d1}")
print(f"j1: {j1}")
print(f"repr(d1): {repr(d1)}")
print(f"repr(j1): {repr(j1)}")

print(f"next(d1): {next(d1)}")
print(f"next(d1): {next(d1)}")

print(f"d1.draw(): {d1.draw()}")


for card in d1:
    print(card)
