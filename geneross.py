import json

def cargar_genero():
    global generos
    try:
        with open('generos.json', 'r') as archivo:
            generos = json.load(archivo)
    except FileNotFoundError:
        generos = []  
    except json.JSONDecodeError:
        generos = []

def guardar():
    with open('generos.json', 'w') as archivo:
        json.dump(generos, archivo, indent=4)

def agregar_genero():
        
    cargar_genero()
    id=input("ingrese el id del genero musical: ")
    desc=input("escriba la descripcion del genero: ")
    genero={
           "id":id,
            "descripcion": desc
            }
    generos.append(genero)
    guardar()
