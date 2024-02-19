import json
import os

#Nombre de archivo y direccion del mismo
archivo = "Islas_Bingo.json"
carpeta = f"D:\\BIngo\\Gestor_Bingo\\Gestor_Maquinas_Bingo\\Gestor_Maquinas_Bingo\\{archivo}"

#Keys---------------------------------
#Preventivo---------------------------
Preventivo_key = "Preventivo"
limpias_key = "Maquinas Limpias"
sucias_key = "Maquinas Sucias"
#Tecnico-----------------------------
Tecnico_key = "Tecnico"
#Laboratorio-------------------------
Laboratorio_key = "Laboratorio"

registro_maquinas = {}
islas_maximas = 100

#Generar las key de preventivo (Hacer que genere la de los 3 cargos)
registro_maquinas[Preventivo_key] = {
    limpias_key : [],
    sucias_key : []
}

#Generar las islas por defecto
for islas in range(islas_maximas):
     registro_maquinas[Preventivo_key][sucias_key].append((islas+1))

#Verficar que exista el archivo
if(os.path.isfile(carpeta) == True):
    print(f"\nEl archivo {archivo} fue cargado correctamente")
else:
    with open(archivo, 'x') as file:
          json.dump(registro_maquinas,file,indent=4)
    print(f"\nEl archivo {archivo} fue creado correctamente")

#Agregar isla limpia ---------------------------------------------------------------------------------------------------------------------
#print("Indique la isla que fue limpiada: ")
#numero_de_isla = int(input())
#
##Lectura del archivo
#with open (archivo,'r') as file:
#    registro_maquinas = json.load(file)     
#
#registro_maquinas[Preventivo_key][sucias_key].remove(numero_de_isla)
#
##Cargar en el registro para subir al archivo    
#registro_maquinas[Preventivo_key][limpias_key].append(numero_de_isla)
#
##Ordenamiento de menor a mayor
#for islas_a in range(len(registro_maquinas[Preventivo_key][limpias_key])):
#     for islas_b in range(len(registro_maquinas[Preventivo_key][limpias_key])):
#          if registro_maquinas[Preventivo_key][limpias_key][islas_a] < registro_maquinas[Preventivo_key][limpias_key][islas_b]:
#               temporal = registro_maquinas[Preventivo_key][limpias_key][islas_a]
#               registro_maquinas[Preventivo_key][limpias_key][islas_a] = registro_maquinas[Preventivo_key][limpias_key][islas_b]
#               registro_maquinas[Preventivo_key][limpias_key][islas_b] = temporal
#
##Cargarla en el archivo
#with open (archivo, 'w') as file:
#    json.dump(registro_maquinas, file, indent=4)
#    
#---------------------------------------------------------------------------------------------------------------------------------------
#Agregar isla sucia
print("Indique la isla que no fue limpiada: ")
numero_de_isla = int(input())

#Lectura del archivo
with open (archivo,'r') as file:
    registro_maquinas = json.load(file)     

registro_maquinas[Preventivo_key][limpias_key].remove(numero_de_isla)

#Cargar en el registro para subir al archivo    
registro_maquinas[Preventivo_key][sucias_key].append(numero_de_isla)

#Ordenamiento de menor a mayor
for islas_a in range(len(registro_maquinas[Preventivo_key][sucias_key])):
     for islas_b in range(len(registro_maquinas[Preventivo_key][sucias_key])):
          if registro_maquinas[Preventivo_key][sucias_key][islas_a] < registro_maquinas[Preventivo_key][sucias_key][islas_b]:
               temporal = registro_maquinas[Preventivo_key][sucias_key][islas_a]
               registro_maquinas[Preventivo_key][sucias_key][islas_a] = registro_maquinas[Preventivo_key][sucias_key][islas_b]
               registro_maquinas[Preventivo_key][sucias_key][islas_b] = temporal

#Cargarla en el archivo
with open (archivo, 'w') as file:
    json.dump(registro_maquinas, file, indent=4)
