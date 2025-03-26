import json

paises=[]

def cargar_pais():
    global paises 
    try:
        with open('paises.json', 'r') as archivo:
            paises = json.load(archivo)
    except FileNotFoundError:
        paises = []  
    except json.JSONDecodeError:
        paises = []

def guardar():
    with open('paises.json', 'w') as archivo:
        json.dump(paises, archivo, indent=4)

def agregar_pais():
    cargar_pais()
    paiz=input("ingrese el nombre del pais: ")
    iso=input("agreger el codigo iso: ")
    iso3=input("agrege el iso 3: ")
    pais={
           "nombre del pais":paiz,
            "codigo ISO": iso,
            "codigo ISO3": iso3
        }
    paises.append(pais)
    guardar()