from poodle import Poodle
from kennel import Kennel
from namegen import generate_name
from random import randint, choice
from time import sleep

patriarch = Poodle(gender='male')
matriarch = Poodle(gender='female')
doghouse = Kennel(2, [matriarch], [patriarch])
print(doghouse)

for i in range(15):
    sleep(randint(2, 5))
    doghouse.grow()
    print('')

sleep(3)
print('')
print(doghouse.census())
print(doghouse)
