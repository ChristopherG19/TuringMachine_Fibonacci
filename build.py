from TM import *

def leerCinta(num):
    cadena = '1' * num
    return cadena

def buildTM(input):
    transition_function = {}
    inState = None
    fnState = None
    
    with open('transiciones.txt', 'r') as file:
        for line in file:
            if line.strip() == "":
                continue
            line = line.strip()
            line = line.split(':')
            tupla = eval(line[0])
            tupla2 = eval(line[1])
            transition_function[(tupla[0], tupla[1])] = (tupla2[0][0], tupla2[0][1], tupla2[0][2])

    with open('maquina.txt', 'r') as file:
        lista = []
        for line in file: 
            lista.append(line.strip())
        blank = lista[2].strip("'")
        inState = lista[4].strip("'")
        fnState = lista[5].strip("'")
 
    return TM(input, transition_function, inState, fnState, blank)