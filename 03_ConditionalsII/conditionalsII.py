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
x = 1

if not x == 1: #"not" can be used to invert a true result into false and a false into true
 print ("This only prints if x is not 1!") #be careful, the "not" does not inverts the operation, it inverts the result.

#portugues:
x = 1

if not x == 1:#o "not" torna o verdadeiro falso e o falso verdadeiro
 print ("Esta mensagem só é apresentada se x não for 1!") #cuidado, o "not" não inverte a operação mas sim o resultado desta.

#------------------------------------------------------------------------
#english:
a, b, c = 1, 2, 3
if b > a:
 print( "a > b")
 if b < c: #conditionals can be nested witthout a problem, just remember that the second one will not be evaluated if the first is not true
  print( "b < c")

#portugues:
a, b, c = 1, 2, 3
if b > a:
 print( "a > b")
 if b < c: #condicionais podem ser colocados um dentro do outro sem problemas, lembre porém que o segundo só será avaliado se o primeiro for ativado
  print( "b < c")

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
x = 10

#english:
#there is also a special way to use a if else in a single line
print ("yay!") if x == 10 else print("nay")
#Note that both the if and else are required, "print ("yay!") if x == 10" would raise a sintax error

#portugues:
#existe uma forma especial que pode ser usada para criar um if else em uma unica linha
print ("Tudo certo!") if x == 10 else print("Não deu certo")
#Note que são necessários ambos o if e o else, "print ("Tudo certo!") if x == 10" resulta em um erro de sintaxe

#------------------------------------------------------------------------
