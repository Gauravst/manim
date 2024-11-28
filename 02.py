from manim import *


class Main(Scene):
    def construct(self):

        title = Text("Bubble Sort", color=RED, font="Poppins")
        subTitle = Text(
            "DSA by Commit Core", color=GREEN, font="Poppins", font_size=25
        ).next_to(title, DOWN)

        # self.play(Write(title, rate_func=linear, run_time=2))
        # self.play(Write(subTitle, rate_func=linear, run_time=1))
        # self.wait()
        #
        # self.play(FadeOut(title), FadeOut(subTitle))

        numbers = [5, 2, 4, 9, 0]

        square_size = 0.8
        spacing = 1

        totalWidth = (len(numbers) - 1) * spacing

        startX = -totalWidth / 2

        squaresWithNumbers = []


        for i, num in enumerate(numbers):
            square = Square(side_length=square_size, color=GREEN)

            square.shift(RIGHT * (startX + i * spacing))

            number = Text(str(num), color=GREEN, font="Poppins", font_size=28)

            number.move_to(square.get_center())

            squareWithNumber = VGroup(square, number)
            squaresWithNumbers.append(squareWithNumber)



        original_position = squaresWithNumbers[0].get_center()
        original_border = Rectangle(
            width=square_size, height=square_size, color=YELLOW, stroke_width=4
        ).move_to(original_position)

        self.add(original_border)
        self.add(*squaresWithNumbers)



        comparison = Text(">", color=RED).scale(1).move_to(ORIGIN + UP * 1.5)



        self.wait(2)
        self.play(squaresWithNumbers[0].animate.move_to(ORIGIN + UP * 1.5 + LEFT * 1).set_color(RED))
        
        self.play(Write(comparison)) 
        self.play(squaresWithNumbers[1].animate.move_to(ORIGIN + UP * 1.5 + RIGHT * 1).set_color(RED))


        self.wait(2)


