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

    next_word = pick_random(result[-1])
    if next_word is None:
        print('starter not found')

    else:
        result.append(next_word)
        while next_word != None and (next_word not in '.!?' or len(result) < 15):
            if len(result) > 50:
                result.append('.')
                break

            next_word = pick_random(next_word)

            if next_word is not None:
                result.append(next_word)
        s = ''
        
        for w in result:
            s += (w not in '-",.!?;\'') * ' ' + w

        print(s[1:] + '\n')

while (i := input('Enter starter (".q" to exit, ".r" for random): ')) != '.q':
    
    if i == '.r':
        i =  random.choice(markov.keys())

    if len(i) == 0:
        print('no input. try again')
    else:
        print_sentence(i)