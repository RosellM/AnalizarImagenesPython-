import argparse
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import Image

to_file = []
for nmXd in range(0,3):
           for imagen in range(1,30):
                      print imagen
                      
                      matriz_x =   cv2.imread("tratada"+str(imagen)+".png",0)
                      x_to_file = []
                      x = []
                      x = matriz_x.flatten()
                      print "total de x : ", len(x)
                      existe_patron = 0;
                      contador_divicion = 0 
                      for i in range(1,len(x)):
                                 print "valor del gris : ", x[i]
                                 if  x[i] == 255:
                                            existe_patron = 1
                                 if contador_divicion == 100:
                                            contador_divicion = 1
                                            x_to_file.append(existe_patron)
                                            existe_patron = 0
                                 contador_divicion = contador_divicion + 1
                      to_file.append(x_to_file)
                      print "valores de array : ", x_to_file,"\n"
                      print len(x_to_file)
archi = open("dataSet.data", "w")
for i in to_file:
           archi.write(','.join([str(x) for x in i] ))
           archi.write("\n")
archi.close()
