class Punto:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y

    def __str__(self):
        return f"( {self.x}, {self.y})"

    def cuadrante(self):
        if self.x != 0 and self.y != 0:
            if self.x>0:
                if self.y > 0:
                    print("Se encuentra en el primer cuadrante.")
                elif self.y < 0:
                    print("Se encuentra en el cuarto cuadrante.")
            elif self.x < 0:
                if self.y > 0:
                    print("Se encuentra en el segundo cuadrante.")
                elif self.y < 0:
                    print("Se encuentra en el tercer cuadrante.")          
        elif self.x == 0 and self.y != 0:
            print("Se encuentra sobre el eje x.")      
        elif self.x != 0 and self.y == 0:
            print("Se encuentra sobre el eje y.")
        else:
            print("Se encuentra en el origen.")  
    
    def vector(self,x2,y2):
        componente_i=self.x + x2
        componente_j=self.y + y2
        print(f"{componente_i}i + {componente_j}j")
        
A=Punto(3,2)
print(A)
A.cuadrante()
A.vector(4,6)