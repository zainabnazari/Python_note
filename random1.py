# file name: random1.py

# To generate a 1D random number between [0,1):
import numpy as np
x=np.random.rand(5)
print(x)
'''
output:
[0.90907376 0.13799189 0.58644767 0.9362912  0.22169574]
'''
# To generate a 2D random number:
y=np.random.rand(2,2)
print(y)

'''
output:
[[0.63012486 0.50949039]
 [0.83741808 0.63140463]]
'''
# To generate a nD random number:
# myrandom=np.random.rand(1D,2D,3D,..,nD)


# To generate random number with Gaussian distribution
# np.random.normal(mean, standard deviation, shape)
# one dimension: np.random.normal(mean, standard deviation, 1d)
xg=np.random.normal(0.0,1.0,5)
print(xg)

'''
output:
[-0.16594284  1.50995672 -0.93375937 -0.01684865  0.13507735]

'''
# To generate random Gaussian distribution with shape 2D:

yg=np.random.normal(0.0,1.0,(2,2))
print(yg)

'''
output:

[[ 0.89220523  0.98818578]
 [ 0.40821246 -0.7114725 ]]

'''
# To generate Guasssian random number for nD
# yg=np.random.normal(mean,standard deviation,(1D,2D,3D,...nD))
