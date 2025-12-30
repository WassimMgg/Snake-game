from turtle import Turtle
MOVE_DISTANCE = 20

class Snake:
    def __init__(self):
        self.positions = [(0, 0), (-20, 0), (-40, 0)]
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        
    def create_snake(self):
        for item in self.positions:
            t = Turtle("square")
            t.color("white")
            t.penup()
            t.goto(item)
            self.segments.append(t)
        
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
        
    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
 
    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
    
    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def extend_tail(self):
        tail_tall = len(self.segments) - 1
        tail_x_positions = self.segments[tail_tall].xcor()
        tail_y_positions = self.segments[tail_tall].ycor()
        new_segment  = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        if self.segments[tail_tall].heading() == 180:
            new_segment.goto(x = tail_x_positions + 20, y = tail_y_positions)
        elif self.segments[tail_tall].heading() == 0:
            new_segment.goto(x = tail_x_positions - 20, y = tail_y_positions)
        elif self.segments[tail_tall].heading() == 270:
            new_segment.goto(x = tail_x_positions, y = tail_y_positions + 20)
        else:
            new_segment.goto(x = tail_x_positions, y = tail_y_positions - 20)
        self.segments.append(new_segment)

