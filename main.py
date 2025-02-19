def showMenu():
    print("--- Simulador de Encuesta ---")
    print("1. Responder encuesta")
    print("2. Ver resultados")
    print("3. Salir")

def respond(encuesta, respuestas):
    print("Responde la siguiente encuesta:")
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