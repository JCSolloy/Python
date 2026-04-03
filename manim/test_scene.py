from manim import *

# Todas las animaciones ocurren dentro de una clase que hereda de "Scene"
class TestScene(Scene):
    # El método "construct" es donde defines la secuencia de animaciones
    def construct(self):
        # 1. Crear los objetos (se llaman "Mobjects")
        circle = Circle()
        square = Square()

        # 2. Darles estilo y posición
        circle.set_fill(BLUE, opacity=0.5)  # Color azul, 50% de opacidad
        square.set_fill(RED, opacity=0.5)   # Color rojo, 50% de opacidad
        square.rotate(PI / 4)               # Rota el cuadrado 45 grados

        # 3. Definir la secuencia de animación
        self.play(Create(circle))   # Anima la aparición del círculo
        self.wait(1)                # Pausa de 1 segundo

        self.play(Transform(circle, square)) # Anima la transformación del círculo al cuadrado
        self.wait(1)

        self.play(FadeOut(square))  # Anima la desaparición del cuadrado
        self.wait(1)
