#!/usr/bin/env python3

#Loops are used to repaeat the same block of code several times
#Loops (estruturas de repeticao) sao usados par arepertir o mesmo bloco de codigo diversas vezes

#------------------------------------------------------------------------
for i in range(0, 10):
 print (i)
#minimal example of a for loop
#exemplo minimo de um loop for

#------------------------------------------------------------------------
#english:
eletronics = ["toaster", "fridge", "computer", "television"]

for device in eletronics:
 print (device)

#portuges:
eletronicos = ["sanduicheira", "televisao", "computador", "geladeira"]

for dispositivo in eletronicos:
 print(dispositivo)

#------------------------------------------------------------------------
for i in range(0, 10):
 if i == 5:
  break
 print (i)
#break is used to stop the loop and continue running the code after it
#o comando break (frear, parar) interrompe o loop no ponto onde este for ativado e continua apos o bloco do loop

#------------------------------------------------------------------------
for i in range(0, 10):
 if i == 5:
  continue
 print (i)
#continue is used to break only the current iteration of the loop, continuing with the next
#o comando continue e usado para interromper apenas a iteracao atual do loop, seguindo na proxima

#------------------------------------------------------------------------
