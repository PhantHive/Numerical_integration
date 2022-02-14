class Simpson:

    def __init__(self, f, a, b, N):

        self.f = f
        self.a = a
        self.b = b
        self.N = N

        self.h = (self.b - self.a) / self.N

    def MSimpson(self):

        MS = 0
        for i in range(self.N):
            xi = self.a + i*self.h
            ci = xi + self.h/2
            MS += (self.h/6)*(self.f(self.a + i*self.h) + 4*self.f(ci) + self.f(self.a + (i+1)*self.h))

        return MS