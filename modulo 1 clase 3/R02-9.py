"""9. Elevar una base al exponente de 6 (que estará dentro una variable), este
número el cual su valor estará asignado a una variable y luego restar este
mismo valor multiplicado por dos (usar pow o **). Mostrar el resultado final
en pantalla."""

"Definir la base y el exponente (que será 6)"

base = 5
exponente = 6

"Calcular la potencia: base elevada al exponente 6"
resultado_potencia = base ** exponente  # También puedes usar pow(base, exponente)

"Restar el valor del exponente multiplicado por dos"
resultado_final = resultado_potencia - (exponente * 2)

"Mostrar el resultado en pantalla"
print(f"Base: {base}")
print(f"Exponente: {exponente}")
print(f"{base}^{exponente} = {resultado_potencia}")
print(f"Resultado final: {resultado_potencia} - ({exponente} * 2) = {resultado_final}")