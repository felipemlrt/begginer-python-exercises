#!/usr/bin/env python3.6

#Functions allows programmers to avoid having to write the same code multiple times and allows re use of code
#Funções permitem a programadores evitar re escrever o mesmo codigo diversas vezes além de permitir o re uso de codigo.

#----------------------------------------------------------------------------------------------------
#english:
def function(): #create in block, do not forget () and :
 print("It works!")

function()#call the function
function()#note that to repeat the function is just a matter of calling it again
#minimal example of how to create and call a function

#portugues:
def funcao(): #declaração da função, nunca esqueça () e :
 print("Funciona!")

funcao()#chamada da função
funcao()#note que é possível re usar o mesmo código facilmente, basta chamar a função novamente
#Exemplo minimo de como criar e chamar uma função

#----------------------------------------------------------------------------------------------------
#english:
def sum( X, Y):#use the () to specify arguments to the function, these are values that need to be provided once the function is called
 print(X + Y)

sum(5, 5)#note that the arguments need to be passed otherwise the function will raise an error

#portugues:
def soma( X, Y):#use () para determinar argumentos necessarios para a função
 print(X + Y)

sum(5, 5)#note a necessidade de passar os argumentos

#----------------------------------------------------------------------------------------------------
#english:
def sum( X, Y=1):#a standart value may be given, this way if the user does not provide a value this is used
 print(X + Y)

sum(5)#note that now Y does not require a value to be given
sum(8, 3)#a value may still be given to Y

#portugues:
def soma( X, Y=1):#um valor padrão pode ser atribuido, assim o argumento se torna opcional
 print(X + Y)

sum(5)#note que não há necessidade de passar Y
sum(8, 3)#porém caso um valor diferente do padrão seja desejado este ainda pode ser passado

#----------------------------------------------------------------------------------------------------
#english:
#example of the use of return to create a function that performs a task apart from the main code
def ask_name():
 name = input("What is your name?")
 return name

print("Welcome " + ask_name())

#portugues:
#exemplo do uso do return para criar uma função que realiza uma operação a parte e retorna o resultado
def pergunta_nome():
 nome = input("Qual seu nome?")
 return nome

print("Bem vindo " + pergunta_nome())

#----------------------------------------------------------------------------------------------------
#lambda functions are simple single line functions
#funções lambda são simples, definidas em uma unica linha
func_x = lambda a, b, c: (a * b)/c

print(func_x(5,10,5))

#----------------------------------------------------------------------------------------------------
