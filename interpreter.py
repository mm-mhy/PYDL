from textx import metamodel_from_file 
import turtle

def draw_shape(shape):
        turtle.pencolor(shape.line_color.color if shape.line_color is not None else 'black')
        turtle.fillcolor(shape.fill_color.color if shape.fill_color is not None else 'white')
        turtle.down()
        turtle.begin_fill()
        for l in shape.lines:
            draw_line(l)
        turtle.end_fill()

def draw_line(l):
        bearing = l.direction.bearing
        if bearing == 'E':
            turtle.setheading(0)
        elif bearing == 'NE':
            turtle.setheading(45)
        elif bearing == 'SE':
            turtle.setheading(-45)
        elif bearing == 'W':
            turtle.setheading(180)
        elif bearing =='NW':
            turtle.setheading(135)
        elif bearing =='SW':
            turtle.setheading(-135)
        elif bearing =='N':
            turtle.setheading(90)
        elif bearing =='S':
            turtle.setheading(-90)
        else:
            turtle.left(l.direction.angle.degrees)
        turtle.forward(l.length)


turtle_meta = metamodel_from_file("tx_turtle\\turtle.tx")

scene = turtle_meta.model_from_file("triangle_and_square.turtle")

for d in scene.draw_instructions:
    turtle.up()
    turtle.goto(d.position.x if d.position is not None else 0,
                d.position.y if d.position is not None else 0)
    draw_shape(d.shape)

turtle.hideturtle()
turtle.done()
