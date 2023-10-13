import os
import shutil

#Funcion para crear las carpetas
def createDirectorios(nombre:str, ruta:str):
    for raiz, dirs, archivos in os.walk(ruta):
        dirs[:] = [] # Aqui evito que lea los subdirectorios
    if nombre not in dirs:
        ruta_completa = ruta + "/" + nombre
        os.makedirs(ruta_completa, exist_ok=True)

def getExtension(direccion):
    for archivo in os.listdir(direccion):
        extension = os.path.splitext(archivo)[1]
        extension = extension[1:]  # aqui se quita el punto de la extension

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

xd = list(carpetasAndExtensiones.keys()) # Asi sacare el nombre de las carpetas del diccionario
direccion = "C:/Users/juand/Downloads/prueba"

for i in range(len(xd)): # Aqui se crean las carpetas
    createDirectorios(xd[i],direccion)



