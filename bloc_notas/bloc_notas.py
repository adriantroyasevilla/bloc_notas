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

def inicio():
    os.system("clear")
    menu()
    
def menu():
    print(f'    BIENVENIDO AL BLOC DE NOTAS DE ADRIÁN')
    print('-'*50)
    opcion = int(input(f'Selecciona la opción que desees realizar:\n\n Nueva nota[1]\n Ver notas[2]\n Borrar nota[3]\n Salir[4] -->'))
    return opcion

if __name__ == "__main__":
    inicio()