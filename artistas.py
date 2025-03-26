import json
def cargar_artista():
    global artistas 
    try:
        with open('artistas.json', 'r') as archivo:
            artistas = json.load(archivo)
    except FileNotFoundError:
        artistas = []  
    except json.JSONDecodeError:
        artistas= []

def guardar():
    with open('artistas.json', 'w') as archivo:
        json.dump(artistas, archivo, indent=4)

def datos_artista():       
    nombre=input("ingrese del nombre del artista: ")
    pais=input("ingrese el pais: ")
    while True:
        try:
            actividad=int(input("ingresa el periodo de actividad: "))
            break
        except ValueError:
            print ("ingrese un valor numerico")
            continue

    exito=input("ingrese la fecha de lanzamiento de el primer exito: ")
    genero=input("ingrese el genero musical: ")

    while True:
        try:
            unidades=int(input("unidades certificadas totales: "))
            break
        except ValueError:
            print ("ingrese un valor numerico")
            continue

    while True:
        try:
            ventas=int(input("ventas reclamadas: "))
            break
        except ValueError:
            print ("ingrese un valor numerico")
            continue

    estado=input("ingrese si el artista esta activo (si/no)")
    artista={
            "nombre artista":nombre,
            "pais": pais,
            "periodo de actividad": actividad,
            "fecha del primer exito": exito,
            "genero musical": genero,
            "unidades certificadas": unidades,
            "ventas reclamadas": ventas,
            "estado de actividad" : estado
        }
    cargar_artista()
    artistas.append(artista)
    guardar()


