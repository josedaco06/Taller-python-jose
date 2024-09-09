tarifas={


"Estados Unidos": 900,
"Canada":800,
"Europa":950,
"Resto del mundo":1250}

Destino= input("Ingrese el destino de la llamada(Estados Unidos,Canada,Europa,Resto del mundo):")

Duracion=input("Ingrese la duracion de llamada en minutos")

costo_total=tarifas[destino]*Duracion

if "duracion">15:
    costo_total=0.8

print("El costo total de la llamada es:$",costo_total)
