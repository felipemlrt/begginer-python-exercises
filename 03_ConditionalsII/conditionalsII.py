#!/usr/bin/env python3

#some more complex examples of conditionals
#alguns exemplos mais complexos de condicionais

#------------------------------------------------------------------------
#egnlish:
name = "Jonh"
users = ["Jonh", "Mark", "Anne"]

if name in users:
 print ("Yes, even this works")

#portugues:
nome = "joao"
usuarios = ["joao", "Marcos", "Ana"]

if nome in usuarios:
 print ("Sim, ate isso funciona")

#------------------------------------------------------------------------
#english:
alarm1 = "off"
alarm2 = "off"

if alarm1 is "off" and alarm2 is "off":
 print ("All is ok!")

#portugues
alarme1 = "desligado"
alarme2 = "desligado"

if alarme1 is "desligado" and alarme2 is "desligado":
 print ("Tudo ok!")

#------------------------------------------------------------------------
#english:
power = "plugged"
generator = "off"

if power is "plugged" or generator is "on":
 print ("We have power!")

#portugues:
energia = "conectada"
gerador = "desligado"

if energia is "conectada" or gerador is "ligado":
 print ("Temos energia!")

#------------------------------------------------------------------------
#english:
a, b = 1, 2
if b > a:
 pass #the pass statement is used in development to make a block not raise an error due to being empty
 
#portugues:
a, b = 1, 2
if b > a:
 pass #pass é usado durante o desenvolvimento para fazer com que um bloco vazio não gere erro

#------------------------------------------------------------------------
