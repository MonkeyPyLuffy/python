kilometersTraveled = 0
usedLiters = 0
litersUsedPerkilometer = 0

kilometersTraveled = float(input("por favor ingrese los kilometros recorridos"))
usedLiters = float(input("ingrese la cantidad de gasolina gastada"))
result = kilometersTraveled/usedLiters
result = str(result)
if litersUsedPerkilometer.is_integer():
    print("la cantidad de gasolina usada es" + result)
else:
    print("lo siento el numero no es valido")


