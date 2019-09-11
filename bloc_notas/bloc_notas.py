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
        # elif opcion == 3:
        #     def borrar_nota()
            elif opcion == 4:
                exit()
            else:
                'Escoge una opción correcta'
        except ValueError:
                'Debes introducir un número'

def añadir_nota():
    nota = input(f'\nIntroduce la nota: ')
    print('-- NOTA GUARDADA --\n')
    bloc = open('bloc.csv', 'a')
    bloc.write(f'{nota}\n')
    bloc.close()

def ver_notas():
    bloc = open('bloc.csv', 'r')
    lista_notas = csv.reader(bloc)
    for numero,nota in enumerate(lista_notas):
        print(f'\n{numero}-->{nota}')
# def opcion_seleccionada(opcion):
#     try:
#         if opcion == 1:
#             añadir_nota()
#     elif opcion == 2:
#         def ver_notas()
#     elif opcion == 3:
#         def borrar_nota()
#         elif opcion == 4:
#             exit()
#         else:
#             'Escoge una opción correcta'
#     except ValueError:
#             'Debes introducir un número'
    
if __name__ == "__main__":
    inicio()