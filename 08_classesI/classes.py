#A class in pythons is a collection of methods(functions that belong to a class) and attributes (variables that belong to a class) all related to a certain concept, object, functionality, etc.
#Em python uma classe é uma coleção de métodos(funções) e atributos(variaveis) relacionadas a um certo conceito, objeto, funcionalidade, etc.
#Classes make code easier to organize, reference and re use.
#Classes tornam o codigo mais facil de organizar, referenciar e re-usar.

#In python classes are simple to create
class class_name:# This create a class named <class_name> # a
  
  atribute = 1 #example of the creation of an atribute
  other_atribute = "This is an atribute" #example of a string atribute
  yet_another = None #example of a None value atribute, be mindfull there is a difference between a atribute nor existing and it being None
  
  def __init__():
    pass
  
  def sum(x, y):#This creates a method called sum that is contained on class_name
    return x + y
  
  def multiply(x, y):#classes may contain multiple methods
    return x * y;

if __name__ == "__main__": #This is used so that the code below will only run if this file is run dictly, if this class is imported to another project it will not be run
  pass
