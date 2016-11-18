#!/usr/bin/python
# -*- coding: utf-8 -*-

# import random

from random import shuffle
arreglo = ['P1-OKOKOK-', 'P2', 'P3', 'P4']

shuffle(arreglo)

x=0
arreglo[x]  = "/A " + str(arreglo[x])
x += 1
arreglo[x]  = "/B " + str(arreglo[x])
x += 1
arreglo[x]  = "/C " + str(arreglo[x])
x += 1
arreglo[x]  = "/D " + str(arreglo[x])

for i in range(0,4):
  if arreglo[i].find('-OKOKOK-') != -1:
    arreglo[i] = arreglo[i].replace('-OKOKOK-','')
    lacorrectaes = arreglo[i][1]



print arreglo[0] , arreglo[1], arreglo[2], arreglo[3] , lacorrectaes


#print str(arreglo[0]), str(arreglo[1]),str(arreglo[2]),str(arreglo[3])

# posicion =  random.randrange(0, 4, 1)
# p = roles[:posicion]
# x = roles




# print  p
