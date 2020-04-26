import pickle
import re
from collections import defaultdict, Counter
from bs4 import BeautifulSoup

def parse(string, markov, weight):

    p = re.compile(r"[\w']+|[.,!?;]")
    
    words = re.finditer(p, string)

    if (last := next(words, None)) != None:
        last = last.group()
    while (n := next(words, None)) != None:
        n = n.group()
        markov[last.lower()][n] += weight
        last = n

markov = defaultdict(Counter)

with open('../../Downloads/copperfield.html') as c:
    soup = BeautifulSoup(c, 'lxml')

    text = soup.findAll('p')

    for t in text:
        parse(t.text, markov, 1)

with open('../../Downloads/lolita.html') as c:
    soup = BeautifulSoup(c, 'lxml')

    t = soup.find('pre')

    parse(t.text, markov, 2)

with open('./computer.txt') as c:
    parse(c.read(), markov, 10)

with open('../../Downloads/my immortal.txt') as c:
    f = c.read()
    parse(f, markov, 4)

print(markov)

with open('./markov.bin', 'wb') as c:
    pickle.dump(markov, c)