from tkinter import S
from turtle import Turtle
import random
import time


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    cars=[]
    def __init__(self):
        self.nums=random.randint(1,5)
        

    
    def car(self):
        rand_num=random.randint(1,6)
        if rand_num==1:
            car1=Turtle()
            car1.shapesize(1,2)
            car1.color(random.choice(COLORS))
            car1.pu()
            car1.shape('square')
            car1.goto(300,random.randint(-250,250))
            self.cars.append(car1)
    
    
    
    def move(self):
        for car in self.cars:
            car.backward(STARTING_MOVE_DISTANCE)
    def speed_up(self):
        global STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE+=MOVE_INCREMENT