kilometersTraveled = 0
usedLiters = 0
litersUsedPerkilometer = 0

kilometersTraveled = float(input("por favor ingrese los kilometros recorridos"))
usedLiters = float(input("ingrese la cantidad de gasolina gastada"))
result = kilometersTraveled/usedLiters
result = str(result) 
print ("la cantidad de gasolina usada por kilometro es:"  +  result)
