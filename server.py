import markov
import random
import time

throttle = 0.05
corpus = open('corpus.txt')
markov.build(corpus.read())

def babbler():
    text = markov.babble()
    token = next(text)
    yield str.encode('<!doctype html><html><head><title>markov babbler</title></head><body><p>', 'utf-8')
    yield str.encode(token, 'utf-8')
    time.sleep(throttle)
    count = 0
    section = random.randrange(5, 25)
    while True:
        token = next(text)
        yield str.encode(('' if token in '.,:;?!' else ' ')+token, 'utf-8')
        time.sleep(throttle)
        if token in '.?!':
            count += 1
        if count >= section:
            yield str.encode('<p>', 'utf-8')
            section = random.randrange(5, 25)
            count = 0

def markov_babble(env, start_response):
    start_response('200 OK', [('Content-Type','text/html; charset=utf-8')])
    return babbler()