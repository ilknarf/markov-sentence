import pickle
import random

with open('./markov.bin', 'rb') as c: 
    markov = pickle.load(c)

def pick_random(last):
    d = markov[last.lower()]
    
    if not d.keys():
        return None
    
    s = sum(d.values())
    goal = random.randint(0, s)

    c = 0
    for key in d.keys():
        c += d[key]
        if c > goal:
            break
    
    return key

def print_sentence(i):
    result = i.split()

    if (n := pick_random(result[-1])) == None:
        print('bad input')

    else:
        result.append(n)
        while n != None and (n not in '.!?' or len(result) < 15):
            if len(result) > 50:
                result.append('.')
                break

            n = pick_random(n)

            if n != None:
                result.append(n)
        s = ''
        
        for w in result:
            s += (w not in '-",.!?;\'') * ' ' + w

        print(s[1:] + '\n')

while (i := input(
        'Enter starter(.QUIT to exit, .RANDOM for random): ')) != '.QUIT':
    
    if i == '.RANDOM':
        i =  random.choice(list(markov.keys()))

    if len(i) == 0:
        print('no input. try again')
    else:
        print_sentence(i)