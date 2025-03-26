from artistas import datos_artista
from paixes import agregar_pais
from geneross import agregar_genero
#from reportes import realizar_reporte
def menu_principal():
    print(
    """
    ****************************************
    *************menu principal*************
    ****************************************
    precione
    1. para añadir artistas
    2. para añadir paises
    3. para añadir generos
    4. para ver reporte
    5. para salir
    ****************************************
    ****************************************
    ****************************************
    """
    )

def menu():
    while True:
        menu_principal()
        opc=input("ingrese su opccion: ")
        if opc =="1":
            datos_artista()
        elif opc=="2":
            agregar_pais()
        elif opc=="3":
            agregar_genero()
        elif opc=="4":
            print("realizar reportes no esta disponible")
            #realizar_reporte()
        elif opc=="5":
            print("saliendo.....")
            break
        else:
            print("opcion no disponible vuelva a intentarlo")

