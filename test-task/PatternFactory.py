from math import *


class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __str__(self):
        return f'x:{self.x},y:{self.y}'

@staticmethod
def new_decart_point(x,y):
    return point(x,y)

@staticmethod
def new_polar_point(rho,theta):
    return point(rho*cos(theta),rho*sin(theta))

if __name__=='__main__':
    decart = new_decart_point(2, 3)
    polar = new_polar_point(1, 2)
    print(decart, polar)

