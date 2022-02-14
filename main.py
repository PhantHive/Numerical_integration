from src.square_method import Square
from src.trapezoidal_method import Trapezoidal
from src.midpoint import MidPoint
from src.simpson import Simpson
from src.gauss_legendre import GL
from scipy.integrate import quad


# Functions

def f(x):
    return 1 / (1 + x ** 2)



if __name__ == '__main__':
    N = 10

    print(quad(f, 0, 2))

    # ==============
    # Square method
    # square_method = Square(f, 0, 2, N)
    # SR = square_method.SRight()
    # SL = square_method.SLeft()
    # print("Left square method: ", SL)
    # print("Right square method: ", SR)
    # ==============
    # Trapezoidal method
    # trapez_method = Trapezoidal(f, 0, 2, N)
    # print(trapez_method.TMethod()) ii
    # ==============
    # Midpoint method
    # mp_method = MidPoint(f, 0, 2, N)
    # print(mp_method.MPmethod())
    # ==============
    # Simpson method
    # simpson_method = Simpson(f, 0, 2, N)
    # print(simpson_method.MSimpson())
    # ==============
    # Gauss Legendre method
    # gl2 = GL(f, 0, 2, N)
    # print(gl2.gl2())