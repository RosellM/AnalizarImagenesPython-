import cv2
from processImage import ProcessImage 
from NeuralNetwork import NeuralNetwork
class UtilCam:
           def __init__(self,neuralNetwork):
                      self.neuralNetwork = neuralNetwork                     
                      self.cam = cv2.VideoCapture(0)
           def loadImage(self):
                      self.img = cv2.imread("thumbnail.png",0)
                         
           def showCam(self):
                      while(True):
                          self.ret, self.frame = self.cam.read()
                       
                          cv2.namedWindow('frame')
                          cv2.setMouseCallback('frame', self.getPixels)    
                          cv2.imshow('frame',self.frame)
                          if cv2.waitKey(1) & 0xFF == ord('q'):
                              break   
           def createFilters(self,imageName):
                      processImage = ProcessImage(imageName,self.neuralNetwork)
                      processImage.applyFilters()
                                  
           def getPixels(self,event, x, y, flags, param):
                      if event == cv2.EVENT_LBUTTONDOWN:
                                 print x , y       
                                 cropped = self.frame[y-30:y+60,x-30:x+60]
                                 cv2.imwrite("thumbnail.png", cropped)
                                 self.createFilters("thumbnail.png")
                                 
                                 

