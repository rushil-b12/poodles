from random import choice

def generate_name():
    with open('male.txt', 'r', encoding="utf8") as mfile:
        content = mfile.readlines()
        m = choice(content)[:-1]

    with open('female.txt', 'r', encoding="utf8") as ffile:
        content = ffile.readlines()
        f = choice(content)[:-1]
    
    return m, f

if __name__ == '__main__':
    print(generate_name())