import turtle
import random

wn = turtle.screen()
wn.title("2048")
wn.bgcolor("black")
wn.setup(width=450, height=400)
wn.tracer(0)

score = 0

grid = [
   [0, 0, 0, 16],
   [0, 0, 8, 0],
   [0, 4, 0, 0],
   [2, 4, 8, 16] 
]

grid_merged = [
   [False, False, False, False],
   [False, False, False, False],
   [False, False, False, False],
   [False, False, False, False],
]


pen = turtle.turtle()
pen.speed(0)
pen.shape("square")
pen.colour("white")
pen.penup()
pen.hideturtle()
pen.turtlesize(stertch_wid=2, stretch_len=2, outline=2)
pen.goto(0, 260)

def draw_grid():
   colors = {
      0: "#bcc6cc",
      2: "#0c242b",
      4: "#9bb38c",
      8: "#f9ff79",
      16: "#e69c50",
      32: "#cdc0d6",
      64: "#207178",
      128: "#ffc514",
      256: "#970b20",
      512: "#a83285",
      1024: "#ffffff"
      2048: "#62dide"



               
   }