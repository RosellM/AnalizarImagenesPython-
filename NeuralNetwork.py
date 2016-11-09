import numpy as np

def tanh(x):
    return np.tanh(x)

def tanh_deriv(x):
    return 1.0 - np.tanh(x)**2

def logistic(x):
    return 1/(1 + np.exp(-x))

def logistic_derivative(x):
    return logistic(x)*(1-logistic(x))
    
class NeuralNetwork:
    def __init__(self, layers, activation='tanh'):
        if activation == 'logistic':
            self.activation = logistic
            self.activation_deriv = logistic_derivative
        elif activation == 'tanh':
            self.activation = tanh
            self.activation_deriv = tanh_deriv
        self.weights = []
        for i in range(1, len(layers) - 1):
            print"capa ", i
            self.weights.append((1*np.random.random((layers[i - 1] + 1, layers[i]+1))-1)*0.25)
        self.weights.append((2*np.random.random((layers[i] + 1, layers[i+1]))-1)*0.25)
        print "conjunto de pesos : ",len(self.weights)
        
        #print "c1 : ",len(self.weights[0])
        #print "c2 : ",len(self.weights[1])
        #print "c3 : ",len(self.weights[2])
        #print "cs : ",len(self.weights[3])
        archi = open("weights.data", "w")
        for i in self.weights:
                      archi.write(','.join([str(x) for x in i] ))
                      archi.write("\n")
        archi.close()
        
    def show(self):
           print self.weights[0] , self.weights[1];
               
    def fit(self, X, y, learning_rate=0.2, epochs=10000):
        self.deltas = []
        self.errorArray  = []
        X = np.atleast_2d(X)      
        temp = np.ones([X.shape[0],X.shape[1]+1])
        temp[:, 0:-1] = X  # adding the bias unit to the input layer
        X = temp
        Y = np.array(y)
        print "Realizando entrenamiento..."
        for k in range(epochs):
            i = np.random.randint(X.shape[0])
            a = [X[i]]
            for l in range(len(self.weights)):
            #pesos por valores de x
                #ingresa valores de activation a a[]
                a.append(self.activation(np.dot(a[l], self.weights[l])))                        
            error = y[i] - a[-1]
            
            if k % 500 == 0:
                      print "iteracion : ", k, " Error :", error
                      self.errorArray.append(error)
            deltas = [error * self.activation_deriv(a[-1])]
            for l in range(len(a) - 2, 0, -1):        
                deltas.append(deltas[-1].dot(self.weights[l].T)*self.activation_deriv(a[l]))
            deltas.reverse()
            for i in range(len(self.weights)):             
                layer = np.atleast_2d(a[i])
                delta = np.atleast_2d(deltas[i])
                self.weights[i] += learning_rate * layer.T.dot(delta)
    def getError(self):
           return self.errorArray
    def predict(self,x):
           x = np.array(x)
           temp = np.ones(x.shape[0]+1)
           temp[0:-1] = x
           a = temp
           for l in range(0, len(self.weights)):
                      a = self.activation(np.dot(a, self.weights[l]))
           return a
    


