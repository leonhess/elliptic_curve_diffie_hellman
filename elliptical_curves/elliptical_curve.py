import secrets
from .elliptical_curve_math import math as e_math
from .point import point

#definition of curve 
# y**2 = x**3 +A*x +B

class elliptical_curve:
    def  __init__(self, p_p, p_a, p_b, p_G, p_h):
        print("init elliptical_curve")
        self.p =p_p #modulo
        
        self.a = p_a #curve parameter
        self.b = p_b #curve parameter 
        #self.n = p_n # order 
        self.h = p_h # cofactor
        if self.is_on_curve(p_G):
            self.G = p_G # Generator Point
        else:
            print("Error Generator point not on curve")

    ## simple curve functions 
    def is_on_curve(self, P):
        x = P.getX()
        y = P.getY()
        eq1 = e_math.power(y,2,self.p)
        eq2 = e_math.power(x,3,self.p)
        eq3 = e_math.multiply(self.a, x, self.p)
        eq4 = e_math.add(eq2, eq3, self.p)
        eq5 = e_math.add(eq4, self.b, self.p)

        return eq1 == eq5

    ## point operations on curve 
    def add_points(self, P1,P2):
        R = point(0,0,inf=True)
        if e_math.are_points_equal(P1,P2) and P1.getX()!=0:
            # use point doubling
            R = self.point_doubling(P1,P2)
        elif not e_math.are_points_equal(P1,P2) and P1.getX() != P2.getX():
            #use normal addition
            R = self.simple_point_addition(P1,P2)
        return R

    def point_doubling(self, P1,P2):
        p = self.p
        a = self.a
        # calculate the slope 
        #s =  (3 * (X1^2) + a) / (2*Y1) 
        s_z = e_math.power(P1.getX(),2, p)    # X1^2
        s_z =  e_math.multiply(3, s_z, p)      # 3*(X1^2)
        s_z = e_math.add(s_z, a, p)            # 3 * (X1^2) + a

        s_n = e_math.multiply(2, P1.getY(), p) # 2*Y1
     
        s = e_math.multiply(s_z,e_math.inverse(s_n,p), p)         # (3*(X1^2)+a) / (2*Y1)

        # calculate the new x
        # x =  s^2 - 2*X1 
        x = e_math.subtract(e_math.power(s,2,p),            # S^2
                            e_math.multiply(2,P1.getX(),p), # (2*X1) 
                            p)

        # calculate new y
        # y = s*(x1-x)-Y1
        y = e_math.subtract(e_math.multiply(s, # s
                                             e_math.subtract(P1.getX(),x, p) # (X1 -x)
                                             , p),
                             P1.getY(), # Y1
                             p) 
        return point(x,y)



    def simple_point_addition(self, P1, P2 ):
        p = self.p
        # calculate the slope 
        #s =  (Y1- Y2) / (X1 - X2) 
        s_z = e_math.subtract(P1.getY(), P2.getY(), p) # Y1 - Y2 
        s_n = e_math.subtract(P1.getX(), P2.getX(), p) # X1 - X2
        s = e_math.multiply(s_z,e_math.inverse(s_n, p), p) # (Y1 - Y2) / (X1 - X2) 
        # calculate the new x
        # x =  s^2 - (X1+X2 ) 
        x = e_math.subtract(e_math.power(s, 2, p),               # s^2
                            e_math.add(P1.getX(), P2.getX(),p),  # (X1 + P2)
                            p)
        # calculate new y 
        # y = s*(X1 -X) - Y1 
        y = e_math.subtract(e_math.multiply(s,                                  #s 
                                            e_math.subtract(P1.getX(),x,p),     # (X1-X)
                                            p),
                            P1.getY(),                                          # Y1
                            p)
        return point(x,y)


    def multiply_point(self,P,x):
        T = P
        for i in range(0,x):
            T = self.add_points(T,P)
        return T

    ## Cryptic functions
    def generate_secret(self):
        self.K = secrets.choice(range(1,self.n))
        print(self.K)

    def calculate_public_point(self):
        secret_point = self.multiply_point(self.G, self.K-1)
        if not self.is_on_curve(secret_point):
            print("secret point error")
        self.public_Point = secret_point
        secret_point.pr()

    def calculate_shared_Point(self,P):
        shared_point = self.multiply_point(P, self.K-1)
        if not self.is_on_curve(shared_point):
            print("secret point error")
        self.shared_Point = shared_point
        shared_point.pr()

    def calculate_cyclic_group(self):
        n = 1 
        group = [self.G]
        while(not group[n-1].is_infinte()):
            group[n-1].pr()
            P = self.add_points(self.G,group[n-1])
            group.append(P)
            P.pr()
            n+=1
        self.n = n
        self.cyclic_group = group


    ## getter 
    def calculate_cofactor():
        pass 

    def get_order(self):
        return self.n
    

    
