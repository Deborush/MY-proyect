import random

def mostrar_menu():
    print("\n--- Simulador de Encuesta ---")
    print("1. Responder encuesta")
    print("2. Ver resultados")
    print("3. Salir")

def responder_encuesta(encuesta, respuestas):
    print("\nResponde la siguiente encuesta:")
    for i, (pregunta, opciones) in enumerate(encuesta.items(), 1):
        print(f"{i}. {pregunta}")
        for j, opcion in enumerate(opciones, 1):
            print(f"   {j}. {opcion}")
        
        while True:
            try:
                eleccion = int(input("Elige una opción: "))
                if 1 <= eleccion <= len(opciones):
                    respuestas[pregunta][eleccion - 1] += 1
                    break
                else:
                    print("Opción inválida. Intenta de nuevo.")
            except ValueError:
                print("Entrada no válida. Ingresa un número.")

def ver_resultados(encuesta, respuestas):
    print("\n--- Resultados de la Encuesta ---")
    for pregunta, opciones in encuesta.items():
        print(f"\n{pregunta}")
        for i, opcion in enumerate(opciones):
            print(f"   {opcion}: {respuestas[pregunta][i]} votos")
