import cv2
import os
import numpy as np
import time

#os.chdir(r'F:\UDEC\HTML\otros\python')

#leer las imagenes del archivo
imagen1 = cv2.imread("img1.png", 1)
imagen2 = cv2.imread("img2.png", 1)

newimg1 = cv2.resize(imagen1, (500, 300))
newimg2 = cv2.resize(imagen2, (500, 300))

diferencia = cv2.subtract(newimg1, newimg2)

#definir funcion de comparacion
def compara (im1, im2):
	diferencia = cv2.subtract(im1, im2)
	if not np.any(diferencia):
		print("Las imagenes son iguales")
	else:
		print("Las imagenes son diferentes")

#mostrar las dos imagenes en pantalla
imas = np.hstack((newimg1, newimg2))
cv2.imshow("fotos", imas)
cv2.waitKey(0)
cv2.destroyAllWindows()

#crear imagen de diferencia
cv2.imwrite("imDiferencia.png", diferencia) 
cv2.imshow("diferencia", diferencia)
cv2.waitKey(0)
cv2.destroyAllWindows()

compara(newimg1, newimg2)
print(diferencia)