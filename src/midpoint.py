class MidPoint:

    def __init__(self, f, a, b, N):

        self.f = f
        self.a = a
        self.b = b
        self.N = N
        self.h = (self.b - self.a) / self.N


    def MPmethod(self):

        MP = 0
        for i in range(self.N):

            xi = self.a + i*self.h
            ci = xi + self.h/2

            MP += self.h*(self.f(ci))

        return MP