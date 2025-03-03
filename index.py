import os 

#Obtener la ruta de la carpeta donde estan los archivos
carpeta_path = "carpeta"

#Obtener lista con los nombres de archivos en la carpeta
archivos = os.listdir(carpeta_path)

#Prefijo que se agregara al nombre de cada archivo
prefijo = "nuevo_"

#Iteraciones con los archivos de la carpeta
for nombre_archivo in archivos:
    #Obtener ruta completa del archivo
    archivo_path = os.path.join(carpeta_path, nombre_archivo)
    
    #Validar si es o no una carpeta dentro de la carpeta principal
    if os.path.isfile(archivo_path):
        #obtener el nuevo nombre
        nuevo_archivo = prefijo + nombre_archivo

        #obtener ruta completa del nuevo archivo
        nuevo_archivo_ruta = os.path.join(carpeta_path, nuevo_archivo)
        
        #Renombrar el archivo
        os.rename(archivo_path, nuevo_archivo_ruta)