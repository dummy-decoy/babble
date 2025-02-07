import random
import time

# when context_size=2:
# database = {(word1,word2): {word3_1: probability, word3_2: probability2}, (word2, word3): {word4: probability}}

context_size = 3
database = {}
starts = {}

def split(text):
    tkn = ''
    i = iter(text)    
    chr = next(i)
    try:
        while True:
            while str.isspace(chr):
                chr = next(i)
            if str.isalnum(chr) or (chr == '\'') or (chr == '-'):
                while str.isalnum(chr) or (chr == '\'') or (chr == '-'):
                    tkn += chr
                    chr = next(i)
                yield tkn
                tkn = ''
            elif chr in '.,:;!?':
                tkn += chr
                chr = next(i)
                yield tkn
                tkn = ''
            else:           
                chr = next(i)
    except StopIteration:
        if tkn != '':
            yield tkn

def build(corpus):
    tokens = split(corpus)
    run = tuple(next(tokens) for i in range(context_size))
    starts[run] = starts.setdefault(run, 0)+1
    try:
        while current := next(tokens):
            database[run][current] = database.setdefault(run, {}).setdefault(current, 0)+1
            popped = run[0]
            run = run[1:]+(current,)
            if popped in '.!?':
                starts[run] = starts.setdefault(run, 0)+1
    except StopIteration:
        pass

def babble():
    seed = random.choices(list(starts.keys()), weights=list(starts.values()))[0]
    for token in seed:
        yield token
    while True:
        nexts = database[seed]
        next = random.choices(list(nexts.keys()), weights=list(nexts.values()))[0]
        yield(next)
        seed = seed[1:]+(next,)
