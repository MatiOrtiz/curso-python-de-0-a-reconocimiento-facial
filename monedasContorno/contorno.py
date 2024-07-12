import cv2
imagen=cv2.imread('contorno.jpg')


#Para mostrar
cv2.imshow('imagen',imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()