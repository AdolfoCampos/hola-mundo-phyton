def main():
  edad = int(input("¿Cuál es tu edad?"))
  if edad <= 13:
    print("Eres un niño.")
  elif edad >= 14 and edad <= 17:
    print("Eres un adolescente.")
  elif edad >= 18 and edad <= 64:
    print("Eres un adulto.")
  else:
    print("Eres un adulto mayor.")

if __name__ == "__main__":
  main()