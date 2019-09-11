'''
BLOC DE NOTAS de ADRIAN
-----------------------
v1.0
-----------------------
*Ejercicio 3pts para el examen final del módulo
*Sin internet
    Solo Evernote
    No hay Slack
*Para terminal
*Pensar bien las opciones que tendrá el bloc de notas
*Diagramación en www.lucidchart.com(diagrama flujo)
Entorno virtual Python 3.7.4
Git Local
Finalizar el ejercicio a la 16:15 enviar enlace por Github
'''
import os
import csv

lista = []

def inicio():
    os.system("clear")
    menu()

    
def menu():
    while True:
        print(f'    BIENVENIDO AL BLOC DE NOTAS DE ADRIÁN')
        print('-'*50)
        opcion = int(input(f'\nSelecciona la opción que desees realizar:\n\n Nueva nota[1]\n Ver notas[2]\n Borrar nota[3]\n Salir[4] --> '))
        try:
            if opcion == 1:
                añadir_nota()
            elif opcion == 2:
                ver_notas()
            elif opcion == 3:
                eliminar_nota()
            elif opcion == 4:
                exit()
            else:
                'Escoge una opción correcta'
        except ValueError:
                'Debes introducir un número'

def añadir_nota():
    nota = input(f'\nIntroduce la nota: ')
    bloc = open('bloc.csv','a')
    bloc.write(f'{nota}\n')
    print('-- NOTA GUARDADA --\n')
    
def ver_notas():
    bloc = open('bloc.csv', 'r')
    leer = csv.reader(bloc)
    print(f'\n -- Lista de notas --\n')
    for numero,nota in enumerate(leer):
        print(f'Nota {numero} --> {nota}')
    print('')
    
def eliminar_nota():
    nota_a_borrar = int(input(f'¿Qué nota desea borrar? --> '))
    with open('bloc.csv','r+') as bloc:
        leer = csv.reader(bloc)
    for index,notas in enumerate(lista):
        if index == nota_a_borrar:
            del lista[index]
        break
    guardar()
    print('')

def guardar():
    bloc = open('bloc.csv','w')
    for notas in lista:
        bloc.write(f'{notas}\n')

    
if __name__ == "__main__":
    inicio()