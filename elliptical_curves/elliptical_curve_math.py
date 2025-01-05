def are_points_equal(P1,P2):
    if P1.getX() == P2.getX() and P1.getY() == P2.getY():
        return True 
    else:
        return False

# basic math operators
def subtract(x,y):
    return x-y

def add(x, y, p ):
    return x+y

def multiply(X, Y, p):
    Z = X*Y 
    return Z

def divide(Z,N,p):
    multiplicative_inverse_modul = pow(N,-1,p)
    r = multiply(Z,multiplicative_inverse_modul)
    r = r % p
    return r 

def power(B,E,p):
    r = B**E % p
    return r 
