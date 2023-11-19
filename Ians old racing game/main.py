from turtle import Screen
from blocks import Blocks
# from car import Car
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(400,600)
screen.title('Racing')
screen.tracer(0)

blocks = Blocks()
# car = Car()

screen.listen()
# screen.onkeypress(key="Left", fun=car.left)
# screen.onkeypress(key="Right", fun=car.right)

game_over = False
while not game_over:
    blocks.scroll()
    # if car.any_collisions(blocks.blocks):
    #   game_over = True
    screen.update()
    time.sleep(0.2)

screen.exitonclick()