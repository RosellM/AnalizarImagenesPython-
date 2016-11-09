import numpy as np

def tanh(x):
    return np.tanh(x)

def tanh_deriv(x):
    return 1.0 - np.tanh(x)**2

def logistic(x):
    return 1/(1 + np.exp(-x))

def logistic_derivative(x):
    return logistic(x)*(1-logistic(x))

#[143,143,1]
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
            self.weights.append((1*np.random.random((layers[i - 1] + 1, layers[i]+1))-1)*0.25) #3 , 3
        print layers[i] + 1, layers[i+1]
        self.weights.append((2*np.random.random((layers[i] + 1, layers[i+1]))-1)*0.25)
        
        
    def show(self):
           print self.weights[0] , self.weights[1];
               
    def fit(self, X, y, learning_rate=0.2, epochs=1000):
        print X
        X = np.atleast_2d(X)      
        temp = np.ones([X.shape[0],X.shape[1]+1])
        temp[:, 0:-1] = X  # adding the bias unit to the input layer
        X = temp
        Y = np.array(y)
        print X, Y
        for k in range(epochs):
            print "<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>><>>>>>>>>>>>>>>>>>>><<<<<<<<<<<>>>>>>>>>>"
            i = np.random.randint(X.shape[0])
            a = [X[i]]
            for l in range(len(self.weights)):
            #pesos por valores de x
                print "x * w : ", a[l],"  *   ", self.weights[l]
                #ingresa valores de activation a a[]
                a.append(self.activation(np.dot(a[l], self.weights[l])))            
            print "mostrando datos agregados a A " ,  a
            print "y - y' : ", y[i] , " - " , a[-1]
            error = y[i] - a[-1]
            print "error * funcion de activation : [  " , error ," * ", self.activation_deriv(a[-1])," ]"
            
            
            deltas = [error * self.activation_deriv(a[-1])]
            for l in range(len(a) - 2, 0, -1): #(1,0,-1)  we need to begin at the second to last layer           
                deltas.append(deltas[-1].dot(self.weights[l].T)*self.activation_deriv(a[l]))
            deltas.reverse()
            
            print "deltas : ", deltas
            
         
            
            for i in range(len(self.weights)):
                print "before delta :" , deltas[i] , "layer :" , a[i]
                layer = np.atleast_2d(a[i])
                
                delta = np.atleast_2d(deltas[i])
                
                print "delta :" , delta , "layer :" , layer
                
                print "aprendizaje : " , self.weights[i] ,"  + = ", learning_rate ," * ", layer.T.dot(delta)
                self.weights[i] += learning_rate * layer.T.dot(delta)
     
    def predict(self,x):
           x = np.array(x)
           temp = np.ones(x.shape[0]+1)
           temp[0:-1] = x
           a = temp
           for l in range(0, len(self.weights)):
                      a = self.activation(np.dot(a, self.weights[l]))
           return a

nn = NeuralNetwork([2,2,1]);

X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([0, 1, 1, 0])
nn.show()
nn.fit(X, y)

for i in [[0, 0], [0, 1], [1, 0], [1,1]]:
    print(i,nn.predict(i))
