#Programa que crea un gif
import sys

from PIL import Image

images = []

for arg in sys.argv[1:]: #usamos slides para saltar el nombre del programa
    image = Image.open(arg) #abrimos las imagenes pasadas por los argumentos
    images.append(image)
    
images[0].save(
    "costumes.gif", save_all=True, append_images=[images[1]], duration=200, loop=0
)

