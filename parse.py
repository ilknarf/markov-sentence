import os

import pickle
import re
from collections import defaultdict, Counter

def parse(string, markov, weight):

    p = re.compile(r"[\w']+|[.,!?;]")
    
    words = re.finditer(p, string)

    if (last := next(words, None)) is not None:
        last = last.group()
    while (n := next(words, None)) is not None:
        n = n.group()
        markov[last.lower()][n] += weight
        last = n

model = None
model_location = None

while (cmd := input('Enter l to load (or create) model, a to add new file, q to quit: ')) != 'q':
    if cmd == 'l':
        if model is not None:
            print('model is already loaded')
        else:
            model_location = input('enter the location (or desired location_ of the model: ')
            if os.path.exists(model_location):
                if os.path.isdir(model_location):
                    print('model location is directory')
                else:
                    try:
                        with open(model_location, 'w') as file:
                            model = pickle.load(file)
                    except:
                        print('invalid file contents')
            else:
                model = defaultdict(Counter)

    if cmd == 'a':
        if model is None:
            print('load a model file before adding text')
        else:
            filepath = input('enter the location of the file to add: ')
            weight = input('enter the weight of the file (1): ')
            if type(weight) is not int:
                print('please enter a valid integer')
            else:
                with open(filepath) as f:
                    string = f.read()
                    parse(string, model, weight)
                
                pickle.dump(model, open(model_location, 'w'))
    else:
        print('invalid command. press "q" to quit')