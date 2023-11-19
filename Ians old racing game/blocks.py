from turtle import Turtle
import random

SCROLL_FACTOR = 20

class Blocks:
    def __init__(self):
        self.blocks = []
        self.random_threshold = 10

    def make_block(self):
        block = Turtle()
        block.shape('circle')
        block.penup()
        block.color('white')
        x = random.randint(-170, 160)
        block.goto(x, 280)
        self.blocks.append(block)
    def scroll(self):
        # Move all existing blocks down
        for index in range(len(self.blocks)-1,0,-1):
            block = self.blocks[index]
            block.goto(block.xcor(), block.ycor() - SCROLL_FACTOR)
            # If the block has scrolled off the screen then remove it
            if block.ycor() < -200:
                block.hideturtle()
                del self.blocks[index]


        # Add a new line of blocks at the top
        if random.randint(0,100) < self.random_threshold:
            self.make_block()
            if random.randint(0, 100) < self.random_threshold:
                self.make_block()

        # Over time make the threshold a bit higher so that we get more and more blocks
        self.random_threshold *= 1.02

