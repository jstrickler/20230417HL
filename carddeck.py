import random

class CardDeck:  # inherits from 'object'
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    SUITS = 'Clubs Diamonds Hearts Spades'.split()

    def __init__(self, dealer):
        # self.some_member = None
        self._dealer = dealer
        self._make_deck()

    def _make_deck(self):
        self._cards = list()
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = rank, suit
                self._cards.append(card)

    @property
    def cards(self):
        return self._cards
    
    # 1. getter method
    # 2. getter property

    # getter property
    @property
    def dealer(self):
        return self._dealer

    # setter property
    @dealer.setter
    def dealer(self, dealer):
        if isinstance(dealer, str):
            self._dealer = dealer
        else:
            raise TypeError("dealer must be a str")
    
    def shuffle(self):
        random.shuffle(self._cards)

    # instance method
    def draw(self):
        return self._cards.pop()

    @classmethod
    def get_suits(cls):
        return cls.SUITS

    @staticmethod
    def bark():
        print("Woof! woof!")

    def __len__(self):  # len(x)
        return len(self._cards)

    def __str__(self):  # str(x)
        # CardDeck:Alex,48
        my_type = type(self)
        my_name = my_type.__name__
        return f"{my_name}:{self.dealer},{len(self)}"
    
    def __repr__(self):
        my_type = type(self)
        my_name = my_type.__name__
        return f"{my_name}('{self.dealer}')"

    def __iter__(self):
        return self

    def __next__(self):
        try:
            card = self._cards.pop()  # returns last element
        except IndexError:
            raise StopIteration
        return card

    # context manager protocol
    # def __enter__(self): pass
    # def __exit__(self, *args): pass


    