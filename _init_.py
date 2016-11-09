# import the necessary packages
import argparse
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import Image


global image
global edges
muestras = []
muestras_pixel = []
colorPixelsOFYUP = []
colorPixelsOFYDOWN = []

colorPixelsOFXUP = []
colorPixelsOFXDOWN = []



	
def clearMuestraArray():
	muestras_pixel = []

def createDataSet():
           archi = open("dataSet.data", "w")
           for i in muestras_pixel:
                      archi.write(i+ "\n")
           archi.close()

def getMaxWidthOfY(x,y):
	return y - 5

def getMaxWitdhOfX(x,y):
	return x - 5

def createBoxOfPixels(x,y):
	max_y =  getMaxWidthOfY(x,y)
	max_x = getMaxWitdhOfX(x,y)
	print "inicio de la matriz :", max_x, max_y,"\n"
	entradas = getValuesOfBox(max_x, max_y, max_y + 12,[])
	muestras_pixel.append(entradas)

def getValuesOfBox(max_x, max_y,gmax_y,m):
		
	if max_y < gmax_y:
		for i  in range(max_x, max_x + 12):
			pix_color  = closing[max_y,i]
			print i , max_y , " : ", pix_color
			if pix_color == 255:
			           pix_color = 1
			m.append(pix_color)
		getValuesOfBox(max_x, max_y+1,gmax_y,m)
	return ','.join([str(x) for x in m] )
		
	
		
def click_and_crop(event, x, y, flags, param):
	if event == cv2.EVENT_LBUTTONDOWN:
		print x , y
		createBoxOfPixels(x,y)
		
		
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())
 
#carga y convierte la imagen a escala de grises
img = cv2.imread(args["image"],0)
newx,newy = img.shape[1]/4,img.shape[0]/4 #new size (w,h)
newimage = cv2.resize(img,(90,90))

kernel = np.ones((2,2),np.uint8)
edges = cv2.Canny(newimage,100,100);
transformacion = cv2.dilate(edges,kernel,iterations = 1)
closing = cv2.morphologyEx(transformacion, cv2.MORPH_GRADIENT, kernel)
cv2.imwrite("tratada.png",closing)

cv2.namedWindow("image")
cv2.setMouseCallback("image", click_and_crop)
while True: 
	cv2.imshow("image", closing)	
	key = cv2.waitKey(1) & 0xFF
		# if the 'r' key is pressed, reset the cropping region
        if key == 100:
        	print "Datos guardados...."
        	createDataSet()
        	break;
        	
 
cv2.destroyAllWindows()
