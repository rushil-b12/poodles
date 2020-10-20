from poodle import Poodle
from random import choice
from namegen import generate_name


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
        return f'The kennel has a population of {self.population} including {len(self.males)} males and {len(self.females)} females.'

    def grow(self):
        mother = choice(self.females)
        father = choice(self.males)
        baby = mother.couple(father)
        if not baby:
            pass
        elif baby.gender == 'female':
            self.females.append(baby)
        elif baby.gender == 'male':
            self.males.append(baby)
    
if __name__ == '__main__':
    x = Kennel()
    print(x)