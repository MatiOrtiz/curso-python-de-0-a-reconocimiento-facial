from cv2 import cv2
imagen=cv2.imread('/monedasControno/contorno.jpg')
grises= cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
umbral= cv2.threshold(grises,100,255,cv2.THRESH_BINARY)

#Para mostrar
cv2.imshow('imagen',imagen)
cv2.imshow('imagen de grises',grises)
cv2.waitKey(0)
cv2.destroyAllWindows()