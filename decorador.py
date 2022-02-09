def funcion_decoradora(funcion_parametro):

    def funcion_interna(*args):

        print("Hola") 

        funcion_parametro(*args)

    return funcion_interna
a=2
b=2
@funcion_decoradora
def suma(a,b):
    print(a+b)

suma(a,b)   