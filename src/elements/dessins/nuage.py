import usefull
import time
import turtle

def nuage(t, body_color, reflect_color, eyes_color):
    t.speed(100)

    # Contour noir
    usefull.row_right_squares(t, 4)
    usefull.row_left_squares(t, 2)
    usefull.row_right_squares(t, 4)
    usefull.left_square(t)
    usefull.low_traverse(t)
    usefull.walk_along_up_square(t)
    usefull.row_left_squares(t, 3)
    usefull.row_right_squares(t, 6)
    usefull.row_left_squares(t, 3)
    t.left(90)
    t.forward(20)
    usefull.walk_along_up_square(t)
    usefull.row_left_squares(t, 1)
    usefull.row_right_squares(t, 10)
    usefull.row_left_squares(t, 1)
    t.left(90)
    t.forward(20)
    usefull.walk_along_up_square(t)
    usefull.row_left_squares(t, 3)
    usefull.row_right_squares(t, 6)
    usefull.row_left_squares(t, 3)
    t.left(90)
    t.forward(20)
    usefull.right_square(t)

    # Reflet
    t.color(reflect_color)
    usefull.row_left_squares(t, 1)
    usefull.row_right_squares(t, 4)
    usefull.row_left_squares(t, 2)
    usefull.row_right_squares(t, 4)
    t.left(90)
    usefull.left_square(t)
    usefull.walk_along_up_square(t)
    usefull.row_left_squares(t, 4)
    t.backward(20)
    usefull.row_right_squares(t, 6)
    usefull.row_left_squares(t, 3)
    t.left(90)
    t.forward(20)
    usefull.right_square(t)

    # Encrage
    t.color(body_color)
    t.begin_fill()
    t.forward(20)
    usefull.walk_along_up_square(t)
    t.forward(180)
    t.left(90)
    t.forward(20)
    usefull.walk_along_up_square(t)
    t.forward(60)
    usefull.walk_along_up_square(t)
    t.forward(120)
    usefull.long_left_diagonal(t)
    t.left(90)
    t.forward(20)
    usefull.walk_along_up_square(t)
    t.forward(80)
    usefull.long_left_diagonal(t)
    usefull.walk_along_up_square(t)
    t.forward(60)
    t.left(90)
    t.forward(20)
    usefull.walk_along_up_square(t)
    t.forward(60)
    usefull.walk_along_up_square(t)
    t.forward(100)
    t.left(90)
    t.forward(20)
    t.right(90)
    t.forward(60)
    t.left(90)
    t.forward(20)
    t.end_fill()

    # Yeux
    t.up()
    t.forward(60)
    t.left(90)
    t.forward(60)
    t.color(eyes_color)
    t.down()
    usefull.row_left_squares(t, 3)
    t.up()
    t.right(90)
    t.forward(60)
    t.right(90)
    t.down()
    usefull.row_right_squares(t, 3)

    # Bouche
    t.up()
    t.backward(120)
    t.left(90)
    t.forward(20)
    t.left(180)
    t.color("#000000")
    t.down()
    usefull.row_left_squares(t, 1)
    usefull.row_right_squares(t, 4)
    usefull.row_left_squares(t, 1)

    time.sleep(5)

t = turtle.Turtle()
nuage(t, "#777777", "#333333", "#FFFF00")