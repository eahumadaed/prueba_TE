from te import Te

te_1 = Te()
te_2 = Te()

#Se imprimen los tipos
tipo_1 = type(te_1)
tipo_2 = type(te_2)

print(tipo_1)
print(tipo_2)


#Comparativa
if tipo_1 == tipo_2:
    print("Ambos objetos son del mismo tipo")
else:
    print("Los objetos no son del mismo tipo")
    
    

# print(te_1.sabor(1))
# #te_2.sabor(2)
# print(te_2.sabor(2))
# print(te_1.formato(300))
# print(te_2.formato(500))