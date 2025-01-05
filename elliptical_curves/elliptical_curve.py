import secrets

class point:
    def __init__(self,p_x,p_y,inf=0):
        self.x = p_x 
        self.y = p_y
        self.inf=inf

    def getX(self):
        return self.x 

    def getY(self):
        return self.y
    
    def is_infinte(self):
        return self.inf

    def pr(self):
        print(f"x:{self.getX()} y:{self.getY()}")


#definition of curve 
# y**2 = x**3 +A*x +B

class elliptical_curve:
    def  __init__(self, p_p, p_a, p_b, p_G, p_h):
        print("init elliptical_curve")
        self.p =p_p #modulo
        
        self.a = p_a #curve parameter
        self.b = p_b #curve parameter 
        
        self.G = p_G # Generator Point
        #self.n = p_n # order 
        self.h = p_h # cofactor

    def calculate_secret_point(self):
        self.public_Point = self.multiply_point(self.G, self.K-1)

    def calculate_shared_Point(self,P):
        self.shared_Point = self.multiply_point(P,self.K-1)


    def calculate_cyclic_group(self):
        n = 1 
        group = [self.G]
        while(not group[n-1].is_infinte()):
            P = self.add_points(self.G,group[n-1])
            group.append(P)
            n+=1
        self.n = n

    def generate_secret(self):
        self.K = secrets.choice(range(1,self.n))
        self.K = 9
        print(self.K)

    def calculate_cofactor():
        pass 

    def get_order(self):
        return self.n



    def is_on_curve(self, P):
        x = P.getX()
        y = P.getY()
        return y**2 == x**3 + self.a *x + self.b 

    def equal_points(self, P1, P2):
        if P1.getX() == P2.getX() and P1.getY() == P2.getY():
            return True 
        else:
            return False

        

    def add_points(self, P1,P2):
        x = 0 
        y = 0
        print(f"p2 to add :x = {P2.getX()}, y = {P2.getY()}")
        if self.equal_points(P1,P2):
            if P1.getX() != 0:
                # point doubling
                print("point double")
                s_z = (3 * ((P1.getX()**2 )% self.p) + self.a ) % self.p
                s_n = 2 * P1.getY() 
                s_n = pow(s_n, -1, self.p)
               
                input(s_n)
                s = (s_z * s_n) % self.p


                print(f"slope : {s}")
            
                x = ( ((s**2) % self.p) - 2 * P1.getX()) % self.p  
                y = ( s * (P1.getX() - x) - P1.getY()) % self.p
            else:
                return point(0,0,inf=True)
        else:
            if P1.getX() != P2.getX():
                #normal addition
                s_z = (P1.getY() - P2.getY()) % self.p 
                s_n =  P1.getX() - P2.getX()
                s_n = pow(s_n, -1, self.p)
                s = (s_z * s_n) % self.p

                x = ((s**2)%self.p -(P1.getX() + P2.getX())) % self.p
                y = ((s * (P1.getX() - x )) % self.p - P1.getY()) % self.p
            else:
                return point(0,0,inf=True)
        new_point = point(x,y)
        return new_point

    def multiply_point(self,P,x):
        P.pr()
        T = P
        for i in range(0,x):
            T = self.add_points(T,P)
        return T
