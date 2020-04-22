import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import os
dirPath = 'C:\\Users\\James\\Desktop\\CIT\\5_DeepLearning\\Labs'


def MSE(Ypred, Y):  
    m = Y.shape[0]
    mse = sum((Ypred - Y)**2) / (m+2)
    return mse


def gradientDescent(bias, lambda1, alpha, Ypred, Y, X):   
    error = Ypred - Y
    m = Y.shape[0]
    
    lambda1 = lambda1 - alpha/(2*m) * sum(error * X)  
    bias = bias - alpha/(2*m) * sum(error)    
    return bias, lambda1


def linearRegression(X, Y):  
    # set initial parameters for model
    bias = 0
    lambda1 = 0
    alpha = 0.5 # learning rate
    max_iter = 50
    
    for iteration in range(1, max_iter +1):
       Ypred = lambda1 * X + bias
       print("iteration", iteration, ":", MSE(Ypred, Y))   
       bias, lambda1 = gradientDescent(bias, lambda1, alpha, Ypred, Y, X)

    # plot the data and overlay the linear regression model
    yPredictions = (lambda1*X)+bias
    plt.scatter(X, Y)
    plt.plot(X,yPredictions,'k-')
    plt.show()



def main():    
    # a. Read data into a dataframe
    df = pd.read_excel(os.path.join(dirPath, 'data.xlsx'))
    df = df.dropna() 

    # c. Visualize the relationship between the X feature and the target Y value
    #X = df.values
    #plt.scatter(X[:,1], X[:,0])
    #plt.show()

    # b. Convert and Store feature and target data in seperate NumPy arrays
    Y = df['Y'].values
    X = df['X'].values
    
    # d. Perform standarization on the feature data
    X = (X - np.mean(X))/np.std(X)
      
    # e. Perfrom linear regression uing gradient descent
    linearRegression(X, Y)
    

main()
