# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
numeros= [4,8,9,4,3,2,5,1]

arreglo=[1,"hola",3,"dfsdf"]

arreglo2=[1,"buenas",54, arreglo, 1, "*","h",2,7,6,"$", 4, "b", "j", 85,66]

print(arreglo2[3])

for dat in arreglo2:
    print(dat)
   
arregloslice = arreglo2[0:10]

print(numeros.sort())

alfabeto = ["c", "d","a", "j", "z", "x", "q"]

print(alfabeto.sort())

alfabeto2 = ["A","Z","P","R", "U", "N", "Y", "b", "c", "f"]

arreglo2.index("h")

dir (numeros)

#Código que permite organizar en la Variable Explorer

alfabeto2.sort(key=str.lower)