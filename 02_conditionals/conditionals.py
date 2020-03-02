#!/usr/bin/env python3

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
