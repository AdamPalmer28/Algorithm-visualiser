from tkinter import N
import numpy as np
import pygame as pg

from list_sort import *

class number_handler:

    def __init__(self, render, n, method = 0):

        self.render = render 
        self.screen_width = self.render.width

        self.n = n # size of list
        self.list = list_sorter( self.n, method = 0) # intialise list sorter

        self.block_width = self.render.block_width # rect width
        self.unit_height = (self.render.height / self.n) # rect height per 1 value

        self.rect_colour = "lightgrey" 



        pg.font.init() # init font
            
        # if self.n < 100:
        #     fontsize = 12
        # elif ((self.n >= 100) & (self.n < 200)):
        #     fontsize = 10
        # else:
        #     fontsize = 8
        # self.num_font = pg.font.SysFont('Arial', fontsize)

        # self.font_y = (self.render.height - 20) # y cord of values
        

    def draw(self):
        "Draw all list elements"
        for ind, i in enumerate(self.list.values):
            self.draw_rect(ind, i)



    def draw_rect(self, ind, value):
        """
        Draws individual rectangle
        ind - index in list, is used for position on screen
        value - value of list item, is used for height
        """
        x_1, w = ind * self.block_width, self.block_width    # postion start of rect
        
        rect_height = int(value * self.unit_height)
        y_1, h = self.render.height - rect_height, rect_height 

        #(left, top, width, height)
        pg.draw.rect(self.render.screen, self.rect_colour, (x_1, y_1, w, h))

        # draw text/font of values

        # text_surface = self.num_font.render(str(value), False, (0, 0, 0))
        # self.render.screen.blit(text_surface, (x_1 + w/4, self.font_y))
        





