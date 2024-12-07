import secrets, string, sys

diccionario = {
    'letras': string.ascii_letters,
    'numeros': string.digits,
    'caracteres': string.punctuation
}

def generar_password(tipo, longitud):
    return ''.join(secrets.choice(tipo) for _ in range(longitud))

def menu():
    while True:
        print("\n--- GENERADOR DE CONTRASEÑAS V0.1 ---\n")
        print("1. Generar contraseña solo de letras")
        print("2. Generar contraseña solo de números")
        print("3. Generar contraseña de letras y números")
        print("4. Generar contraseña de letras, números y caracteres")
        print("0. Salir")

        opcion = input("\nEscriba la opción seleccionada: ")

        if opcion == "1":
            longitud = int(input("\nIngrese la longitud de la contraseña: "))
            password = generar_password(diccionario['letras'], longitud)
            print("\n-------------------")
            print(f"Contraseña generada: {password}")
            print("-------------------")
        elif opcion == "2":
            longitud = int(input("\nIngrese la longitud de la contraseña: "))
            password = generar_password(diccionario['numeros'], longitud)
            print("\n-------------------")
            print(f"Contraseña generada: {password}")
            print("-------------------")
        elif opcion == "3":
            longitud = int(input("\nIngrese la longitud de la contraseña: "))
            tipo = diccionario['letras'] + diccionario['numeros']
            password = generar_password(tipo, longitud)
            print("\n-------------------")
            print(f"Contraseña generada: {password}")
            print("-------------------")
        elif opcion == "4":
            longitud = int(input("\nIngrese la longitud de la contraseña: "))
            tipo = diccionario['letras'] + diccionario['numeros'] + diccionario['caracteres']
            password = generar_password(tipo, longitud)
            print("\n-------------------")
            print(f"Contraseña generada: {password}")
            print("-------------------")
        elif opcion == "0":
            print("\nSaliendo del programa...\n")
            sys.exit()
        else:
            print("\n-------------------------------------")
            print("Opción no válida. Intente nuevamente.")
            print("-------------------------------------")

if __name__ == "__main__":
    menu()
