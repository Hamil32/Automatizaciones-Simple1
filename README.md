# Renombrador de Archivos con Prefijo

Este es un script simple en Python que renombra todos los archivos en una carpeta específica, agregando un prefijo a sus nombres.

## ¿Qué hace el script?

El script realiza lo siguiente:
1. Obtiene la ruta de una carpeta especificada (`carpeta`).
2. Recorre todos los archivos en esa carpeta.
3. Agrega un prefijo (`nuevo_`) al nombre de cada archivo.
4. Renombra los archivos con el nuevo nombre.

## Requisitos

- Python 3.x instalado en tu sistema.
- Acceso a una carpeta con archivos para renombrar.

## Cómo usar

1. Clona este repositorio o descarga el script.
2. Asegúrate de que la carpeta que contiene los archivos que deseas renombrar esté en el mismo directorio que el script, o modifica la variable `carpeta_path` para que apunte a la ruta correcta.
3. Ejecuta el script con Python:

   ```bash
   python renombrador.py
   
Después de ejecutar el script, todos los archivos en la carpeta especificada tendrán el prefijo nuevo_ en sus nombres.

Ejemplo
Supongamos que tienes una carpeta llamada carpeta con los siguientes archivos:

archivo1.txt

archivo2.jpg

archivo3.pdf

Después de ejecutar el script, los archivos se renombrarán a:

nuevo_archivo1.txt

nuevo_archivo2.jpg

nuevo_archivo3.pdf

Advertencias
El script solo renombra archivos, no carpetas.

Asegúrate de hacer una copia de seguridad de tus archivos antes de ejecutar el script, ya que el cambio de nombre es irreversible.
