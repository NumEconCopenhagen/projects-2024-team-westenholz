def square(x):
    """ square numpy array
    
    Args:
    
        x (ndarray): input array
        
    Returns:
    
        y (ndarray): output array
    
    """
    
    y = x**2
    return y 



from types import SimpleNamespace

from types import SimpleNamespace
import numpy as np

class ExchangeEconomyClass:

    def __init__(self):
        par = self.par = SimpleNamespace()
        # a. preferences
        par.alpha = 1/3
        par.beta = 2/3
        # b. endowments
        par.w1A = 0.8
        par.w2A = 0.3

    def utility_A(self, x1A, x2A):
        par = self.par
        return x1A**par.alpha * x2A**(1 - par.alpha)

    def utility_B(self, x1B, x2B):
        par = self.par
        return x1B**par.beta * x2B**(1 - par.beta) 

    def demand_A(self, p1):
        par = self.par
        x1A = par.alpha * (p1 * par.w1A + par.w2A) / p1
        x2A = (1 - par.alpha) * (p1 * par.w1A + par.w2A)
        return x1A, x2A

    def demand_B(self, p1):
        par = self.par
        x1B = par.beta * (p1 * (1 - par.w1A) + (1 - par.w2A)) / p1
        x2B = (1 - par.beta) * (p1 * (1 - par.w1A) + (1 - par.w2A))
        return x1B, x2B

    def check_market_clearing(self, p1):
        par = self.par
        x1A, x2A = self.demand_A(p1)
        x1B, x2B = self.demand_B(p1)
        eps1 = x1A - par.w1A + x1B - (1 - par.w1A)
        eps2 = x2A - par.w2A + x2B - (1 - par.w2A)
        return eps1, eps2
    
    def question1(self):
        self.list_x1A = []
        self.list_x2A = []
        for j in range(76):
            x1A = j / 75
            for i in range(76):
                x2A = i / 75
                x1B = 1 - x1A
                x2B = 1 - x2A
                if self.utility_A(x1A, x2A) >= self.utility_A(self.par.w1A, self.par.w2A) and \
                   self.utility_B(x1B, x2B) >= self.utility_B((1 - self.par.w1A), (1 - self.par.w2A)):
                    self.list_x1A.append(x1A)
                    self.list_x2A.append(x2A)

    def question2(self):
        self.price_list = []
        self.error1 = []
        self.error2 = []
        for var in range(76):
            price = 0.5 + 2 * (var / 75)
            eps1, eps2 = self.check_market_clearing(price)
            self.price_list.append(price)
            self.error1.append(eps1)
            self.error2.append(eps2)

    def market_clearing_price(self, p1, max_iter=500):
        par = self.par
        eps = 1e-8    
        t = 0
        while t < max_iter:
            eps1, eps2 = self.check_market_clearing(p1)
            if np.abs(eps1) < eps:
                break
            p1 = p1 + 0.5 * eps1 / par.alpha
            t += 1
        if t == max_iter:
            print("Warning: Maximum iterations reached without convergence.")
        return p1

    def market_clearing_price_Q8(self, p1, max_iter=500):
        par = self.par
        eps = 1e-8    
        t = 0
        while t < max_iter:
            eps1, eps2 = self.check_market_clearing(p1)
            if np.abs(eps1) < eps:
                break 
            if par.alpha != 0:
                p1 = p1 + 0.5 * eps1 / par.alpha
            else:
                raise ValueError("Alpha parameter cannot be zero.")
            t += 1
        if t == max_iter:
            print("Warning: Maximum iterations reached without convergence.")
        return p1




    
    