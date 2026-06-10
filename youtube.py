from manim import *
from helper import EquationHelper


class ExponentThumbnail(Scene):
    def construct(self):
        # Background
        self.camera.background_color = "#0B1026"

        # Main title
        title1 = Text(
            "LAWS OF",
            font_size=72,
            weight=BOLD,
            color=WHITE
        )

        title2 = Text(
            "EXPONENTS",
            font_size=90,
            weight=BOLD,
            color=YELLOW
        )

        title_group = VGroup(title1, title2).arrange(DOWN, buff=0.15)
        title_group.to_edge(LEFT, buff=0.6).shift(UP*1.2)

        # Main equation
        equation = MathTex(
            r"a^m",
            r"\times",
            r"a^n",
            r"=",
            r"a^{m+n}",
            font_size=90
        )

        equation[0].set_color(BLUE)
        equation[2].set_color(PINK)
        equation[4].set_color(GREEN)

        equation.next_to(title_group, DOWN, buff=0.8)
        equation.shift(LEFT*0.4)

        # Subtitle
        subtitle = Text(
            "Rules of Powers",
            font_size=36,
            color=WHITE
        )

        subtitle.next_to(equation, DOWN, buff=0.6)

        # Right-side rules
        rules = VGroup(
            MathTex(r"a^m\times a^n=a^{m+n}", font_size=42),
            MathTex(r"\frac{a^m}{a^n}=a^{m-n}", font_size=42),
            MathTex(r"(a^m)^n=a^{mn}", font_size=42),
            MathTex(r"(ab)^n=a^nb^n", font_size=42),
            MathTex(r"a^0=1, \quad (a \neq 0)", font_size=42),
            # MathTex(r"a^{-n}=\frac{1}{a^n}, \quad (a \neq 0)", font_size=42),
            # MathTex(r"\sqrt[n]{a}=a^{\frac{1}{n}}", font_size=42),
            MathTex(r"\sqrt[n]{a^m}=a^{\frac{m}{n}}", font_size=42),
            # MathTex(r"\frac{a^m}{b^m}=\left(\frac{a}{b}\right)^m", font_size=42),
            # MathTex(r"\left(\frac{a}{b}\right)^{-n}=\left(\frac{b}{a}\right)^n, \quad (a,b \neq 0)", font_size=42),
            # MathTex(r"\left(\frac{a}{b}\right)^n=\frac{a^n}{b^n}, \quad (a,b \neq 0)", font_size=42),
            MathTex(r"1^m=1^n=1", font_size=42)
        )

        rules.arrange(DOWN, aligned_edge=LEFT, buff=0.45)
        rules.to_edge(RIGHT, buff=0.6)

        for r in rules:
            box = SurroundingRectangle(
                r,
                corner_radius=0.12,
                buff=0.15,
                color=BLUE
            )
            self.add(box)

        # Decorative glow circles
        glow1 = Circle(radius=0.7, color=BLUE).set_opacity(0.15)
        glow1.shift(3*LEFT + 2.5*DOWN)

        glow2 = Circle(radius=0.9, color=GREEN).set_opacity(0.12)
        glow2.shift(5*RIGHT + 2*UP)

        self.add(glow1, glow2)

        # Add objects
        self.add(
            title_group,
            equation,
            subtitle,
            rules,
        )

        # Wait so last frame can be exported
        self.wait(1)
        
        
class Clip_1_1(Scene):
    def construct(self):
        
        # =========================
        # DECLARATIONS
        # =========================
        
        # Main equation        
        equation = EquationHelper.animate_equation(
            scene=self,
            parts=[
                "2^x \\times 3^y \\times 5^z",
                "=",
                "45"
            ],
            font_size=48
        ) 
        
        solve_this = EquationHelper.animate_equation(
            scene=self,
            parts = ["x+y+z=?"],
            font_size=48,
            color=YELLOW,
            reference=equation,
            side=DOWN,
            buff=0.8,
            animation=FadeIn
        )

        self.wait(2)
        self.play(equation.animate.to_edge(UP), FadeOut(solve_this))
        
        primes = EquationHelper.build_from_parts(
            scene=self,
            sources=[
                ("copy", equation, 2),
                ("new", "="),
                ("new", "9 \\times 5"),
                ("new", "="),
                ("new", "3^2 \\times 5^1"),
            ],
            reference=equation,
            side=DOWN,
            buff=0.8,
            font_size=48,
            color=YELLOW,
            part_lag=0.5,
            equal_lag=1.5,
        )
        
        simp_1 = EquationHelper.animate_equation(
            scene=self,
            parts=[
                "2^x \\times 3^y \\times 5^z",
                "=",
                "3^2 \\times 5^1"
            ],
            reference=primes,
            side=DOWN,
            buff=0.8,
            animation=Write,
            color=YELLOW,
            equal_lag=1.5
        )
        
        simp_2 = EquationHelper.animate_equation(
            scene=self,
            parts=[
                "2^x \\times 3^y \\times 5^z",
                "=",
                "1 \\times 3^2 \\times 5^1"
            ],
            color = YELLOW,
            font_size = 48,
            reference=simp_1,
            side = DOWN, 
            buff=0.8,
            animation=Write,
            equal_lag=1.5
        )
        
        simp_3 = EquationHelper.animate_equation(
            scene=self,
            color = YELLOW, 
            font_size = 48,
            reference=simp_2,
            side=DOWN,
            buff = 0.8,
            parts=[
                "2^x",
                "\\times",
                "3^y",
                "\\times",
                "5^z",
                "=",
                "2^0",
                "\\times",
                "3^2",
                "\\times",
                " 5^1"
            ],
            equal_lag=1.5
        )
        
        self.play(
            FadeOut(primes),
            FadeOut(simp_1),
            FadeOut(simp_2)
            # FadeOut(red_line),
        )
        self.wait()
        
        self.play(
            simp_3.animate.next_to(equation, DOWN, buff=0.8)
        )
        
        rect1 = VGroup(
            SurroundingRectangle(simp_3[0], color=RED, buff=0.15), 
            SurroundingRectangle(simp_3[6], color=RED, buff=0.15)
            )
        
        rect2 = VGroup(
            SurroundingRectangle(simp_3[2], color=RED, buff=0.15), 
            SurroundingRectangle(simp_3[8], color=RED, buff=0.15)
            )
                
        rect3 = VGroup(
            SurroundingRectangle(simp_3[4], color=RED, buff=0.15), 
            SurroundingRectangle(simp_3[10], color=RED, buff=0.15)
            )                  
        
        eq1 = MathTex(r"x", "=", "0", color=BLUE).shift(UP)
        eq2 = MathTex(r"y", "=", "2", color=GREEN).next_to(eq1, DOWN, buff=0.5)
        eq3 = MathTex(r"z", "=", "1", color=RED).next_to(eq2, DOWN, buff=0.5)

        self.play(Create(rect1))
        self.wait(1)
        self.play(Write(eq1))

        self.play(ReplacementTransform(rect1, rect2))
        self.wait(1)
        self.play(Write(eq2))

        self.play(ReplacementTransform(rect2, rect3))
        self.wait(1)
        self.play(Write(eq3))

        self.play(FadeOut(rect3))
        
        self.play(Create(SurroundingRectangle(equation[0])))
        
        

