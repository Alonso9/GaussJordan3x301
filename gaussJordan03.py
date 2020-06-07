#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
x + y z = 6
2x - y + 3z = 9
-x + 2y +z = 6
'''
import numpy

print("\t------Programa en python del metodo de Gauss-Jordan 3x3------\n\n")

m = int(input('Ingrese numero de filas: '))
n = int(input('Ingrese numero de columnas: '))

matriz = numpy.zeros((m,n))

vectoRes = numpy.zeros(n)

aux1, aux2 = 0,0

#-------------------------funcion rellenar matriz y vector de resultados----------------------#

def rellenar():
    for r in range(0, m):
        for i in range(0, n):
            matriz[(r,i)] = int(input('Ingresa valor [' + str(r + 1) + "," + str(i + 1) + ']: ' ))
        vectoRes[(r)] = int(input('Ingresa el resultado de la ecuacion[' + str(r + 1) + ']: ' ))

#-------------------------------funcion mostrar matriz--------------------------------#
def mostrar():
    print('\n\t----------Valores de la matriz-----------------------\n' + str(matriz))
    print('\n\t----------Valores del  vector de resultados----------\n' + str(vectoRes))

def procedimiento():
    '''
    celdas: 31-21-32-13-23-12
    '''    

    for r in range(0,m):
        
        #step 1
        matriz[2,r] = matriz[2,r] + matriz[0,r]
        #step 2
        matriz[1,r] = matriz[1,r] - 2 * matriz[0,r]
        #step 3
        matriz[2,r] = matriz[2,r] + matriz[1,r]
        matriz[2,r] = matriz[2,r]/3
        #step 4
        matriz[0,r] = matriz[0,r] - matriz[2,r]
        #step 5
        matriz[1,r] = matriz[1,r] - matriz[2,r]
        matriz[1,r] = matriz[1,r]/-3
        #step 6
        matriz[0,r] = matriz[0,r]-matriz[1,r]
        
    vectoRes[2] = vectoRes[2] + vectoRes[0]
    vectoRes[1] = vectoRes[1] - 2 * vectoRes[0]
    vectoRes[2] = vectoRes[2] + vectoRes[1]
    vectoRes[2] = vectoRes[2]/3
    vectoRes[0] = vectoRes[0] - vectoRes[2]
    vectoRes[1] = vectoRes[1] - vectoRes[2]
    vectoRes[1] = vectoRes[1] /-3
    vectoRes[0] = vectoRes[0] - vectoRes[1]
    
    mostrar()
def main():
    
    rellenar()
    mostrar()
    procedimiento()
    print(f"\nResutado final es:\nx; {vectoRes[0]}\ny; {vectoRes[1]}\nz; {vectoRes[2]}")

main()
