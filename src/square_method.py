class Square:


    def __init__(self, f, a, b, N):
        '''
        :param f: f(x)
        :param a: left interval
        :param b: right interval
        :param N: number of subintervals
        '''

        self.f = f
        self.a = a
        self.b = b
        self.N = N

        self.h = (self.b - self.a) / self.N


    def SLeft(self):
        '''
        :return: left integration (LI)
        '''

        LI = 0
        for i in range(self.N):
            LI += self.h * self.f(self.a + i*self.h)

        return LI

    def SRight(self):
        '''
        :return: right integration (RI)
        '''
        DI = 0
        for i in range(1, self.N + 1):
            DI += self.h * self.f(self.a + i*self.h)

        return DI





