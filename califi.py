nota1=float(input("Ingrese la primera nota:"))
nota2=float(input("Ingrese la segunda nota:"))
nota3=float(input("Ingrese la tercera nota:"))
nota4=float(input("Ingrese la cuarta nota:"))

promedio=(nota1+nota2+nota3+nota4)/4

if promedio>=4:
  clasificacion="Excelente"
elif promedio>3:
    clasificacion="Bien"
else:
     clasificacion="Deficiente"

costo_matricula=float(input("Ingrese el costo de matricula:"))

if clasificacion=="Excelente":
    monto_final=costo_matricula*0.8
else:
    monto_final=costo_matricula

print("Promedio:",promedio)
print("Clasificacion:",clasificacion)
print("Monto final:",monto_final)
