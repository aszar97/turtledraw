#Sprint 5 Turtle Draw
#Adela Zarzour
#CSPC-20000
#Credits: Eric Pogue, Dr. Ray Klump
#All rights reserved.



import turtle 

TEXTFILENAME = 'turtle-draw.txt'

TEXTFILENAME = input('File name: ') #Asks user for the file name
open(TEXTFILENAME, 'r')


print('TurtleDrawLite - Part 3')


turtleDraw = turtle.Turtle()
turtleDraw.speed(10) #Sets the speed of the turtle
turtleDraw.penup()
turtle.setup (450,450) #Sets the dimensions of the main window


# Reads a text file line by line
turtleDrawTextFile = open(TEXTFILENAME, 'r')
line = turtleDrawTextFile.readline()

while line:
    print(line, end='')
    line = turtleDrawTextFile.readline()
    parts = line.split(' ')

    if (len(parts) == 3):
        color = parts[0]
        x = int(parts[1])
        y = int(parts[2])
        
        turtleDraw.color(color)
        turtleDraw.goto(x,y)
   
        # Todo: Calculate the distance and add it to the total distance
        
        turtleDraw.pendown()

    if (len(parts) == 1): # Assumes that a single word on a line is "stop"
        turtleDraw.penup()


#Todo: Print the total near the bottom right
turtle.done()
turtleDrawTextFile.close()

# Todo: Wait fot the user to press the enter key before closing 
print('\nEnd')
