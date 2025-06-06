import numpy as np
import matplotlib.pyplot as plt
import sklearn.linear_model as lm
from sklearn.metrics import mean_squared_error

def non_func(x):
    y = 1.6345 - 0.6235*np.cos(0.6067*x) - 1.3501*np.sin(0.6067*x) - 1.1622 * np.cos(2*x*0.6067) - 0.9443*np.sin(2*x*0.6067)
    return y

def add_noise(y):
    np.random.seed(14) 
    varNoise = np.max(y) - np.min(y)  
    y_noisy = y + 0.1*varNoise*np.random.normal(0,1,len(y))
    return y_noisy

x = np.linspace(1,10,100)

y_true = non_func(x)

y_measured = add_noise(y_true)

#prikaz stvarnih i izmjerenih vrijednosti
plt.figure(1)
plt.plot(x, y_measured, 'ok', label='Mjerena vrijednost')
plt.plot(x, y_true, label='Stvarna vrijednost')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc=4)
plt.show()

#trening i test skup
np.random.seed(12)
indeksi = np.random.permutation(len(x))
indeksi_train = indeksi[0:int(np.floor(0.7*len(x)))]
indeksi_test = indeksi[int(np.floor(0.7*len(x)))+1:len(x)]

x = x[:, np.newaxis]
y_measured = y_measured[:, np.newaxis]

#trening
xtrain = x[indeksi_train]
ytrain = y_measured[indeksi_train]

#testiranje
xtest = x[indeksi_test]
ytest = y_measured[indeksi_test]

#prikaz podataka
plt.figure(2)
plt.plot(xtrain, ytrain, 'ob', label='Trening')
plt.plot(xtest, ytest, 'or', label='Test')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc=4)
plt.show()

linearModel = lm.LinearRegression()
linearModel.fit(xtrain, ytrain)

print('Model je oblika y_hat = Theta0 + Theta1 * x')
print('y_hat = ', linearModel.intercept_, '+', linearModel.coef_, '*x')
u
ytest_p = linearModel.predict(xtest)

MSE_test = mean_squared_error(ytest, ytest_p)

plt.figure(3)
plt.plot(xtest, ytest_p, 'og', label='Predvidjeno')
plt.plot(xtest, ytest, 'or', label='Test')
plt.legend(loc=4)

x_pravac = np.array([1,10])
x_pravac = x_pravac[:, np.newaxis]
y_pravac = linearModel.predict(x_pravac)
plt.plot(x_pravac, y_pravac)
plt.show()
