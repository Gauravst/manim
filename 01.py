from manim import *


class Main(Scene):
    def construct(self):

        name = Tex("Commit ", "Core")
        name[0].set_color(RED)

        name[1].set_color(BLUE)

        self.play(Write(name))
        self.wait(3)
