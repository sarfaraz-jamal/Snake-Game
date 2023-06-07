from turtle import Turtle

POSITIONS = [(0,0),(-20,0),(-40,0)]
DISTANCE = 20

class Snake:

    def __init__(self):
        self.segments = []
        self.create_body()

    def create_body(self):

       for coordinate in POSITIONS:
            self.create_segment(coordinate)
    

    def create_segment(self, position):
            new_segment = Turtle()
            new_segment.shape("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.setposition(position)    
            self.segments.append(new_segment)


    def extend_body(self):
        position = self.segments[-1].position()
        self.create_segment(position)

    def move(self):
        
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.segments[0].forward(DISTANCE)
       
    def up(self):
        if self.segments[0].heading() == 0 or self.segments[0].heading() == 180:
            self.segments[0].setheading(90)
        else:
            pass
    
    def down(self):
        if self.segments[0].heading() == 0 or self.segments[0].heading() == 180:
            self.segments[0].setheading(270)
        else:
            pass

    def right(self):
        if self.segments[0].heading() == 90 or self.segments[0].heading() == 270:
            self.segments[0].setheading(0)
        else:
            pass
    
        
    def left(self):
        if self.segments[0].heading() == 90 or self.segments[0].heading() == 270:
            self.segments[0].setheading(180)
        else:
            pass



