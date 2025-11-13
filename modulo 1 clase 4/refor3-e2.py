"""Crea un programa que calcule el Índice de Masa Corporal (IMC) de una persona.
La fórmula es: IMC = Peso (kg) / (altura (m))^2
En el mensaje también indicar el nombre de la persona indicando su IMC también"""

def calcular_imc():
    print("=== CALCULADORA DE IMC ===")

    # Solicitar datos al usuario
    nombre = input("Ingrese su nombre: ")
    peso = float(input("Ingrese su peso en kg: "))
    altura = float(input("Ingrese su altura en metros: "))

    # Calcular IMC
    imc = peso / (altura ** 2)

    # Determinar categoría
    if imc < 18.5:
        categoria = "Bajo peso"
    elif 18.5 <= imc < 25:
        categoria = "Peso normal"
    elif 25 <= imc < 30:
        categoria = "Sobrepeso"
    else:
        categoria = "Obesidad"

    # Mostrar resultados
    print(f"\n--- RESULTADO PARA {nombre.upper()} ---")
    print(f"IMC: {imc:.2f}")
    print(f"Categoría: {categoria}")
    print(f"{nombre}, tu Índice de Masa Corporal es: {imc:.2f}")


# Ejecutar el programa
calcular_imc()