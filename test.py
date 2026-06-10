from manim import*
from helper import EquationHelper


class test(Scene):
    def construct(self):
        equ1 = EquationHelper.animate_equation(
            scene=self,
            parts=[
                "a^2",
                "\\times",
                "y^2",
                "=",
                "z^2 \\times d^2"
            ]
        )
        
        equ2 = EquationHelper.animate_equation(
            scene=self,
            parts=[
                "a^3 + z^3",
                "=",
                "\\sqrt(a+b)"
            ],
            reference=equ1,
            side=DOWN
        )

        EquationHelper.build_from_parts(
            scene=self,
            sources=[
                ("copy", equ1, 4),
                ("new", "="),
                ("new", "a \\times b"),
                ("new", "+"),
                ("copy", equ2, 2)
                ],
            reference=equ1,
            side=UP,
            buff=0.8,
            font_size=48,
            color=YELLOW,
            part_lag=0.5,
            equal_lag=1.5
        )
        