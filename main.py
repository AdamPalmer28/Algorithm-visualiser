import numpy as np
import pygame as pg

from num_draw import *
import time

class SoftwareRender:

    def __init__(self):

        self.res  =  self.width,  self.height  =  1760,  990 
        self.FPS = 60
        self.screen = pg.display.set_mode( self.res )
        self.clock = pg.time.Clock()

        self.n = 220 # number of numbers to sort
        assert self.width % self.n == 0, "Resolution doesn't divide by list size"
        self.block_width = self.width / self.n

        self.method = 0 # 0 - bubble
        self.numbers = number_handler(self, self.n, self.method) # handles numbers and sorting

        
        
        

    def draw(self, ind):
        """collective draw function"""

        self.screen.fill(pg.Color('white')) # background

        # draw list (of numbers) 
        self.numbers.draw()

        # draw "checking" line
        pg.draw.rect(self.screen, 'green', (ind * self.block_width, 0, self.block_width, self.height))



    def run(self):
        
        start_time = time.time()
        sorted = False
        while True:
            pg.display.set_caption( str( self.clock.get_fps() ) ) # display fps in window name
            #pg.display.flip() # update screen
            self.clock.tick(self.FPS)          
            
            
            if not sorted:
                temp_sorted = True
                for ind in range(self.n - 1):

                    if self.numbers.list.sort_iteration(ind):
                        temp_sorted = False

                    self.draw(ind)
                    pg.display.update()#.flip() # update screen

                if temp_sorted:
                    sorted = True # breaks loop if sorted

                    end_time = time.time()
                    time_taken = np.round(end_time - start_time, 2)
                    
                    time_taken_str = f"Finished in {time_taken} seconds"
                    print(time_taken_str)


            for event in pg.event.get():
                if event.type == pg.KEYDOWN:

                    if event.key == pg.K_r:
                        # restart sorting algorithm
                        self.numbers = number_handler(self, self.n, self.method) # handles numbers and sorting
                        start_time = time.time()
                        sorted = False

                elif event.type == pg.QUIT: 
                    # exit function
                    exit()


if __name__ == '__main__':
    render = SoftwareRender()
    render.run()
