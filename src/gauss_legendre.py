from math import sqrt


class GL:


    def __init__(self, f, a, b, N):

        self.f = f
        self.a = a
        self.b = b
        self.N = N

        self.h = (self.b - self.a)/self.N


    def gl2(self):

        gl2 = 0
        for i in range(self.N):
            a = (self.h/(2 * sqrt(3)))
            xi = self.a + i * self.h
            ci = xi + self.h / 2
            gl2 += self.h * 0.5 * (self.f(ci - a) + self.f(ci + a))

        return gl2


    def gl3(self):

        gl3 = 0
        for i in range(self.N):
            xi = self.a + i * self.h
            ci = xi + self.h / 2
            gl3 += (self.h / 18) * (5 * self.f(ci - (sqrt(3/20) * self.h)) + 8 * self.f(ci) + 5 * self.f(ci + sqrt(3/20) * self.h))

        return gl3



