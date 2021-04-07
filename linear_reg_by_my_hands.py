import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

#Linear Regression with 2 vars
# y = a + bx

x = np.array([1,2,3,4,5,6,7,8,9,10,11,12]).reshape(-1,1)
y = np.array([15000, 25000,27000,30000,31278,35456,37800,40000,52000,55000,67000,70000]).reshape(-1,1)

def linear_regression(x , y ):
    
    X = np.array(x , dtype ="float32")
    Y = np.array(y, dtype = "float32")
    
    #получаем суммы для Х и У 
    sum_x = sum(X)
    sum_y = sum(Y)
    
    #получим сумму квадратов X 
    sum_x_v_2 = sum(X**2)
    
    # получим сумму произведений X*Y
    
    sum_xy = sum(X*Y)
    
    #получим n данных
    n = len(x)
    #решаем систему уравнений
    Matrix = np.array(  [ [n , sum_x],
                      [sum_x , sum_x_v_2] ] , dtype="float32" )
    print("Matrix : ", Matrix , "   ", Matrix.shape)
    
    vector = np.array([sum_y , sum_xy], dtype="float32")
    print("vector :", vector)
    #получаем два коеффициента для y = a+bx
    a,b = np.linalg.solve(Matrix , vector)
    
    print(" y = ", a ," + ",b," x")
    return a,b
    
    linear_regression(x , y)
