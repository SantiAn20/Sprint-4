import os
import datetime

#Verificacion que el archivo CSV ingresado contenga la extensión correspondiente
def verificacion_csv(archivo_csv):
  if "." in archivo_csv:
    punto = archivo_csv.index(".")
    punto = punto + 1 #A partir de donde empieza la extensión
    extension = archivo_csv[punto:]

    if archivo_csv[punto:] != "csv":
      archivo_csv = archivo_csv.replace(extension,'csv')


  #Si el nombre del archivo ingresado no tiene la extensión, se le agrega
  else:
    archivo_csv= archivo_csv + ".csv"

  return archivo_csv


#Ingreso de cómo el usuario quiere visualizar el contenido
def pantalla_csv():
  print("¿Cómo quiere visualizar la informacion consultada?" '\n' 
        "Opción 1: Por PANTALLA (Ingrese 1)" '\n' 
        "Opción 2: Por CSV (Ingrese 2)")
  print()
  salida = input("Ingrese la opción deseada: ")

  while salida != "1" and salida != "2":
    print()
    print("Error. Ingrese nuevamente una de las opciones:" '\n'
          "Opción 1: Por PANTALLA (Ingrese 1)" '\n' 
          "Opción 2: Por CSV (Ingrese 2)")
    print()
    salida = input("Ingrese la opción deseada: ")

  return salida


#DNI con el que se va a realizar la consulta
def ingreso_dni():
  dni = input("Ingrese su DNI para realizar la consulta: ")
  while len(dni) != 8 or dni.isdigit() == False:
    print()
    dni = input("DNI ingresado incorrecto. Ingrese un DNI correcto: ")

  return dni

#Tipo de cheque con el que se va a realizar la consulta
def tipo_cheque():
  print("¿Qué tipo de cheque quiere consultar?" '\n' 
        "Opción 1: EMITIDO (Ingrese 1)" '\n' 
        "Opción 2: DEPOSITADO (Ingrese 2)")
  print()
  tipo = input("Ingrese la opción deseada: ")

  while tipo != "1" and tipo != "2":
    print()
    print("Error. Ingrese nuevamente una de las opciones:" '\n' 
        "Opción 1: EMITIDO (Ingrese 1)" '\n' 
        "Opción 2: DEPOSITADO (Ingrese 2)")
    print()
    tipo= input("Ingrese la opción deseada: ")

  if tipo == "1":
    tipo = "emitido"
  
  else:
    tipo = "depositado"
  
  return tipo


# Preguntamos al usuario si desea filtrar por estado, si quiere por cuál
def estado_cheque():
  print("¿Desea filtrar cheques por su estado?" '\n' 
        "Opción 1: SI (Ingrese 1)" '\n' 
        "Opción 2: NO (Ingrese 2)")
  print()
  estado = input("Ingrese la opción deseada: ")

  while estado != "1" and estado != "2":
    print()
    print("Error. Ingrese nuevamente una de las opciones:" '\n'
          "Opción 1: SI (Ingrese 1)" '\n' 
          "Opción 2: NO (Ingrese 2)")
    print()
    estado = input("Ingrese la opción deseada: ")


  if (estado == "1") :
    print("Seleccione el estado por el cual se filtrarán los cheques" '\n' 
        "Opción 1: Aprobado (Ingrese 1)" '\n' 
        "Opción 2: Rechazado (Ingrese 2)" '\n'
        "Opción 3: Pendiente (Ingrese 3)")
    print()
    opciones = input("Ingrese la opción deseada: ")
  
    while opciones != "1" and opciones != "2" and opciones != "3":
        print()
        print("Error. Ingrese nuevamente una de las opciones:" '\n'
             "Opción 1: Aprobado (Ingrese 1)" '\n' 
             "Opción 2: Rechazado (Ingrese 2)" '\n'
             "Opción 3: Pendiente (Ingrese 3)" )
        print()
        opciones = input("Ingrese la opción deseada: ")

    
    if (opciones == "1"):
        opciones = "aprobado"
    elif (opciones == "2"):
     opciones = "rechazado"
    else :
      opciones = "pendiente"

  else:
    return False #SI LA OPCION ES NO USAR ESTE FILTRO
      
  return opciones


# Preguntamos al usuario si desea filtrar por fecha
def fecha_cheque():
  print("¿Desea filtrar cheques por rango de fechas?" '\n' 
        "Opción 1: SI (Ingrese 1)" '\n' 
        "Opción 2: NO (Ingrese 2)")
  print()
  opcion = input("Ingrese la opción deseada: ")

  while opcion != "1" and opcion != "2":
    print()
    print("Error. Ingrese nuevamente una de las opciones:" '\n'
          "Opción 1: SI (Ingrese 1)" '\n' 
          "Opción 2: NO (Ingrese 2)")
    print()
    opcion = input("Ingrese la opción deseada: ")

  if opcion == "1":
     return True 
  
  else:
    return False #SI LA OPCION ES NO USAR ESTE FILTRO


def rango_fecha():

  #Si quiere filtrar por rango de fechas

  print("Complete las fechas por las que se filtrarán los cheques" '\n'
        "Ejemplo: 2021-10-20 12:00:00 o 2021-10-20")
  print()
  fecha1 = input("Desde: ")
  print()
  fecha2 = input("Hasta: ")
      
  return fecha1, fecha2


#Busca el dni en la lista, si no coincide, devuelve la lista vacía
def buscar_dni(lista,dni):
  if dni in lista[8]:
    return lista
  
  else:
    return []


#Busca el tipo de cheque en la lista, si no coincide, devuelve la lista vacía
def buscar_tipo(lista,tipo):
      if lista != []:
         if tipo in lista:
           return lista
         
         else:
            return []
         
      else:
         return []


#Busca el estado de cheque en la lista, si no coincide o no quería usar este filtro, devuelve la lista vacía
def buscar_estado(lista,estado):
      if estado == False:
        if lista != []:
           return lista
        else:
           return []
      
      else:
        if lista != []:
          if estado in lista:
            return lista

          else:
              return []
        
        else:
              return []


#Busca el el rango de fechas en la lista, si no coincide o no quería usar este filtro, devuelve la lista vacía
def buscar_fecha(lista,fecha,fecha1,fecha2):
      fecha1 = str(fecha1)
      fecha2 = str(fecha2)


      if fecha == False:
        if lista != []:
           return lista
        else:
           return []
      
      else:
        if lista != []:
          fecha_csv = int(lista[7])
          fecha_csv = str(datetime.datetime.fromtimestamp(fecha_csv))
          
          if fecha_csv > fecha1 and fecha_csv < fecha2:
            return lista

          else:
              return []
        
        else:
              return []


#Se imprime por pantalla la información o se exporta a un CSV
def imprimir_exportar(salida,linea,lista):
      if salida == "1":
         print(linea)
         print("-------------")
         
      else: #salida es 2, entonces se escribe en CSV
         dni= lista[8]
         fecha_actual = datetime.datetime.now()
         fechaEnTimestamp = str(int(datetime.datetime.timestamp(fecha_actual)))
  
         with open(dni + "_" + fechaEnTimestamp + ".csv", "a") as nuevo_csv:
           nuevo_csv.write(linea + "\n")



#MAIN

print()
archivo_csv = input("Ingrese el nombre del archivo CSV: ")
archivo_csv = verificacion_csv(archivo_csv)

while os.path.exists(archivo_csv) == False:
  print()
  archivo_csv = input("El archivo CSV ingresado no existe, ingrese el nombre del archivo CSV nuevamente: ")
  archivo_csv = verificacion_csv(archivo_csv)


print()
salida = pantalla_csv()
print()
dni = ingreso_dni()
print()
tipo_de_cheque = tipo_cheque()
print()
estado_cheque_Op = estado_cheque()
print()
rango_fechas_Op = fecha_cheque()

if rango_fechas_Op == True:
  print()
  fecha1,fecha2 = rango_fecha()
  print()

no_existe = True #Si no existe en el CSV los datos a consultar, sirve para imprimir un mensaje final que no existieron los datos en el CSV

if salida == 1:
  print("_________________________"'\n'
          "RESULTADOS:")
  print()

with open(archivo_csv, "r") as clientes:
    clientes.readline() #tiro la primera linea
    for linea in clientes:
      linea = linea.strip("\n")
      lista = linea.split(",")
      lista = buscar_dni(lista, dni)
      lista = buscar_tipo(lista, tipo_de_cheque)
      lista = buscar_estado(lista, estado_cheque_Op)
      if rango_fechas_Op == True:
        lista = buscar_fecha(lista, rango_fechas_Op, fecha1, fecha2)
      
      if lista == []: #Si la lista está vacia, es porque no coinciden los datos ingresados
         continue #Entonces vuelve a interar el for
      
      no_existe = False
      
      imprimir_exportar(salida,linea,lista) #Si llega hasta acá es porque los datos coinciden y se ejecuta la función


if no_existe == True:
  print("La información ingresada para buscar en el CSV: '",archivo_csv, "', no existe.")
