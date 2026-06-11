from manim import *


class EquationHelper:

    @staticmethod
    def animate_equation(
        scene,
        parts,
        color=None,
        font_size=None,
        reference=None,
        side=DOWN,
        buff=0.8,
        part_lag=None,
        equal_lag=None,
        animation=Write,
        **kwargs
    ):
        """
        Parameters:
            scene       : Manim scene.
            parts       : List of MathTex strings.
            color       : Equation color.
            font_size   : MathTex font size.
            reference   : Object to position relative to.
            side        : UP, DOWN, LEFT, RIGHT.
            buff        : Distance from reference.
            part_lag    : Pause after each part.
            equal_lag   : Pause after "=".
            animation   : Write, FadeIn, Create or Add.

        Behavior:
            - No lags -> displays whole equation at once.
            - part_lag only -> pauses after every part.
            - part_lag + equal_lag -> custom pause after "=".
            - equal_lag only -> pauses only after "=".
        """

        tex_kwargs = dict(kwargs)

        if font_size is not None:
            tex_kwargs["font_size"] = font_size

        if color is not None:
            tex_kwargs["color"] = color

        equation = MathTex(*parts, **tex_kwargs)

        if reference is not None:
            equation.next_to(reference, side, buff=buff)

        # Helper for displaying one object
        def show(obj):
            if animation == Add:
                scene.add(obj)
            else:
                scene.play(animation(obj))

        # No lag -> display everything together
        if part_lag is None and equal_lag is None:
            show(equation)
            return equation

        # If only part_lag is given, use it for "=" too
        if part_lag is not None and equal_lag is None:
            equal_lag = part_lag

        # Display piece by piece
        for i, part in enumerate(parts):

            show(equation[i])

            if i == len(parts) - 1:
                continue

            if part == "=":
                if equal_lag is not None:
                    scene.wait(equal_lag)
            else:
                if part_lag is not None:
                    scene.wait(part_lag)

        return equation
    


    # @staticmethod
    # def build_from_parts(
    #     scene,
    #     sources,
    #     reference=None,
    #     side=DOWN,
    #     buff=0.8,
    #     font_size=48,
    #     color=None,
    #     box_color=YELLOW,
    #     box_buff=0.15,
    #     copy_buff=0.2,
    #     copy_animation=TransformFromCopy,
    #     new_animation=Write,
    #     part_lag=None,
    #     equal_lag=None,
    #     animate_boxes=True,
    # ):

    #     """
    #     sources examples:

    #     ("copy", equation, 2)

    #     ("new", "=")

    #     ("new", "9 \\times 5")

    #     ("new", MathTex("3^2"))
    #     """

    #     # -----------------------------
    #     # Build destination objects
    #     # -----------------------------

    #     dest_parts = []
    #     actions = []

    #     for item in sources:

    #         mode = item[0]

    #         # -----------------
    #         # COPY
    #         # -----------------

    #         if mode == "copy":

    #             mob = item[1]
    #             idx = item[2]

    #             src = mob[idx]
    #             dst = src.copy()

    #             dest_parts.append(dst)

    #             actions.append({
    #                 "type": "copy",
    #                 "src": src,
    #                 "dst": dst,
    #                 "text": getattr(src, "tex_string", "")
    #             })

    #         # -----------------
    #         # NEW
    #         # -----------------

    #         elif mode == "new":

    #             value = item[1]

    #             if isinstance(value, str):

    #                 kwargs = {}

    #                 if font_size is not None:
    #                     kwargs["font_size"] = font_size

    #                 if color is not None:
    #                     kwargs["color"] = color

    #                 dst = MathTex(value, **kwargs)

    #                 text = value

    #             else:

    #                 dst = value

    #                 text = getattr(dst, "tex_string", "")

    #             dest_parts.append(dst)

    #             actions.append({
    #                 "type": "new",
    #                 "dst": dst,
    #                 "text": text
    #             })

    #     # -----------------------------
    #     # Layout
    #     # -----------------------------

    #     new_eq = VGroup(*dest_parts)
    #     new_eq.arrange(RIGHT, buff=copy_buff)

    #     if reference is not None:
    #         new_eq.next_to(reference, side, buff=buff)

    #     # Save final positions

    #     final_positions = [p.get_center() for p in dest_parts]

    #     # Hide everything

    #     for p in dest_parts:
    #         p.set_opacity(0)

    #     scene.add(new_eq)

    #     # -----------------------------
    #     # Animate
    #     # -----------------------------

    #     for i, action in enumerate(actions):

    #         dst = action["dst"]

    #         dst.set_opacity(1)

    #         if action["type"] == "copy":

    #             src = action["src"]

    #             if animate_boxes:

    #                 box = SurroundingRectangle(
    #                     src,
    #                     color=box_color,
    #                     buff=box_buff
    #                 )

    #                 scene.play(Create(box))

    #             scene.play(copy_animation(src, dst))

    #             if animate_boxes:
    #                 scene.play(FadeOut(box))

    #         else:

    #             scene.play(new_animation(dst))

    #         # -------------------------
    #         # Wait
    #         # -------------------------

    #         if i != len(actions) - 1:

    #             wait_time = part_lag

    #             if action["text"].strip() == "=" and equal_lag is not None:
    #                 wait_time = equal_lag

    #             if wait_time is not None:
    #                 scene.wait(wait_time)

    #     return new_eq
    
    @staticmethod
    def build_from_parts(
        scene,
        sources,
        reference=None,
        side=DOWN,
        buff=0.8,
        font_size=48,
        color=None,
        copy_scale=1.0,
        box_color=YELLOW,
        box_buff=0.15,
        part_buff=0.2,
        copy_animation=TransformFromCopy,
        new_animation=Write,
        part_lag=None,
        equal_lag=None,
        animate_boxes=True,
    ):
    
        # -----------------------------
        # Build destination objects
        # -----------------------------
    
        parts = []
        actions = []
    
        for item in sources:
        
            mode = item[0]
    
            # -------------------------
            # COPY
            # -------------------------
    
            if mode == "copy":
            
                mob = item[1]
                idx = item[2]
    
                src = mob[idx]
                dst = src.copy()
    
                # Apply target color
                if color is not None:
                    dst.set_color(color)
    
                # Apply target scale
                if copy_scale != 1:
                    dst.scale(copy_scale)
    
                parts.append(dst)
    
                actions.append({
                    "type": "copy",
                    "src": src,
                    "dst": dst,
                    "text": getattr(src, "tex_string", ""),
                })
    
            # -------------------------
            # NEW
            # -------------------------
    
            elif mode == "new":
            
                value = item[1]
    
                if isinstance(value, str):
                
                    kwargs = {}
    
                    if font_size is not None:
                        kwargs["font_size"] = font_size
    
                    if color is not None:
                        kwargs["color"] = color
    
                    dst = MathTex(value, **kwargs)
    
                else:
                
                    dst = value
    
                    if color is not None:
                        dst.set_color(color)
    
                parts.append(dst)
    
                actions.append({
                    "type": "new",
                    "dst": dst,
                    "text": getattr(dst, "tex_string", ""),
                })
    
            else:
            
                raise ValueError(f"Unknown mode: {mode}")
    
        # -----------------------------
        # Compute final layout
        # -----------------------------
    
        layout = VGroup(*parts)
        layout.arrange(RIGHT, buff=part_buff)
    
        if reference is not None:
            layout.next_to(reference, side, buff=buff)
    
        final_positions = [m.get_center() for m in parts]
    
        built_parts = []
    
        # -----------------------------
        # Animate
        # -----------------------------
    
        for i, action in enumerate(actions):
        
            dst = action["dst"]
    
            # Put destination at its final location
            dst.move_to(final_positions[i])
    
            if action["type"] == "copy":
            
                src = action["src"]
    
                if animate_boxes:
                
                    box = SurroundingRectangle(
                        src,
                        color=box_color,
                        buff=box_buff,
                    )
    
                    scene.play(Create(box))
    
                # Color/scale interpolate automatically
                scene.play(copy_animation(src, dst))
    
                if animate_boxes:
                    scene.play(FadeOut(box))
    
            else:
            
                scene.play(new_animation(dst))
    
            built_parts.append(dst)
    
            # Optional pause
    
            if i != len(actions) - 1:
            
                wait_time = part_lag
    
                if (
                    action["text"].strip() == "="
                    and equal_lag is not None
                ):
                    wait_time = equal_lag
    
                if wait_time is not None:
                    scene.wait(wait_time)
    
        # -----------------------------
        # Return finished equation
        # -----------------------------
    
        return VGroup(*built_parts)