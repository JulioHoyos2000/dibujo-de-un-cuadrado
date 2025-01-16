import turtle


class Cuadrado:
    def __init__(self, lado):
        self.lado = lado

    def dibujar(self):
        ventana = turtle.Screen()
        ventana.title("Dibujo de un Cuadrado")
        ventana.bgcolor("white")

        lapiz = turtle.Turtle()
        lapiz.pensize(3)
        lapiz.color("blue")

        # Dibujar el cuadrado
        for _ in range(4):
            lapiz.forward(self.lado)
            lapiz.left(90)

        # Finalizar
        ventana.mainloop()


# Ejemplo de uso
try:
    lado = int(input("Ingresa la longitud del lado del cuadrado: "))
    if lado <= 0:
        raise ValueError("La longitud del lado debe ser un número positivo.")

    cuadrado = Cuadrado(lado)
    cuadrado.dibujar()
except ValueError as e:
    print(e)
