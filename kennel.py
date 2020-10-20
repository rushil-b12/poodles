from poodle import Poodle
from random import choice
from namegen import generate_name
from time import sleep

class Kennel:
    def __init__(self, population = 0, females = [], males = []):
        self.population = max(2, population)
        self.females = females
        if len(females) == 0:
            self.females.append(Poodle(gender='female'))
        self.males = males
        if len(males) == 0:
            self.males.append(Poodle(gender='male'))

    def __str__(self):
        m = [poodle.__str__() for poodle in self.males]
        f = [poodle.__str__() for poodle in self.females]
        return f'''
        Kennel:
        Population: {self.population};
        Females: {f}; 
        Males: {m}.
        '''

    def census(self):
        return f'The kennel has a population of {self.population} including {len(self.females)} females and {len(self.males)} males.'

    def grow(self):
        mother = choice(self.females)
        father = choice(self.males)
        print(f'{mother.name} and {father.name} are coupling.')
        baby = mother.couple(father)
        if not baby:
            print('Coupling unsuccessful.')
        elif baby.gender == 'female':
            print('Coupling successful.')
            self.population += 1
            self.females.append(baby)
            print(baby)
        elif baby.gender == 'male':
            print('Coupling successful.')
            self.population += 1
            self.males.append(baby)
            print(baby)
    
if __name__ == '__main__':
    x = Kennel()
    print(x)
    for i in range(5):
        x.grow()
        print(x)
        sleep(2)
    print(x.census())