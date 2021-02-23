def suma(num1,num2):
    return num1+num2
def resta(num1,num2):
    return num1-num2
def multiplicar(num1,num2):
    return num1*num2
def dividir (num1,num2):
    try:
        return num1/num2
    except ZeroDivisionError:
        print("No se puede divir por cero")
        return "Operacion no válida"
op1=int(input("Introduce el primero valor: "))
op2=int(input("Introduce el segundo valor: "))
operacion= input("Introduce la operacion a realizar:\n(suma, resta, multiplicacion, division): ")
if operacion=="suma":
    print("La suma es: ",(suma(op1,op2)))
if operacion=="resta":
    print("La resta es: ", (resta(op1,op2)))
if operacion=="multiplicacion":
    print("La multiplicación es: ", (multiplicar(op1,op2)))
if operacion=="division":
    print("La division es: ", dividir(op1,op2))    
