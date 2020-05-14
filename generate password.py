import random

def shuffle(string):
    templist = list(string)
    random.shuffle(templist)
    return ''.join(templist)

uppercaseletter1=chr(random.randint(65,90))
uppercaseletter2=chr(random.randint(65,90))

password = uppercaseletter1 + uppercaseletter2
password = shuffle(password)

print(password)