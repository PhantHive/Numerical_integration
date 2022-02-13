from src.square_method import Square
from src.trapezoidal_method import Trapezoidal
from src.midpoint import MidPoint
from scipy.integrate import quad


# Functions

def f(x):
    return 1 / (1 + x ** 2)


# methode trapezes
def MTrapezes(f, a, b, N):
    """Cette fonction permet de calculer une approximation de l'integrale d'une fonction
    par la methode des trapezes."""

    longueur = (b - a) / N
    aire = 0

    for i in range(N):
        aire += (f(a + i * longueur) + f(a + (i + 1) * longueur)) * longueur / 2

    return (aire)


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
    # print(trapez_method.TMethod())
    # ==============
    # Midpoint method
    # mp_method = MidPoint(f, 0, 2, N)
    # print(mp_method.MPmethod())
