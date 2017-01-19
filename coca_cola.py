'''
Author: Rich Thompson
Date: today
Class: ISTA 130
Section Leader: I'm the man

Description:
The program draws the name "COCA-COLA". 
'''

# all import statements here, for example:
import turtle  # this is only needed if you're using turtle graphics

# all function definitions here, we'll define functions soon
def draw_c(name)
    name.forward(25)
    name.backward(25)
    name.left(90)
    name.forward(25)
    name.right(90)
    name.forward(25)
    name.penup()
    name.right(90)
    name.forward(25)
    name.left(90)
    


#==========================================================
def main():
    '''
    Construct a turtle and use it write 'COCO-COLA'.
    '''
    # your code goes here, make sure it's indented one level
    
    # prepare the turtle - set its state and initial position
    az_turtle = turtle.Turtle()
    az_turtle.pensize(10)
    az_turtle.shape('turtle')
    az_turtle.penup()
    az_turtle.backward(200)
    az_turtle.pendown()
    az_turtle.pencolor('green')
    
    # draw a C
    
    
    az_turtle.forward(20)
    az_turtle.pendown()
    az_turtle.pencolor('red')
    
    # draw an O
    az_turtle.forward(25)
    az_turtle.backward(25)
    az_turtle.left(90)
    az_turtle.forward(25)
    az_turtle.right(90)
    az_turtle.forward(25)
    az_turtle.right(90)
    az_turtle.forward(25)
    az_turtle.left(90)
    
    az_turtle.penup()
    az_turtle.forward(20)
    az_turtle.pendown()
    az_turtle.pencolor('blue')
  
    # draw a C
    az_turtle.forward(25)
    az_turtle.backward(25)
    az_turtle.left(90)
    az_turtle.forward(25)
    az_turtle.right(90)
    az_turtle.forward(25)
    az_turtle.penup()
    az_turtle.right(90)
    az_turtle.forward(25)
    az_turtle.left(90)
    
    az_turtle.forward(20)
    az_turtle.pendown()
    az_turtle.pencolor('gold')
    
    # draw an A
    az_turtle.left(90)
    az_turtle.forward(25)
    az_turtle.right(90)
    az_turtle.forward(25)
    az_turtle.right(90)
    az_turtle.forward(25)
    az_turtle.backward(12.5)
    az_turtle.right(90)
    az_turtle.forward(25)
    az_turtle.backward(25)
    az_turtle.right(180)
    
    az_turtle.pencolor('magenta')
    
    # draw a hyphen
    az_turtle.penup()
    az_turtle.forward(20)
    az_turtle.pendown()
    az_turtle.forward(25)
    az_turtle.right(90)
    az_turtle.penup()
    az_turtle.forward(12.5)
    az_turtle.left(90)
    
    az_turtle.forward(20)
    az_turtle.pendown()
    az_turtle.pencolor('purple')

    # draw a C
    az_turtle.forward(25)
    az_turtle.backward(25)
    az_turtle.left(90)
    az_turtle.forward(25)
    az_turtle.right(90)
    az_turtle.forward(25)
    az_turtle.penup()
    az_turtle.right(90)
    az_turtle.forward(25)
    az_turtle.left(90)
    
    az_turtle.forward(20)
    az_turtle.pendown()
    az_turtle.pencolor('darkgoldenrod')
    
    # draw an O
    az_turtle.forward(25)
    az_turtle.backward(25)
    az_turtle.left(90)
    az_turtle.forward(25)
    az_turtle.right(90)
    az_turtle.forward(25)
    az_turtle.right(90)
    az_turtle.forward(25)
    az_turtle.left(90)
    
    az_turtle.penup()
    az_turtle.forward(20)
    az_turtle.pendown()
    az_turtle.pencolor('darkred')
    
    # draw an L
    az_turtle.left(90)
    az_turtle.forward(25)
    az_turtle.backward(25)
    az_turtle.right(90)
    az_turtle.forward(25)
   
    az_turtle.penup()
    az_turtle.forward(20)
    az_turtle.pendown()
    az_turtle.pencolor('darkgreen')
    
    # draw an A
    az_turtle.left(90)
    az_turtle.forward(25)
    az_turtle.right(90)
    az_turtle.forward(25)
    az_turtle.right(90)
    az_turtle.forward(25)
    az_turtle.backward(12.5)
    az_turtle.right(90)
    az_turtle.forward(25)
    az_turtle.backward(25)
    az_turtle.right(180)
    
    az_turtle.hideturtle()
    
    input('Press enter to end.')  # only needed if you're using turtle graphics

if __name__ == '__main__':
    main()
