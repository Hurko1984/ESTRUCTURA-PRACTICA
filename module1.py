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


    num1 = int(input("Digite un numero impar: "))
    while(num1%2==0):

               print(" no es impar ")

               num1 = int(input("vuelva a digitar un numero impar: "))
    print(f' {num1} este numero si es impar')

main()







