pokeDex=["Bulbasaur","Charmander","Squirtle","Pikachu"]


pokeDex.remove("Bulbasaur")
pokeDex.remove("Charmander")
pokeDex.remove("Pikachu")
indexNumber = 0

while pokeDex:
    if indexNumber < len(pokeDex):
        print(pokeDex[indexNumber])
        indexNumber += 1
    else:
        break  

print("---------------------------")
pokeDex.append("Eevee")
indexNumber = 0

while pokeDex:
    if indexNumber < len(pokeDex):
        print(pokeDex[indexNumber])
        indexNumber += 1
    else:
        break  