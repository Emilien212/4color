import numpy as np

# Assuming a domain X x Y - [0, 1] x [0, 1]

class Circle:
    def __init__(self):
        # x = r*sin(t) + a
        # y = r*sin(t) + b
        self.a = np.random.uniform(low=0.2, high=0.8)
        self.b = np.random.uniform(low=0.2, high=0.8)
        self.r = np.random.uniform(low=0.1, high=0.5)

        __T = np.linspace(0, 2*np.pi, 10000)

        self.X = self.r*np.cos(__T) + self.a
        self.Y = self.r*np.sin(__T) + self.b
    

    def isIn(self, x, y):
        # (x-a)**2 + (y-b)**2 = r**2
        if (x-self.a)**2 + (y-self.b)**2 > self.r**2:
            return False
        else:
            return True
        

class Square:
    def __init__(self):
        # Four points + closing
        self.a = np.random.uniform(low=0.2, high=0.8)
        self.b = np.random.uniform(low=0.2, high=0.8)
        self.c = np.random.uniform(low=0.2, high=1)

        self.X = np.zeros(5)
        self.Y = np.zeros(5)

        self.X[0], self.Y[0] = (self.a + 1/2*self.c, self.b + 1/2*self.c)
        self.X[1], self.Y[1] = (self.a - 1/2*self.c, self.b + 1/2*self.c)
        self.X[2], self.Y[2] = (self.a - 1/2*self.c, self.b - 1/2*self.c)
        self.X[3], self.Y[3] = (self.a + 1/2*self.c, self.b - 1/2*self.c)
        self.X[4], self.Y[4] = (self.a + 1/2*self.c, self.b + 1/2*self.c)
    
    def isIn(self, x, y):
        if x < self.a + 1/2*self.c and x > self.a - 1/2*self.c and y < self.b + 1/2*self.c and y > self.b - 1/2*self.c:
            return True
        else:
            return False


class Line:
    def __init__(self):
        # Two points
        self.a = np.random.uniform(low=-2, high=2)
        self.b = np.random.uniform(low=-1, high=2)

        self.X = np.zeros(2)
        self.Y = np.zeros(2)

        self.X[0], self.Y[0] = (0, self.b)
        self.X[1], self.Y[1] = (1, self.a + self.b)
    
    def isIn(self, x, y):
        if y < self.a*x + self.b:
            return True
        else:
            return False