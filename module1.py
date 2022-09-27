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


    num1 = int(input("Digite un numero: "))
    num2 = int(input("digite un segundo numero"))
    print(" 1. sumar, 2. restar, 3. multiplicar")
    opcion = int(input("ingrese una opcion"))

    while(opcion == 0 or  opcion >3):

        print(" 1. sumar, 2.restar, 3. multiplicar")

        opcion = int(input("ingrese una opcion: "))


    if opcion == (1):
         resu = num1 + num2

    elif opcion == (2):
            resu = num1 - num2
    else:
            resu =num1 * num2


    print(f' El resultado es: {resu}')


main()








