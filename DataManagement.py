from NeuralNetwork import NeuralNetwork
from UtilCam import UtilCam
import numpy as np
from sklearn.metrics import confusion_matrix,classification_report
import scipy as sp
import matplotlib.pyplot as plt
#cargar  mas muestras
#agregaar lineas, esquina, cruces
#hacer validacion crusada
#guardar datos para graficar
#hacer documentos de funciones

class DataManagement:
           def __init__(self):
                      self.x=[]
                      self.X=[]
                      self.y=[]
                      self.Y=[]
                      self.i = 0
                      self.entradas = []
                      self.salidas = []
                      self.datos = []
           def loadAllData(self):
                      self.file = open('dataSet.data', 'r')
                      for line in self.file:
                                 self.y = line.split("=")
                                 self.x = line.split(",")
                                 index = len(self.x) -1
                                 element = self.x[index]
                                 self.x.remove(element)
                                 for j in range(0, len(self.x)):
                                            self.x[j]  = int(self.x[j])
                                 self.X.append(self.x)
                                 self.Y.append(int(self.y[1].replace("\n", '')))
                      
           def selectRegionForTraining(self,iteracion):
                      regions_validacion = [];
                      regions_validacion.append([0,40]);
                      regions_validacion.append([40,80]);
                      regions_validacion.append([80,120]);
                      print "aqui estoy xD"
                      self.datos = []
                      if iteracion == 0:
                                 self.valor_inicial = regions_validacion[iteracion][0]
                                 self.valor_final = regions_validacion[iteracion][1]
                                 print " valor iniciar : " ,self.valor_inicial
                                 print "valor final : " ,self.valor_final
                      elif iteracion == 1:
                                 self.valor_inicial = regions_validacion[iteracion][0]
                                 self.valor_final = regions_validacion[iteracion][1]
                                 print " valor iniciar : " ,self.valor_inicial
                                 print "valor final : " ,self.valor_final
                      elif iteracion == 2:
                                 self.valor_inicial = regions_validacion[iteracion][0]
                                 self.valor_final = regions_validacion[iteracion][1]
                                 print " valor iniciar : " ,self.valor_inicial
                                 print "valor final : " ,self.valor_final
                      for line in range(0, 89):
                                 if line < self.valor_inicial or line > self.valor_final:
                                            self.entradas.append(self.X[line])
                                            self.salidas.append(self.Y[line])
                      self.datos.append(self.entradas)
                      self.datos.append(self.salidas)  
                      return self.datos
                      
           def selectRegionForPredict(self):
                      self.entradas = []
                      self.salida = []
                      self.datos = []
                      for line in range(self.valor_inicial,self.valor_final):
                                 self.entradas.append(self.X[line])
                                 self.salidas.append(self.Y[line])
                      self.datos.append(self.entradas)
                      self.datos.append(self.salidas)          
                      return self.datos
           
           def createMatrix(self, salidas_esperadas,salidas_dadas,matriz,iteracion):
                      print "numero A ",len( salidas_esperadas)
                      print "numero B ",len( salidas_dadas )
                      y_true = []
                      y_pred = []
                      for i in range(0,len(salidas_esperadas)):
                          salida_esperada = salidas_esperadas[i]
                          salida_dada = self.crearEquivalencias(salidas_dadas[i])
                          y_true.append(salida_esperada)
                          y_pred.append(salida_dada)
                      print confusion_matrix(y_true, y_pred, labels=[-1, 0, 1])  
                      print classification_report(y_true,y_pred)
                      archi = open("matriz-"+str( iteracion )+".data", "w")
                      for x in confusion_matrix(y_true, y_pred, labels=[-1, 0, 1]):
                                 archi.write(str(x))
                                 archi.write("\n")
                      archi.close() 
                      archi2 = open("reporte_clasificacion-"+str (iteracion) +".data","w")
                      archi2.write(classification_report(y_true,y_pred))
                      archi.close()    
           def crearEquivalencias(self,value):
                      if value < 0:
                                 value = -1
                      elif value > 0:
                                 value = 1
                      return value
           def createGaphics(self,nn,iteracion):
                                x = sp.linspace(0, 10, 20)
                                y = []
                                for i in nn.getError():
                                            y.append(i)
                                plt.figure()

                                 # Representamos
                                plt.plot(x,y)
                                plt.savefig('plotCompleta-'+str( iteracion )+'.png')
           def main(self):                     
                      nn = NeuralNetwork([80,80,1]);
                      #loadFileForTraining()
                      data.loadAllData()
                      salidas_dadas = []
                      salidas_esperadas = []
                      nn.show()
                      for i in range(0,3):
                                 salidas_esperadas = []
                                 salidas_dadas = []
                                 valores  = self.selectRegionForTraining(i)
                                 nn.fit(valores[0], valores[1])
                                 valores  = self.selectRegionForPredict()
                                 for k in range(0, len(valores[0])):
                                            salida_dada = nn.predict(valores[0][k])
                                            salidas_dadas.append(salida_dada);
                                            salidas_esperadas.append(valores[1][k])
                                            print("Salida dada : " ,salida_dada, "salida esperada : ", valores[1][k] )
                                 self.createMatrix(salidas_esperadas,salidas_dadas,[],i)
                                 self.createGaphics(nn,i)
                      util = UtilCam(nn)
                      util.showCam()
                      print "\n"
data = DataManagement()
data.main()

