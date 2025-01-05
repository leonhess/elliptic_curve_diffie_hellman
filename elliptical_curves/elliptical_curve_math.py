class math:
    def are_points_equal(P1,P2):
        if P1.getX() == P2.getX() and P1.getY() == P2.getY():
            return True 
        else:
            return False

# basic math operators
    def subtract(x,y,p):
        sub = x-y 
        sub = sub % p
        return sub

    def add(x, y, p ):
        sum_ = x+y 
        sum_ = sum_ % p
        return sum_

    def multiply( X, Y, p):
        Z = X*Y
        #Z = Z % p
        return Z
    
    def inverse(N,p):
        multiplicative_inverse_modul = pow(N,-1,p)
        return multiplicative_inverse_modul 

    #def divide(self, Z,N,p):

    #    r = self.multiply(Z,multiplicative_inverse_modul)
    #    r = r % p
    #    return r 

    def power(B,E,p):
        r = B**E
        r = r % p
        return r 
