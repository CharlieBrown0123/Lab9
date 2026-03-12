'''
Name: Charlie Brown
Project 3: Python Turtle Graphics Scene Refactoring

Project Description:
I refactored my Project 2 scene to be modular. 
I broke the main scene into helper functions for the sun, trees, and cabin. 
By adding parameters for position and scale, I was able to populate the scene 
with a second cabin and more trees for the enhanced version.

Specific Improvements:
1. Function Decomposition: made draw_cabin, draw_tree, and draw_sun.
2. Parameterization: replaced hardcoded coordinates with x and y variables.
3. Scaling: added a scale factor to functions to allow for different sizes.
4. Clean Logic: separated the environment setup from the object drawing.
'''

import turtle
import math

def setup_turtle():
    """Initialize turtle with standard settings"""
    t = turtle.Turtle()
    t.speed(0) 
    screen = turtle.Screen()
    screen.title("Turtle Graphics Assignment")
    return t, screen

def draw_rectangle(t, width, height, fill_color=None):
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    if fill_color:
        t.end_fill()

def draw_square(t, size, fill_color=None):
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    for _ in range(4):
        t.forward(size)
        t.right(90)
    if fill_color:
        t.end_fill()

def draw_triangle(t, size, fill_color=None):
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    for _ in range(3):
        t.forward(size)
        t.left(120)
    if fill_color:
        t.end_fill()

def draw_circle(t, radius, fill_color=None):
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    t.circle(radius)
    if fill_color:
        t.end_fill()

def draw_curve(t, length, curve_factor, segments=10, fill_color=None):
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    segment_length = length / segments
    original_heading = t.heading()
    for i in range(segments):
        angle = curve_factor * math.sin(math.pi * i / segments)
        t.right(angle)
        t.forward(segment_length)
        t.left(angle) 
    t.setheading(original_heading)
    if fill_color:
        t.end_fill()

def jump_to(t, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()


def draw_environment(t): #refactored version
    """Set background color and ground"""
    screen = t.getscreen()
    screen.bgcolor("skyblue")
    
    # 1. Ground
    jump_to(t, -400, -50)
    draw_rectangle(t, 800, 350, "darkgreen")
    
    # 2. Curved Path (Curve Line) #my walkway
    jump_to(t, -400, -100)
    draw_curve(t, 800, 15, segments=20, fill_color="green")

def draw_sun(t, x, y, radius=40):
    """3. Sun #Bright sun"""
    jump_to(t, x, y)
    draw_circle(t, radius, "yellow")

def draw_tree(t, x, y, s=1.0):
    """4. Tree #perfect tree :)"""
    # Trunk
    jump_to(t, x, y)
    draw_rectangle(t, 20 * s, 50 * s, "brown")
    # Leaves
    jump_to(t, x - (40 * s), y) 
    draw_triangle(t, 100 * s, "forestgreen")

def draw_cabin(t, x, y, s=1.0):
    """Draws a cabin using logic from Project 2"""
    # 5. Cabin
    jump_to(t, x, y)
    draw_square(t, 120 * s, "orange") #i love orange
    
    # 6. Roof #made a roof for the cabin
    jump_to(t, x, y)
    draw_triangle(t, 120 * s, "maroon")
    
    # 7. Door #Door
    jump_to(t, x + (40 * s), y - (60 * s))
    # I searched up a different shade of brown for this
    draw_rectangle(t, 40 * s, 60 * s, "chocolate") 
    
    # 8. Window #house needs a window
    jump_to(t, x + (60 * s), y - (50 * s))
    draw_circle(t, 20 * s, "yellow") 
    
    # 9 Smaller window (going for the oregon logo)
    jump_to(t, x + (60 * s), y - (40 * s))
    draw_circle(t, 10 * s, "white")

#main drawing logic

def draw_scene(t):
    # Setup background
    draw_environment(t)
    
    #the code from the previous project
    draw_sun(t, 250, 150)
    draw_cabin(t, -150, -100)
    draw_tree(t, 100, -100)

    #the enhanced version code 
    draw_tree(t, 220, -120, s=0.7)
    draw_tree(t, -300, -80, s=1.2)
    draw_cabin(t, 100, -200, s=0.6) 

def main():
    t, screen = setup_turtle()
    draw_scene(t)
    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()