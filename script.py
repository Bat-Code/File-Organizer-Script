import os
import shutil

#Funcion para crear las carpetas
def createDirectorios(nombre: str, ruta: str, dirs: list):
    if nombre not in dirs:
        ruta_completa = ruta + "/" + nombre
        os.makedirs(ruta_completa, exist_ok=True)

def getExtension(direccion:str, carpetasAndExtensiones:dict, dirs: list):
    for archivo in os.listdir(direccion):
        ruta_completa = os.path.join(direccion, archivo)
        # Verifica si es un archivo y no una carpeta
        if os.path.isfile(ruta_completa):
            extension = os.path.splitext(archivo)[1]
            extension = extension[1:]  # aquí se quita el punto de la extensión
            for carpeta, extensiones in carpetasAndExtensiones.items():
                if extension in extensiones:
                    # Mueve ek archivo a la carpeta correspondiente
                    carpetaDestino = os.path.join(direccion, carpeta)
                    if not os.path.exists(carpetaDestino):
                        createDirectorios(carpeta, direccion, dirs)
                    shutil.move(ruta_completa, os.path.join(carpetaDestino, archivo))

# Estas son las carpetas que se tienen que crear
carpetasAndExtensiones = {
    'Videos' : [
        "mkv","mp4","mov"
    ],
    'Programas': [
        "exe", "msi"
    ],
    'FilesComprimidos': [
        "rar", "zip"
    ],
    'Code': [
        "html", "js", "java", "py"
    ],
    'Imagenes': [
        "png", "jpg", "jpeg"
    ],
    'Files': [
        "docx", "xlsx", "pptx", "txt", "pdf"
    ]
}

direccion = input("Ingrese la direccion: ")
xd = list(carpetasAndExtensiones.keys()) # Asi sacare el nombre de las carpetas del diccionario

# Obtener la lista de directorios raíz para evitar UnboundLocalError
for raiz, dirs, archivos in os.walk(direccion):
    break

for i in range(len(xd)): # Aqui se crean las carpetas
    createDirectorios(xd[i],direccion, dirs)

getExtension(direccion, carpetasAndExtensiones, dirs)

