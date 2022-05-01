from manim import *
import math


class StraighteningCircle(Scene):
    def construct(self):
        circle = Circle(radius=1.75, stroke_width=50).set_color_by_gradient(([GREEN, BLUE])).move_to(UP*1.5).rotate(90*DEGREES, Z_AXIS)
        line = Line(start = [-2*(math.pi), 0, 0], end = [2*math.pi, 0, 0], stroke_width=50, color=BLUE).move_to(DOWN*1.5)

        self.play(DrawBorderThenFill(circle))
        self.wait()
        self.play(ReplacementTransform(circle, line))
        self.wait()
