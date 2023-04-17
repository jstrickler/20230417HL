
from animal import Animal


class Reptile(Animal):
    '''
        An animal with 2 sets of wings and 3 pairs of legs
    '''

    def __init__(self, species, name, sound, has_legs=True):
        super().__init__(species, name, sound)  # call parent constructor
        self._has_legs = has_legs

    @property
    def has_legs(self):  # add reptile-specific property
        return self._has_legs


if __name__ == '__main__':
    guido = Reptile('Burmese python', 'Guido', "SSssssss", False)  # create instance of reptile
    smaug = Reptile('dragon', 'Smaug', 'Roarrrrrrr')

    for reptile in guido, smaug:
        legs_status = 'have' if reptile.has_legs else "do not have"
        print("Hi! I am {} the {} and I {} legs!".format(
                reptile.name, reptile.species, legs_status
            ),
        )
        reptile.make_sound()  # call instance method from parents
        print()
