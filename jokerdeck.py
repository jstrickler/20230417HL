from carddeck import CardDeck

class JokerDeck(CardDeck):
    
    def _make_deck(self):
        super()._make_deck()
        joker = 'Joker', 'Joker'
        self._cards.append(joker)
        self._cards.append(joker)

    