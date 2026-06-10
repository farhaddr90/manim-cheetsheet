from manim import *

class BraceExample(Scene):
    def construct(self):
        line = Line(LEFT * 2, RIGHT * 2)

        brace = Brace(line, DOWN)
        label = brace.get_text("Length")

        self.play(Create(line))
        self.play(GrowFromCenter(brace), Write(label))
        self.wait()
        
        
        

class BraceGroup(Scene):
    def construct(self):
        squares = VGroup(
            Square(),
            Square(),
            Square()
        ).arrange(RIGHT, buff=0.2)

        brace = Brace(squares, DOWN)
        text = brace.get_text("3 squares")

        self.add(squares)
        self.play(GrowFromCenter(brace), Write(text))
        self.wait()
        
        

class BraceLabelExample(Scene):
    def construct(self):
        line = Line(LEFT * 3, RIGHT * 3)

        brace_label = BraceLabel(line, "Width", brace_direction=DOWN)

        self.add(line)
        self.play(Create(brace_label))
        self.wait()