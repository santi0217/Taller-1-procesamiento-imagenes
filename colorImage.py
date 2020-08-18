# biblioteca de opencv
import cv2

# clase colorImage
class colorImage:

    # constructor de la clase
    def __init__(self,path):
        self.image_path = path # recibe la ruta de la imagen
        self.image = cv2.imread(self.image_path) # lee la imagen y la almacena en self.image


    # funcion que muestra ancho y alto de la imagen
    def displayProperties(self):
        height, width, channels = self.image.shape # guarda el alto, ancho y los canales de la imagen
        print('Alto =', height) # imprime el alto de la imagem
        print('Ancho =', width) # imprime el ancho de la imagen

    #funcion que muestra la imagen original
    def showImage(self):
        cv2.imshow('image',self.image) # muestra la imagen original
        cv2.waitKey(5000) # muestra la imagen por 5 segundos

    # funcion que muestra la imagen en escala de grises
    def makeGray(self):
        Gray_image = cv2.imread(self.image_path,0) # lee la imagen guardada en self.image_path en escala de grises
        cv2.imshow('gray_image',Gray_image) # muestra la imagen en escala de grises
        cv2.waitKey(5000) # muestra la imagen por 5 segundos

    # funcion que recibe el color al que quiere pasar la imagen para mostrarla
    def colorizeRGB(self):
        print('Ingrese el color con el que quiere modificar la imagen:') # solicita el color al usuario
        color = input() # lee el color dado por el usuario
        Gray_image = cv2.imread(self.image_path, 0) # lee la imagen guardada en self.image_path en escala de grises
        Color_image = self.image.copy() # copia la imagen guardada en Color_image

        if color == 'blue':
            print('Imagen azuloza:')
            Color_image[:, :, 0] = Gray_image # canal azul en el valor de escala de grises
            Color_image[:, :, 1] = 0 # canal verde en ceros
            Color_image[:, :, 2] = 0 # canal rojo en ceros
            cv2.imshow('Blue_image', Color_image)  # muestra la imagen azuloza
            cv2.waitKey(5000) # muestra la imagen por 5 segundos

        elif color == 'green':
            print('Imagen verdoza:')
            Color_image[:, :, 0] = 0 # canal azul en ceros
            Color_image[:, :, 1] = Gray_image # canal verde en el valor de escala de grises
            Color_image[:, :, 2] = 0 # canal rojo en ceros
            cv2.imshow('Green_image', Color_image)  # muestra la imagen verdoza
            cv2.waitKey(5000) # muestra la imagen por 5 segundos

        elif color == 'red':
            print('Imagen rojiza:')
            Color_image[:, :, 0] = 0 # canal azul en ceros
            Color_image[:, :, 1] = 0 # canal verde en ceros
            Color_image[:, :, 2] = Gray_image # canal rojo en el valor de escala de grises
            cv2.imshow('Red_image', Color_image)  # muestra la imagen rojiza
            cv2.waitKey(5000) # muestra la imagen por 5 segundos

    #funcion que resalta los colores de una imagen dependiendo de su formato final RGB o BGR
    def makeHue(self):
        HSV_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV) # convierte la imagen BGR a HSV
        HSV_image[:, :, 1] = 255 # canal S a 255
        HSV_image[:, :, 2] = 255 # canal V a 255

        print('Imagen con colores resaltados en RGB:')
        RGB_image = cv2.cvtColor(HSV_image, cv2.COLOR_HSV2RGB) # convierte la imagen HSV modificada a RGB
        cv2.imshow('Hue_image_RGB', RGB_image)  # muestra la imagen RGB
        cv2.waitKey(5000) #muestra la imagen por 5 segundos

        print('Imagen con colores resaltados en BGR:')
        BGR_image = cv2.cvtColor(HSV_image, cv2.COLOR_HSV2BGR)  # convierte la imagen HSV modificada a BGR
        cv2.imshow('Hue_image_BGR', BGR_image)  # muestra la imagen BGR
        cv2.waitKey(0)  # muestra la imagen indefinidamente

