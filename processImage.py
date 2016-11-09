import argparse
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from NeuralNetwork import NeuralNetwork
import Image

class ProcessImage:
           def __init__(self,imageName,neuralNetwork):
                      self.imageName = imageName
                      self.neuralNetwork = neuralNetwork
                      self.img = cv2.imread(self.imageName,0)
                      width, height =  self.img.shape[:2]
                      print "w : ", width, " h : ", height
           def applyFilters(self):
                      self.kernel = np.ones((2,2),np.uint8)
                      self.edges = cv2.Canny(self.img,100,100)
                      self.transformacion = cv2.dilate(self.edges,self.kernel,iterations = 1)
                      self.resulting = cv2.morphologyEx(self.transformacion, cv2.MORPH_GRADIENT, self.kernel)
                      cv2.imwrite("tratada.png",self.resulting)
                      print "mostrando matris....\n"
                      self.getValuesOfX()  
                      
           def crearEquivalencias(self,value):
                      if value < 0:
                                 value = -1
                      elif value > 0:
                                 value = 1
                      return value          
           def getValuesOfX(self):
                      matriz_x =   self.resulting
                      x_to_file = []
                      x = []
                      x = matriz_x.flatten()
                      existe_patron = 0;
                      contador_divicion = 0 
                      for i in range(0,len(x)-2):
                                 if  x[i] == 255:
                                            existe_patron = 1
                                 if contador_divicion == 100:
                                            contador_divicion = 1
                                            x_to_file.append(existe_patron)
                                            existe_patron = 0
                                 contador_divicion = contador_divicion + 1
                      print "valores de array : ", x_to_file, " : cantidad : ", len(x_to_file)
                      print "cantida de pesos : ", len(self.neuralNetwork.weights[0])
                      del x_to_file[0]
                      valor = self.neuralNetwork.predict(x_to_file)[0]
                      valor = self.crearEquivalencias(valor)
                      if valor ==1:
                                 print valor, " linea"
                      elif valor==-1:
                                 print valor, " esquina"           
                      
                                 
         
