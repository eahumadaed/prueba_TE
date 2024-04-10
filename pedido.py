
from te import Te

def format_precio(precio):
    return "{:,}".format(precio).replace(',', '.')


def main():
    print("Bienvenido a la hora del té de Alicia en el País de las Maravillas.")
    print("Donde cada taza de té viene con una historia y una pizca de magia.")
    print("Por favor, ingrese el número correspondiente al sabor del té:")
    print("1: Té negro\n2: Té verde\n3: Infusión de hierbas")
    sabor = int(input("Sabor: "))

    print("\nIngrese el formato del té en gramos (300 o 500):")
    formato = int(input("Formato: "))

    tiempo, recomendacion = Te.sabor(sabor)
    precio = Te.formato(formato)

    sabores_texto = {1: 'Té negro', 2: 'Té verde', 3: 'Infusión de hierbas'}
    print(f"\nDetalle del pedido:")
    print(f"Sabor del té: {sabores_texto[sabor]}")
    print(f"Formato: {formato} gr")
    print(f"Precio: ${format_precio(precio)}")
    print(f"Tiempo de preparación: {tiempo} minutos")
    print(f"Recomendación: Beber {recomendacion}")

    print("\n¡Tu pedido está casi listo! Mientras esperas, ¿por qué no te sientas en nuestra mesa virtual y disfrutas de una charla con el Sombrerero Loco y la Liebre? Recuerda, en la hora del té de Alicia, el tiempo se detiene y cada sorbo es una aventura.")

if __name__ == "__main__":
    main()