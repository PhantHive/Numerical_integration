class Trapezoidal:


    def __init__(self, f, a, b, N):

        self.f = f
        self.a = a
        self.b = b
        self.N = N
        self.h = (self.b - self.a) / self.N

    def TMethod(self):

        TM = self.h * 0.5*(self.f(self.a) + self.f(self.a + self.N*self.h))
        for i in range(1, self.N):
            TM += self.h*(self.f(self.a + i*self.h))

        return TM