class Personaje: 
    
    #constructor  de la clase personaje
    def __init__(self, nombre):
        self.nombre = nombre
        self.nivel = 1
        self.exp = 0 
        
    @property
    #Metodo que muestra  el nombre del personaje y su nivel
    #Getter para obtejer  la información
    def estado (self):    
        return  f"Soy {self.nombre}, y el nivel es {self.nivel}, Exp {self.exp}"

    #Setter es para modificar dicha información
    @estado.setter 
    def estado (self, exp):
        Nexp = self.exp + exp
         
         #Mientras la experiencia  sea mayor o igual a 100, el personaje sube un nivel 
        while Nexp >= 100:
            self.nivel += 1
            Nexp -= 100 
            
         #Mientras la nueva experiencia sea 0, y el nivel sube en uno , descuenta si pierdes   
        while  Nexp < 0: 
                if self.nivel > 0: 
                    Nexp += 100
                    self.nivel -= 1
                else: 
                    Nexp = 0
                self.exp = Nexp
    
    # Metodos para realizar comparaciones enriquecidas entre objeto.             
    def __lt__(self , other):  
        return  self.nivel < other.nivel 
                
    def __gt__(self , other): 
        return self.nivel > other.nivel 
    
    #Metodo para calcular la probabilidad de ganar
    def probabilidad_ganar(self, other): 
        if self > other :
            return 0.33
        elif self < other: 
            return 0.66
        else: 
            return  0.5
        
        
    #Metodo que mostrará el dialogo del enfrentamiento    
    @staticmethod
    def mostrar_dialogo(probabilidad):
        return float(input(f"""Con tu nivel actual, tienes {probabilidad} de ganarle al orco.\n 
                      Si ganas, ganarás 50 pts de experiencia y el orco perderá 30 puntos de experiencia\n
                      Si pierdes, perderás 30 pts de experiencia y el orco ganará 50 pts  de experiencia\n
                      1. Atacar\n
                      2. Correr
                     """))
    