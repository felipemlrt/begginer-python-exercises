#!/usr/bin/env python3.6

#Remenber that in python there is no need to assign a type to a variable!
#Lembre-se que em python nao ha a necessidade de declarar um tipo para a variavel!

#----------------------------------------------------------------------------------------------------
#english:
#In python variable's names can only start with letters or undercsore, and cannot contain special characters other than underscore. So A-z, 0-9, and _ can be used.
#Python variables are case sensitive, that means Casio and casio are two different variables.
#Legal (can be used) variable names:
myvar = "John"
my_var = "John" #In python this naming style is favored, try to use it. Examples: my_name, age_of_mom, car_color, and so on.
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#Illegal (can not be used) variable names:
2myvar = "John"
my-var = "John"
my var = "John"

#portugues:

#----------------------------------------------------------------------------------------------------
#english:
name = "John"
age = 21
#Note that there is a need to put " " or ' ' around text values, but for values one can just attribute them.
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
#Note que e necessario adicionar " " ou ' ' envolta de valores de texto porem para numeros basta atribuir.
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

#----------------------------------------------------------------------------------------------------
#english:
banana, apple, avocado = "yellow", "red", "green"
#its possible to assign several variables in a single line

#portugues:
banana, maca, abacate = "amarela", "vermelha", "verde"
#é possível atribuir diversas variaveis em uma só linha

#----------------------------------------------------------------------------------------------------
#floating point values are used just like integer values
#valor de ponto flutuante podem ser usados da mesma forma que inteiros
a = 1.25
print (a)

#----------------------------------------------------------------------------------------------------
#Variables type can be changed even after they have been set
x = 4           # x is of type int
x = "Casio"     # x is now of type str
print(x)
