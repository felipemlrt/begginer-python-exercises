#!/usr/bin/env python3

#Equals / Igual: a == b
# 5 == 3 returns / retorna False, 5 == 5 returns / retorna True
#Not Equals / Diferente: a != b
# 5 != 3 returns / retorna True, 5 != 5 returns / retorna False
#Less than / Menor que: a < b
#Less than or equal to / Menor ou igual que: a <= b
#Greater than / Maior que: a > b
#Greater than or equal to / Maior ou igual que: a >= b

#----------------------------------------------------------------
x = 0

#First a simple if
if x >= 0:
 print ("yay!")

#Primeiramente um if (se) simples
if x >= 0:
 print ("Tudo certo")

#----------------------------------------------------------------
x = -1

#Next, a if with a else
if x >= 0:
 print ("yay!")
else:
 print ("nay!")

#A seguir um if (se) com else (senao)
if x >= 0:
 print ("Tudo certo")
else:
 print ("Nao deu certo")

#----------------------------------------------------------------
x = 2

#Next, if, elif and else
if x >= 10:
 print ("yay!")
elif x >=0 and x < 10:
 print ("may?")
else:
 print ("nay!")

#A seguir um if (se), elif (senao se) e else (senao)
if x >= 10:
 print ("Tudo certo")
elif x >=0 and x < 10:
 print ("Talvez certo")
else:
 print ("Nao deu certo")

#----------------------------------------------------------------
a, b = 5, 10

#english:
#quick one line if statement, usefull to keep the code small and easy to read
if a < b: print("ERROR!")

#portugues:
#if rapido de uma linha, mantem o codigo curto e facil de ler
if a < b: print("ERRO!")
 
#----------------------------------------------------------------
