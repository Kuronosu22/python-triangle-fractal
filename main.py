from turtle import *
from random import random, choice
from math import sqrt

def CreateTriangle():
    # Using iteration for creating each vertex and line
    for vertex in vertices:
        if vertex == vertices[0]:
            penup()
            goto(vertex)
            pendown()
        goto(vertex)
    goto(0,200)

def CreateRandomDot():
    # Using linear interpolation, first defining the random factors and then getting the x and y coordinates inside the triangle
    r1 = random()
    r2 = random()

    u = 1 - sqrt(r1)
    v = sqrt(r1) * (1 - r2)
    w = sqrt(r1) * r2
    print(u,v,w)

    x = u * vertices[0][0] + v * vertices[1][0] + w * vertices[2][0]
    y = u * vertices[0][1] + v * vertices[1][1] + w * vertices[2][1]

    penup()
    goto(x,y)

def Fractal():
    pensize(4)
    while True:
        # Choosing a random vertex and creating a dot in the middle of the distance between it
        random_vertex = choice(vertices)
        distance_vertex = distance(random_vertex)
        seth(towards(random_vertex))
        forward(distance_vertex / 2)
        dot(3, "blue")

# Defining the verticies on the canva
vertices = [(0,200),(-250,-200),(250,-200)]

# Defining the brush size, hideness and speed
pensize(6)
hideturtle()
speed(0)

# Calling the functions
CreateTriangle()
CreateRandomDot()
Fractal()

mainloop()

    