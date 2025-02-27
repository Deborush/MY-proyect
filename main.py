import random  # Importa el módulo random (aunque no se usa en este código)

# Función para mostrar el menú principal
def mostrar_menu():
    print("\n--- 🟢 Simulador de Encuesta 🟢 ---")
    print("1. Responder encuesta")
    print("2. Ver resultados")
    print("3. Salir")

# Función para responder la encuesta
def responder_encuesta(encuesta, respuestas):
    print("\n🔹 Responde la siguiente encuesta:")
    for i, (pregunta, opciones) in enumerate(encuesta.items(), 1):
        print(f"{i}. {pregunta}")  # Muestra la pregunta
        for j, opcion in enumerate(opciones, 1):
            print(f"   {j}. {opcion}")  # Muestra las opciones de respuesta
        
        while True:
            try:
                eleccion = int(input("Elige una opción: "))  # Solicita la respuesta del usuario
                if 1 <= eleccion <= len(opciones):  # Verifica que la opción sea válida
                    respuestas[pregunta][eleccion - 1] += 1  # Registra el voto en la opción seleccionada
                    break
                else:
                    print("Opción inválida. Intenta de nuevo.")  # Mensaje de error si la opción no es válida
            except ValueError:
                print("Entrada no válida. Ingresa un número.")  # Mensaje de error si la entrada no es un número

# Función para ver los resultados de la encuesta
def ver_resultados(encuesta, respuestas):
    print("\n--- 🔴 Resultados de la Encuesta 🔴 ---")
    for pregunta, opciones in encuesta.items():
        print(f"\n{pregunta}")  # Muestra la pregunta
        for i, opcion in enumerate(opciones):
            print(f"   {opcion}: {respuestas[pregunta][i]} votos")  # Muestra los votos por opción

# Función principal del programa
def main():
    # Definición de las preguntas y opciones de la encuesta
    encuesta = {
        "¿Cuál es tu lenguaje de programación favorito?": ["Python", "JavaScript"],
        "¿Prefieres trabajar solo o en equipo?": ["Solo", "En equipo"],
        "¿En qué momento del día prefieres estudiar o trabajar?": ["Mañana", "Tarde", "Noche"],
        "¿Cómo prefieres aprender algo nuevo?": ["Leyendo", "Viendo videos", "Practicando"]
    }
    # Inicializa el diccionario para almacenar las respuestas con valores en 0
    respuestas = {pregunta: [0] * len(opciones) for pregunta, opciones in encuesta.items()}
    
    while True:  # Bucle principal del programa
        mostrar_menu()  # Muestra el menú de opciones
        opcion = input("Elige una opción: ")  # Solicita al usuario que elija una opción
        
        if opcion == "1":
            responder_encuesta(encuesta, respuestas)  # Llama a la función para responder la encuesta
        elif opcion == "2":
            ver_resultados(encuesta, respuestas)  # Llama a la función para ver los resultados
        elif opcion == "3":
            print("Saliendo del programa. ¡Gracias por participar!")  # Mensaje de despedida
            break  # Sale del bucle y finaliza el programa
        else:
            print("Opción no válida. Intenta de nuevo.")  # Mensaje de error si la opción ingresada no es válida

# Punto de entrada del programa
if __name__ == "__main__":
    main()  # Llama a la función principal
