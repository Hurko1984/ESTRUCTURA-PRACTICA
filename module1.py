#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      vangu
#
# Created:     09/09/2022
# Copyright:   (c) vangu 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():

    palabra = input("ingrese su email: ").lower()
    arroba = "probador"
    for caracter in palabra:
        arroba = "mail valido"
        if caracter == "@":
            break
        else:
            arroba = "mail invalido"


    print(arroba)
main()


#print(f'El nombre del usuario es {nombre}')





