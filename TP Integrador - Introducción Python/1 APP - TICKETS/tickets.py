import random, pickle, os, sys

TICKET_FILE = "tickets.pkl"

def cargar_tickets():
    if os.path.exists(TICKET_FILE):
        try:
            with open(TICKET_FILE, "rb") as file:
                return pickle.load(file)
        except (EOFError, pickle.UnpicklingError):
            return {}
    return {}

def guardar_tickets():
    with open(TICKET_FILE, "wb") as file:
        pickle.dump(tickets, file)

def menu():
    global tickets
    tickets = cargar_tickets()
    while True:
        print("\n---------------------------------------")
        print("Hola, bienvenido al sistema de Tickets")
        print("---------------------------------------")
        print("\n---- MENÚ PRINCIPAL ----")
        print("1. Generar un nuevo Ticket")
        print("2. Leer un Ticket")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            alta_ticket()
        elif opcion == "2":
            leer_ticket()
        elif opcion == "3":
            if confirmar_salida():
                guardar_tickets()
                print("\nSaliendo del programa...\n")
                sys.exit()
        else:
            print("\nOpción no válida. Intente nuevamente.")

def alta_ticket():
    while True:
        print("\n--- ALTA DE TICKET ---")
        nombre = input("Ingrese su nombre: ")
        sector = input("Ingrese su sector: ")
        asunto = input("Ingrese el asunto: ")
        problema = input("Describa el problema: ")

        numero_ticket = random.randint(1000, 9999)
        tickets[numero_ticket] = {
            "Nombre": nombre,
            "Sector": sector,
            "Asunto": asunto,
            "Problema": problema
        }

        print("\n=====================================")
        print("--- Se genero el siguiente Ticket ---")
        print("=====================================\n")
        print(f"Número de Ticket: {numero_ticket}")
        print(f"Nombre: {nombre}")
        print(f"Sector: {sector}")
        print(f"Asunto: {asunto}")
        print(f"Problema: {problema}")
        print("\nPor favor, recuerde el número de su ticket.")

        crear_otro = input("\n¿Desea crear otro ticket? (s/n): ").lower()
        if crear_otro != 's':
            break

def leer_ticket():
    while True:
        print("\n=====================================")
        print("--------- LECTURA DE TICKET ---------")
        print("=====================================\n")
        try:
            numero_ticket = int(input("Ingrese el número de ticket: "))
            if numero_ticket in tickets:
                print("\n=====================================")
                print("--------- TICKET ENCONTRADO ---------")
                print("=====================================\n")
                ticket = tickets[numero_ticket]
                print(f"Número de Ticket: {numero_ticket}")
                print(f"Nombre: {ticket['Nombre']}")
                print(f"Sector: {ticket['Sector']}")
                print(f"Asunto: {ticket['Asunto']}")
                print(f"Problema: {ticket['Problema']}")
            else:
                print("No se encontró ningún ticket con ese número.")
        except ValueError:
            print("Por favor, ingrese un número de ticket válido.")

        leer_otro = input("\n¿Desea leer otro ticket? (s/n): ").lower()
        if leer_otro != 's':
            break

def confirmar_salida():
    confirmacion = input("\n¿Está seguro que desea salir? (s/n): ").lower()
    return confirmacion == 's'

if __name__ == "__main__":
    menu()
