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
