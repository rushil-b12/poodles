from random import randint, choice
from namegen import generate_name

class Poodle:
    def __init__(self, name=None, gender=None, colour=None):
        x = randint(0, 1)
        colours = ['black', 'darkbrown', 'hazel', 'white', 'golden', 'tan', 'red', 'grey']
        if gender:    
            self.gender = gender
            x = 1 if self.gender == 'female' else 0
        else:
            self.gender = 'female' if x == 1 else 'male'
        if name:
            self.name = name
        else:
            self.name = generate_name()[x]
        if colour:
            self.colour = colour
        else:
            self.colour = choice(colours)
    
    def __str__(self):
        return f'<{self.name}, {self.gender}, {self.colour}>'

    def couple(self, mate):
        if type(mate) == Poodle:
            if mate.gender != self.gender:
                if randint(0, 1):
                    gender = 'female' if randint(0, 1) else 'male'
                    colour = self.colour if randint(0, 1) else mate.colour
                    m, f = generate_name()
                    name = m if gender == 'male' else f
                    return Poodle(name, gender, colour)
                else:
                    return None
            else:
                raise Exception('Argument must be of opposite gender.')
        else: 
            raise TypeError('Argument must be a Poodle object.')

if __name__ == '__main__':
    a = Poodle(gender='male', colour='hazel')
    print(a)
