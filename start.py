from manim import *
from os import system
import numpy as np


class ArrayScene(Scene):

    def construct(self):
        # Create the array
        self.camera.frame_width = 40
        self.camera.frame_height = 40 * 9 / 16
        h, w = 6, 6
        array = VGroup(*[Text("a" for i in range(h * w))])
        array.arrange_in_grid(h, w, 0.5)
        self.add(array)

        index_str = ["i=", "j=", "k=", "l="]
        groups = VGroup()
        for index in range(4):
            text = Text(index_str[index])
            number = Integer(0).next_to(text)
            groups.add(VGroup(text, number))
        groups.arrange_in_grid(1, 4, buff=0.5)
        groups.next_to(array, UP)
        groups.shift(UP * 2.5)
        self.add(groups)
        rect = Rectangle(YELLOW,
                         width=array[0].width * 3,
                         height=array[0].width * 3)
        rect.move_to(array[2 * w + 2].get_center())
        self.add(rect)
        xdis = array[1].get_center() - array[0].get_center()
        ydis = array[1 * w].get_center() - array[0].get_center()

        if_branch = Text("for each pixel:\n\
        1. row branch\n\
        2. col branch\n\
        3. index branch\n\
        4. radius branch\n").next_to(groups, LEFT)
        if_branch.shift(2.5 * LEFT)
        self.add(if_branch)

        for row in range(2, 3):
            for col in range(2, 3):
                self.play(array.animate.set_color(WHITE), run_time=0.1)
                current_index = row * w + col
                self.play(array[current_index].animate.set_color(GREEN))
                for j in range(-2, 3):
                    for spread_col in range(-2, 3):
                        if (j == -2 or j == 2) and (spread_col != 0):
                            continue
                        if (j == -1 or j == 1) and (spread_col
                                                    not in [-1, 0, 1]):
                            continue
                        self.play(groups[0][1].animate.set_value(row),
                                  groups[1][1].animate.set_value(col),
                                  groups[2][1].animate.set_value(j),
                                  groups[3][1].animate.set_value(spread_col),
                                  run_time=0.2)
                        self.play(rect.animate.move_to(
                            array[current_index].get_center() + j * ydis +
                            spread_col * xdis),
                                  run_time=0.5)
                        if ((row + j) >= 0 and (row + j) < h):
                            index = (row + j) * 6 + col + spread_col

                            if (col + spread_col) < 0 or (col +
                                                          spread_col) >= w:
                                continue
                            self.play(array[index].animate.set_color(YELLOW),
                                      run_time=0.2)


class MultiC(Scene):
    def construct(self):
        # Create the array
        self.camera.frame_width = 40
        self.camera.frame_height = 40 * 9 / 16
        h, w = 8, 8
        array = VGroup(*[Text((str(i))) for i in range(h * w)])
        array.arrange_in_grid(h, w, 0.5)
        self.add(array)

        xdis = array[1].get_center() - array[0].get_center()
        ydis = array[1 * w].get_center() - array[0].get_center()

        rect_a = Rectangle(RED,
                           width=array[0].width * 2,
                           height=array[0].width * 2)
        rect_b = Rectangle(GREEN,
                           width=array[0].width * 2,
                           height=array[0].width * 2)
        rect_c = Rectangle(YELLOW,
                           width=array[0].width * 2,
                           height=array[0].width * 2)
        array_a_center = array[2].get_center()
        array_b_center = array[1 * w + 3].get_center()
        array_c_center = array[1 * w + 4].get_center()
        rect_a.move_to(array[2 * w + 2].get_center())
        rect_b.move_to(array[2 * w + 3].get_center())
        rect_c.move_to(array[2 * w + 4].get_center())
        self.add(rect_a)
        self.add(rect_b)
        self.add(rect_c)
        self.wait()
        array_a = array[2 * w + 2].copy()
        array_b = array[2 * w + 3].copy()
        array_c = array[2 * w + 4].copy()
        self.play(array_a.animate.move_to(RIGHT * 10 + UP))
        self.play(array_b.animate.move_to(RIGHT * 10))
        self.play(array_c.animate.move_to(RIGHT * 10 + DOWN))
        arrow_a = Arrow(start=LEFT, end=RIGHT).next_to(array_a, RIGHT)
        arrow_b = Arrow(start=LEFT, end=RIGHT).next_to(array_b, RIGHT)
        arrow_c = Arrow(start=LEFT, end=RIGHT).next_to(array_c, RIGHT)
        lut = Text("LUT").next_to(arrow_a, UP)
        self.play(Create(arrow_a), Create(arrow_b), Create(arrow_c),
                  Create(lut))
        address_a = Text("address_a").next_to(arrow_a, RIGHT)
        address_b = Text("address_b").next_to(arrow_b, RIGHT)
        address_c = Text("address_c").next_to(arrow_c, RIGHT)
        self.play(Create(address_a), Create(address_b), Create(address_c))

        add_array = VGroup(*[Text("a") for i in range(h * w)])
        add_array.arrange_in_grid(h, w, 0.5)
        add_array.next_to(address_c, DOWN * 5)
        add_axis=add_array[1].get_center()-add_array[0].get_center()
        self.play(Create(add_array))
        self.play(
            address_a.copy().animate.next_to(add_array[7 * w], LEFT),
            address_b.copy().animate.next_to(add_array[4 * w], LEFT),
            address_c.copy().animate.next_to(add_array[6 * w], LEFT),
        )

        rect_add_a = Rectangle(RED,
                               width=array[0].width * 2,
                               height=array[0].width * 2).move_to(add_array[7*w].get_center())
        rect_add_b = Rectangle(GREEN,
                               width=array[0].width * 2,
                               height=array[0].width * 2).move_to(add_array[4*w].get_center())
        rect_add_c = Rectangle(YELLOW,
                               width=array[0].width * 2,
                               height=array[0].width * 2).move_to(add_array[6*w].get_center())
        self.play(Create(rect_add_a),Create(rect_add_b),Create(rect_add_c),)
        self.play(rect_add_a.animate.shift(2*add_axis),rect_add_b.animate.shift(4*add_axis),rect_add_c.animate.shift(4*add_axis),)

        self.play(Create(Text("Memory Repack").next_to(add_array,DOWN*2)))
        array_a_center = array[2].get_center()
        array_b_center = array[1 * w + 3].get_center()
        array_c_center = array[1 * w + 4].get_center()

        polygram_a = Polygon(array_a_center,
                             array_a_center + (2) * ydis + (-2) * xdis,
                             array_a_center + (4) * ydis,
                             array_a_center + (2) * ydis + 2 * xdis,
                             color=RED_B)
        self.add(polygram_a)
        polygram_b = Polygon(array_b_center,
                             array_b_center + (1) * ydis + (-1) * xdis,
                             array_b_center + (2) * ydis,
                             array_b_center + (1) * ydis + 1 * xdis,
                             color=GREEN_B)
        self.add(polygram_b)
        polygram_c = Polygon(array_c_center,
                             array_c_center + (1) * ydis + (-1) * xdis,
                             array_c_center + (2) * ydis,
                             array_c_center + (1) * ydis + 1 * xdis,
                             color=YELLOW_B)
        self.add(polygram_c)
        self.play(Create(polygram_a), Create(polygram_b), Create(polygram_c))
        self.play(polygram_a.animate.set_fill(RED_B, opacity=0.5),
                  polygram_b.animate.set_fill(GREEN_B, opacity=0.5),
                  polygram_c.animate.set_fill(YELLOW_B, opacity=0.5))
        # bool align so can run together

        array_vec_top=Text("b").next_to(array[0],LEFT*20)
        array_vec=VGroup(array_vec_top)
        array_vec.add(Text("b").next_to(array_vec_top,DOWN+LEFT))
        array_vec.add(Text("b").next_to(array_vec_top,DOWN))
        array_vec.add(Text("b").next_to(array_vec_top,DOWN+RIGHT))
        array_vec.add(Text("b").next_to(array_vec_top,DOWN*3))
        self.play(Create(array_vec))
        rec_vec = VGroup(*[Rectangle(color=PURPLE,width=array[0].width*2,height=array[0].width*2) for i in range(5)])
        rec_vec.arrange_in_grid(1,5,0).move_to(array_vec[2].get_center()).shift(RIGHT*rec_vec[0].width*2)
        self.play(Create(rec_vec))
        for i in range(5):
            self.play(rec_vec.animate.move_to(array_vec[i].get_center()).shift(RIGHT*rec_vec[0].width*2),run_time=0.5)
        array_vec_in_ori=VGroup()
        for i in [2,3,4]:
            array_vec_in_ori.add(rect_add_a.copy().move_to(array[i].get_center()).set_fill(color=RED,opacity=1))
        self.play(Create(array_vec_in_ori))
        # for i in []



class VecC(Scene):
    def construct(self):
        # rotate arr_add
        # foreach pixel with a vector to loop
        pass

if __name__ == "__main__":
    system("manim start.py -pql MultiC")
