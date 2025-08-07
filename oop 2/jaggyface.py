import turtle

class SmilyFace:
   def __init__(self):
      self.turtle_screen=turtle.Screen()
      self.turtle_screen.bgcolor("lightblue")
      self.t=turtle.Turtle()
      self.t.speed(5)
      self.t.color("black","yellow")

   def draw_circle(self, x, y, radius):
      self.t.penup()
      self.t.goto(x,y-radius)
      self.t.pendown()
      self.t.begin_fill()
      self.t.circle(radius)
      self.t.end_fill()

   def draw_eye(self,x,y):
    self.draw_circle(x,y,10)



   def draw_mouth(self):
      self.t.penup()
      self.t.goto(-50,-20)
      self.t.pendown()
      self.t.setheading(-60)
      self.t.circle(50,120)


   def draw_face(self):
      self.draw_circle(0,0,100)
      self.draw_eye(-35,40)
      self.draw_eye(35,40)
      self.draw_mouth()

   def run(self):
      self.draw_face()
      turtle.done()

face=SmilyFace()
face.run()               
    






 




 
 
 





