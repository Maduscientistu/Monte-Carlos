from math import sin
import random

def f(x): 
    y = sin(x)+10
    return y

def g(x):
    y = sin(x)+5
    return y

def simulacao(a, b):
    pontosRio = 0
    geracoes = 1000000
    maximo_x = b + 100
    maximo_y = int(f(maximo_x)+100)
    for e in range(geracoes):
        x = random.randint(0,maximo_x)
        y = random.randint(0,maximo_y)
        if x > a and x < b and y > g(x) and y < f(x):
            pontosRio += 1



        
    areatotal = maximo_y * maximo_x
    area = (pontosRio/geracoes)*areatotal
    print(area)
simulacao(float(input('a: ')), float(input('b: ')))
