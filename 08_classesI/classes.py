#A class in pythons is a collection of functions and variables all related to a certain concept, object, functionality, etc.
#Em python uma classe é uma coleção de funções e variaveis relacionadas a um certo conceito, objeto, funcionalidade, etc.
#Classes make code easier to organize, reference and re use.
#Classes tornam o codigo mais facil de organizar, referenciar e re-usar.

#In python classes are simple to create
class class_name:# This create a class named <class_name>
  
  atribute = 1 #example of the creation of an atribute
  
  def sum(x, y):#This creates a function called sum that is contained on class_name
    return x + y
  
  def multiply(x, y):#A class can cotain multiple functions
    return x * y;

if __name__ == "__main__": #This is used so that the code below will only run if this file is run dictly, if this class is imported to another project it will not be run
  ###
