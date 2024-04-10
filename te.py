class Te:
    #Valores de los te
    valores = {300: 3000, 500: 5000}
    tipos = {
                1: ('Te negro',3,'Al desayuno'),
                2: ('Te Verde',5,'Al medio dia'),
                3: ('Infusión de hierbas',6,'Al atardecer')
                }
        
    #Metodos    
    @staticmethod
    def sabor(sabor):
        if sabor in Te.tipos:
            nombre_sabor, tiempo, recomendacion = Te.tipos[sabor]
            return tiempo, recomendacion
        else:
            return None, None
        
    @staticmethod
    def formato(formato):
        return Te.valores.get(formato, 0)
    
        