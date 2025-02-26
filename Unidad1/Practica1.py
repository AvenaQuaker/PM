# 21100158/20100257 26/Febrero/2025 PM 

#1 Funciones con n parámetros 
#Escribir un programa que contenga una función que reciba n parámetros de tipo numérico y calcule el producto total. 
def Ejercicio1(*args):
    producto = 1
    for i in args:
        producto *= i
    return producto

print(Ejercicio1(2, 3, 4, 5, 6))

#2 Manejo y manipulación de elementos de una lista 
# Escribir un programa que almacene el abecedario en una lista, elimine de la 
# lista las letras que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante. 

abecedario = list('abcdefghijklmnopqrstuvwxyz')
letrasEliminadas = []
print(abecedario)

Contador = 1
for i in abecedario:
    if Contador % 3 == 0:
        letrasEliminadas.append(abecedario[Contador])
    Contador += 1

for i in letrasEliminadas:
    abecedario.remove(i)

print(abecedario)

#3 Entrada de datos y manipulación. 
# Escribir un programa que permita al usuario capturar su 
# nombre completo e imprima su nombre de manera inversa letra por letra 
print("Escribe tu nombre completo")
nombre = input()
nombreInvertido = nombre[::-1]
print(nombreInvertido)


#4 Entrada de datos y estructuración. Revisar su retícula para escribir un programa que cree un 
# diccionario vacío para que el usuario capture las materias y créditos de su semestre preferido (inferior a 8vo) al 
# final imprimir en el formato “{asignatura}” tiene “{créditos}” créditos. Y la suma de todos los créditos del semestre 
dic1 = {}
materia9no="DES APLIC DESENTRA"
while(True):
   opcion = 0
   print("1-Capturar Materias \n 2- salir")
   opcion = int(input()) 
   if(opcion == 1 and str(type(opcion))== "<class 'int'>"):
      while(True):
        print("Asignatura: ")
        asignatura = input()
        if(asignatura == materia9no):
            print("No puedes llevar materias superiores a 8vo")
        else:
           break
      print("creditos:")
      creditos =int(input())
      dic1[asignatura] = creditos
   else:
    break

def recorrerDic(**diccionario):
   suma = 0
   for key , value in diccionario.items():
      print(f"{key}:" , f"{value}")
      suma = value + suma 
   print(f"Total de creditos: {suma}") 

recorrerDic(**dic1)
   




#5 Manejo de información 
# Escribir una función que reciba n parámetros de llave valor e imprima la información en formato “{llave}”: “{Valor}” 
def impValorLlave(**diccionario):
   for key , value in diccionario.items():
      print(f"{key}:" , f"{value}")

dic = {"Nombre":"Mario","Edad":27,"Carrera":"ing en sistemas"}

impValorLlave(**dic)


#6 Razonamiento y prueba de código 
# Escribir un programa que reciba un numero entre 0 y 20 e imprimir el numero en letra, no utilizar condicionales, máximo 5 líneas de código.

numeros = ["cero", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve", "diez", "once", "doce", "trece", "catorce", "quince", "dieciséis", "diecisiete", "dieciocho", "diecinueve", "veinte"]
print(numeros[int(input("Introduce un número entre 0 y 20: "))])


#7 Formateo y conversiones 
# Escribir un programa que muestre un menú con 2 opciones la primera opción “1.- Imprimir YYYY/MM/DD” la segunda “
# 2.- Imprimir MM/DD/YYYY” una vez seleccionada la opción imprimir la fecha del día de hoy en el formato seleccionado.

import datetime

print("selecciona una opcion")
print("1.- Imprimir YYYY/MM/DD")
print("2.- Imprimir MM/DD/YYYY")

opcion2 = int(input())


if(opcion2 == 1):
   print(datetime.datetime.now().strftime("%Y/%m/%d"))
else:
   print(datetime.datetime.now().strftime("%m/%d/%y"))
