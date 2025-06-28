#Leccion 1
print("Hello Perros locos")

#Leccion 2
nombre = "Adolfo"
edad = 30
altura = 1.85
es_estudiante = True

print("Se llama:", nombre)
print("Años de edad:", edad)
print("Mide:", altura)
print("¿Estudia?", es_estudiante)
#Ejercicio
print("-Ejercicio:")
ciudad = "León"
comida = "pizza"
hermanos = 5

print("Vivo en", ciudad, "me gusta mucho la", comida, "y tengo", hermanos,
      "hermanos")
print("¡¡¡¡FIN!!!")


# main.py
def presentar_datos(nombre, edad, altura, es_estudiante):
  print("Se llama:", nombre)
  print("Años de edad:", edad)
  print("Mide:", altura)
  print("¿Estudia?", es_estudiante)


def main():
  # Parte 1: Mensajes introductorios
  print("Hello Perros este es el ejercicio")

  # Parte 2: Datos personales con variables y funcion
  nombre = "Adolfo"
  edad = 30
  altura = 1.85
  es_estudiante = True

  presentar_datos(nombre, edad, altura, es_estudiante)

  # Parte 3: Datos adicionales
  ciudad = "León"
  comida = "pizza"
  hermanos = 5
  print(
      f"Vivo en {ciudad}, me gusta mucho la {comida} y tengo {hermanos} hermanos"
  )


# Este bloque hace que, si ejecutas el script directamente, se llame a main().
if __name__ == "__main__":
  main()
