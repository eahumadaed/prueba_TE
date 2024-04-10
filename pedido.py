
from te import Te

def format_precio(precio):
    return "{:,}".format(precio).replace(',', '.')

def imprimir_mensaje(mensaje): #al final no me gusto y se descarta.
    longitud = len(mensaje)
    print(f"\n{'*' * (longitud + 4)}")
    print(f"* {mensaje} *")
    print(f"{'*' * (longitud + 4)}\n")
    
    
def main():
    print("*******************************************")
    print("* Bienvenido a la hora del té de Alicia en el País de las Maravillas.")
    print("*   Donde cada taza de té viene con una historia y una pizca de magia.")
    print("*   Por favor, ingrese el número correspondiente al sabor del té:")
    print("*   1: Té negro\n*   2: Té verde\n*   3: Infusión de hierbas")
    print("*******************************************")
    sabor = int(input("Sabor: "))

    print("\nIngrese el formato del té en gramos (300 o 500):")
    formato = int(input("Formato: "))

    tiempo, recomendacion = Te.sabor(sabor)
    precio = Te.formato(formato)

    sabores_texto = {1: 'Té negro', 2: 'Té verde', 3: 'Infusión de hierbas'}
    detalles_pedido = f"""
    Detalle del pedido:
    Sabor del té: {sabores_texto[sabor]}
    Formato: {formato} gr
    Precio: ${format_precio(precio)}
    Tiempo de preparación: {tiempo} minutos
    Recomendación: Beber {recomendacion}
    """
    print(detalles_pedido)

    print("*******************************************")
    print("* ¡Tu pedido está casi listo!")
    print("* Mientras esperas, ¿por qué no te sientas en nuestra mesa virtual y disfrutas de una charla con el Sombrerero Loco y la Liebre?")
    print("* Recuerda, en la hora del té de Alicia, el tiempo se detiene y cada sorbo es una aventura.")
    print("*******************************************")
if __name__ == "__main__":
    main()