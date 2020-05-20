nombre = input("Ingrese su nombre: ")
apellido = input(f"Hola {nombre}, cuál es su apellido?: ")

print(f"Bienvenido {nombre} {apellido}, es un gusto conocerte\n\n")

edad = int(input("Cuál es tu edad: "))

if edad != 18: 
    print("Wow eres mayor de edad\n")
else:
    print("Owww... eres pequeñito\n")