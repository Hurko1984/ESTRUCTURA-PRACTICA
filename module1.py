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

   palabra_secreta = "python"
   contador = 1
   palabra = input("Ingrese la palabra secreta: ").lower()

   while palabra != palabra_secreta and contador < 7:
         palabra = input("Ingrese la palabra secreta: ").lower()
         contador = contador + 1
   print("Próxima instrucción")



main()





