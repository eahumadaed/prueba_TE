class Te:
    def __init__(self):
        #Valores de los te
        self.valores = {300: 3000, 500: 5000}
        
    @staticmethod
    def sabor(sabor):
        #print(sabor)
        #sabores = {1:"Té negro",2:"Té verde",3:"Infusión de hierbas"}
        #Te.nombre = sabores[sabor]
        
        #return Te.nombre
        #vla = {1:"Se recomienda consumir al desayuno",2:"Se recomienda consumir al medio dia",3:"Se recomienda consumir al atardecer"}
        
        #return vla[sabor]
        if sabor == 1:
            return ("se recomienda consumir al desayuno")
        elif sabor == 2:
            return ("se recomienda consumir al medio dia")
        elif sabor == 3:
            return ("se recomienda consumir al atardecer")
        
    @staticmethod
    def formato(self,formato):
        #print(formato)
        #Te.valor = Te.valores[formato]
        return self.valores.get(formato,"Formato no disponible")
    
        