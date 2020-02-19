#!/usr/bin/env python3.6

#Remenber that in python there is no need to assign a type to a variable!
#Lembre-se que em python nao ha a necessidade de declarar um tipo para a variavel!

#----------------------------------------------------------------------------------------------------
#english:
name = "John"
age = 21
#Note that there is a need to put " " around text values, but for values one can just attribute them.
#For non english speakers it is very important to not use special characters, that are not available in english, in variable names otherwise errors may occur.
#An example of wich would be preço wich uses the ç special character.

print(name)
print("John")
#The variable can be used in place of the desired value, this brings two main benefits.
#A code may be made in wich the value are defined only when the code is run
#And a code may be made in wich the value of variables, and thus the behaviour of the program, change as it is run

#portugues:
nome = "Joao"
idade = 21
#Note que e necessario adicionar " " envolta de valores de texto porem para numeros basta atribuir.
#Para nao falantes de ingles e muito importante nao usar caracterres que nao existem no ingles para nome de variaveis ou podem ocorrer erros ao tentar executar o codigo.
#Um exemplo seria a variavel preço, que usa o ç, e assim deve ser evitada.

print(nome)
print("Joao")
#Variaveis podem ser usadas no lugar do valor que elas contem, isso traz duas principais vantagens,
#Primeiramente um codigo pode ser criado onde todas as operaçoes sao programadas porem os valores so serao atribuidos durante a execuçao
#Alem disso um codigo pode ser criado onde ao longo da execuçao seu comportamento se altera

#----------------------------------------------------------------------------------------------------
#english:
name = input("What is your name?")
age = input("What is your age?")
print("Hello ", name, "!")
#Variables allow programmers to create code that will use values not known to them.

#portugues:
nome = input("Qual seu nome?")
idade = input("Qual sua idade?")
print("Oi ", nome,"!")
#variaveis permitem a programadores criarem codigos com valores desconhecidos que so serao definidos na execucao.
