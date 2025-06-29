def main():
    #Ejercicio 1
    usuario = input("Usuario: ")
    clave = input("Clave: ")
  
    if usuario == "admin" and clave == "1234":
       print("Acceso concedido")
    elif usuario == "admin":
        print("Clave incorrecta")
    else:
        print("Usuario incorrecto")
  
    #Ejercicio 2
    a = float(input("Primer número: "))
    b  = float(input("Segundo número: "))
    op = input("Operación (+, -, *, /): ")

    if op == "+":
        resultado = a + b
    elif op == "-":
        resultado = a - b
    elif op == "*":
        resultado = a * b
    elif op == "/":
        if b != 0:
          resultado = a / b
        else:
          resultado = "Error: división por cero"

    else:
      print ("Operación no válida")
      return

    print(f"Resultado: {resultado}")

if __name__ == "__main__":
  main()