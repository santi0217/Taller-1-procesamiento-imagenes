#  Fecha: 17 de agosto del 2020
#
#  Autor: Santiago Márquez Álvarez
#
#  Descripción: el codigo consiste en la utilización de una clase llamada colorImage
#               la cual recibe del usuario la ruta de una imagen de su ordenador con
#               el fin de visualizar sus dimensiones, y tratar los valores de sus colores
#               para poder verla en escala de grises, colorizarla de rojo, verde o azul y
#               poder resaltar uno de sus colores dependiendo si se quiere en formato RGB
#               o BGR.

# importa la clase de colorImage
from colorImage import *

# funcion principal main
if __name__ == '__main__':

    print('Ingrese la ruta de la imagen a tratar:') # solicita la ruta de la imagen al usuario
    ruta_imagen = input() # lee la ruta dada por el usuario
    Img = colorImage(ruta_imagen) # construye la clase guardando la imagen
    print('Imagen seleccionada:')
    Img.showImage() #muestra la imagen original
    print('Dimensiones de la imagen:')
    Img.displayProperties() # imprime alto y ancho de la imagen
    print('Imagen en escala de grises:')
    Img.makeGray() # muestra imagen en escala de grises

    Img.colorizeRGB() # muestra la imagen azuloza,verdoza o rojiza

    Img.makeHue() # muestra la imagen modficada en HSV y convertida a RGB

