import numpy as np

from manim import *


class ConvexPlot(Scene):
    def construct(self):
        self.set_axes()
        self.add_convex_graph()
        self.add_lines()
        self.add_x_labels()
    
    def set_axes(self):
        self.axes = Axes(
            x_range=[0, 20],
            y_range=[0, 25],
            axis_config={"tick_size": 0},
            x_axis_config={"label_direction": RIGHT},
            tips=False,
        )
        labels = self.axes.get_axis_labels(x_label="weight", y_label="Loss")
        self.add(self.axes, labels)
    
    def add_convex_graph(self):
        # convex function (gradient descent converges to the minimum point)
        def convex_func(x): 
            return pow((0.7*x-7), 2)+3
        self.convex_graph = self.axes.plot(convex_func, color=RED, x_range=[4, 16])
        self.add(self.convex_graph)
    
    def add_lines(self):
        # minimum point of the convex function
        self.minimum_line = self.axes.get_vertical_line(self.axes.input_to_graph_point(10, self.convex_graph), color=RED)
        self.add(self.minimum_line)
    
    def add_x_labels(self):
        x_labels = [MathTex("minimum")]

        for i in range(len(x_labels)):
            x_labels[i].next_to(self.minimum_line, DOWN)  # x point of x_label
            self.add(x_labels[i])


