from random import randint

class Poodle:
    def __init__(self, name, gender, colour):
        self.name = name
        self.gender = gender
        self.colour = colour
    
    def __str__(self):
        return f'Poodle <{self.name}, {self.gender}, {self.colour}>'

    def couple(self, mate):
        if type(mate) == Poodle:
            if mate.gender != self.gender:
                if randint(0, 1):
                    gender = 'female' if randint(0, 1) else 'male'
                    colour = self.colour if randint(0, 1) else mate.colour
                    name = 'abcdefghijklmnopqrstuvwxyz'[randint(0, 25)]
                    return Poodle(name, gender, colour)
                else:
                    return None
            else:
                raise Exception('Argument must be of opposite gender.')
        else: 
            raise TypeError('Argument must be a Poodle object.')

if __name__ == '__main__':
    a = Poodle('Harry', 'male', 'brown')
    b = Poodle('Holly', 'female', 'black')
    print(a.couple(b))
