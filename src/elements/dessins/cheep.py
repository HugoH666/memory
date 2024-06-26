import usefull

def cheep(t, type_color, pixel_size):
    t.speed(100)

    if type_color == 1:
        body_color = "#FF0000"
    else:
        body_color = "#00FF00"

    # Contour noir
    usefull.row_left_squares(t, 4, pixel_size)
    t.backward(pixel_size)
    usefull.row_right_squares(t, 6, pixel_size)
    usefull.row_left_squares(t, 2, pixel_size)
    usefull.double_walk_along_up_square_left(t, pixel_size)
    t.backward(pixel_size)
    usefull.row_right_squares(t, 2, pixel_size)
    usefull.row_left_squares(t, 3, pixel_size)
    usefull.double_walk_along_up_square_left(t, pixel_size)
    usefull.row_right_squares(t, 1, pixel_size)
    t.left(90)
    usefull.row_right_squares(t, 3, pixel_size)
    t.left(90)
    usefull.row_right_squares(t, 1, pixel_size)
    usefull.row_left_squares(t, 2, pixel_size)
    t.left(90)
    usefull.row_left_squares(t, 3, pixel_size)
    t.right(90)
    usefull.row_left_squares(t, 1, pixel_size)
    t.right(90)
    t.forward(pixel_size)
    usefull.left_square(t, pixel_size)
    usefull.right_square(t, pixel_size)
    t.left(90)
    usefull.row_left_squares(t, 4, pixel_size)
    t.right(90)
    for _ in range(4):
        usefull.right_square(t, pixel_size)
        t.forward(pixel_size)
        t.right(90)
        t.forward(pixel_size)
        t.left(90)
    t.right(90)
    usefull.row_left_squares(t, 3, pixel_size)
    usefull.right_square(t, pixel_size)
    t.backward(3*pixel_size)
    t.left(90)
    usefull.row_right_squares(t, 4, pixel_size)
    usefull.row_left_squares(t, 1, pixel_size)
    t.left(90)
    t.forward(pixel_size)
    usefull.walk_along_up_square_right(t, pixel_size)
    usefull.row_left_squares(t, 2, pixel_size)
    usefull.row_right_squares(t, 5, pixel_size)
    t.left(90)
    usefull.row_left_squares(t, 2, pixel_size)
    t.left(90)
    usefull.row_left_squares(t, 2, pixel_size)
    t.backward(pixel_size)
    usefull.row_right_squares(t, 5, pixel_size)
    usefull.walk_along_up_square_right(t, pixel_size)
    for _ in range(2):
        usefull.right_square(t, pixel_size)
        t.forward(pixel_size)
        t.right(90)
        t.forward(pixel_size)
        t.left(90)
    t.up()
    t.backward(6*pixel_size)
    t.left(90)
    t.forward(2*pixel_size)
    t.left(180)
    t.down()
    usefull.row_left_squares(t, 5, pixel_size)
    usefull.row_right_squares(t, 1, pixel_size)
    t.right(90)
    t.forward(pixel_size)
    usefull.row_left_squares(t, 3, pixel_size)
    t.backward(pixel_size)
    usefull.row_right_squares(t, 5, pixel_size)
    t.right(90)
    t.forward(pixel_size)
    usefull.row_left_squares(t, 4, pixel_size)
    usefull.row_right_squares(t, 1, pixel_size)
    t.right(90)
    t.forward(pixel_size)
    usefull.row_left_squares(t, 3, pixel_size)
    usefull.walk_along_up_square_left(t, pixel_size)
    usefull.row_left_squares(t, 2, pixel_size)
    t.left(180)
    t.forward(3*pixel_size)
    usefull.walk_along_up_square_left(t, pixel_size)
    usefull.row_left_squares(t, 1, pixel_size)
    t.up()
    t.forward(2*pixel_size)
    t.left(90)
    t.forward(6*pixel_size)
    t.down()
    usefull.row_left_squares(t, 3, pixel_size)
    t.left(90)
    usefull.row_left_squares(t, 4, pixel_size)
    usefull.right_square(t, pixel_size)
    t.backward(3*pixel_size)
    t.right(90)
    usefull.row_left_squares(t, 2, pixel_size)
    t.left(90)
    t.forward(5*pixel_size)
    usefull.row_left_squares(t, 1, pixel_size)
    t.left(90)
    t.forward(pixel_size)
    usefull.row_right_squares(t, 2, pixel_size)
    usefull.left_square(t, pixel_size)

    # Bouche
    t.left(90)
    t.color("#FFFF00")
    usefull.row_left_squares(t, 3, pixel_size)
    usefull.walk_along_up_square_right(t, pixel_size)
    usefull.row_right_squares(t, 3, pixel_size)
    t.left(180)
    usefull.row_right_squares(t, 5, pixel_size)
    t.right(90)
    t.forward(2*pixel_size)
    usefull.left_square(t, pixel_size)
    usefull.right_square(t, pixel_size)
    t.forward(pixel_size)
    t.right(90)
    usefull.row_left_squares(t, 4, pixel_size)
    t.left(180)
    usefull.row_left_squares(t, 2, pixel_size)

    # Ventre
    usefull.walk_along_up_square_right(t, pixel_size)
    t.color("#FFFFFF")
    t.up()
    t.forward(2*pixel_size)
    t.down()
    usefull.row_right_squares(t, 5, pixel_size)
    t.backward(4*pixel_size)
    usefull.row_left_squares(t, 5, pixel_size)
    t.backward(4*pixel_size)
    usefull.double_walk_along_up_square_left(t, pixel_size)
    usefull.row_right_squares(t, 6, pixel_size)
    t.backward(5*pixel_size)
    usefull.row_left_squares(t, 5, pixel_size)

    # Queue
    t.up()
    t.forward(pixel_size)
    t.color("#FFFF00")
    t.down()
    usefull.row_left_squares(t, 2, pixel_size)
    t.left(90)
    usefull.row_left_squares(t, 3, pixel_size)
    t.backward(2*pixel_size)
    usefull.row_right_squares(t, 3, pixel_size)

    # Aile
    t.color("#FFFFFF")
    t.forward(pixel_size)
    t.left(90)
    usefull.row_left_squares(t, 4, pixel_size)
    t.backward(4*pixel_size)
    usefull.row_right_squares(t, 3, pixel_size)
    t.left(90)
    t.forward(pixel_size)
    usefull.row_left_squares(t, 1, pixel_size)
    t.right(90)
    usefull.row_right_squares(t, 2, pixel_size)
    t.backward(pixel_size)
    usefull.row_left_squares(t, 2, pixel_size)

    # Corps
    t.color(body_color)
    usefull.row_right_squares(t, 3, pixel_size)
    t.backward(2*pixel_size)
    usefull.row_left_squares(t, 3, pixel_size)
    t.left(90)
    t.forward(2*pixel_size)
    t.left(90)
    usefull.row_left_squares(t, 1, pixel_size)
    usefull.right_square(t, pixel_size)
    usefull.row_left_squares(t, 2, pixel_size)
    t.up()
    t.forward(4*pixel_size)
    t.down()
    usefull.left_square(t, pixel_size)
    t.up()
    t.left(90)
    t.forward(4*pixel_size)
    t.left(90)
    t.forward(pixel_size)
    t.down()
    usefull.row_right_squares(t, 4, pixel_size)
    t.backward(3*pixel_size)
    usefull.row_left_squares(t, 3, pixel_size)
    usefull.double_right_linear_traverse(t, pixel_size)
    usefull.row_right_squares(t, 5, pixel_size)
    t.left(180)
    t.forward(pixel_size)
    usefull.row_right_squares(t, 4, pixel_size)
    t.right(90)
    t.forward(pixel_size)
    t.right(90)
    usefull.row_left_squares(t, 3, pixel_size)

    # Crête
    t.forward(pixel_size)
    t.left(90)
    t.color("#FFFF00")
    usefull.row_right_squares(t, 2, pixel_size)
    t.left(90)
    usefull.left_square(t, pixel_size)
    usefull.row_right_squares(t, 5, pixel_size)
    t.right(90)
    t.forward(pixel_size)
    usefull.left_square(t, pixel_size)
    t.right(90)
    usefull.row_left_squares(t, 3, pixel_size)

    # Yeux
    t.up()
    t.color("#FFFFFF")
    usefull.double_right_linear_traverse(t, pixel_size)
    t.forward(3*pixel_size)
    t.left(90)
    t.down()
    t.begin_fill()
    t.forward(5*pixel_size)
    t.right(90)
    usefull.low_traverse(t, pixel_size)
    t.right(90)
    t.forward(2*pixel_size)
    usefull.walk_along_up_square_right(t, pixel_size)
    t.forward(5*pixel_size)
    t.right(90)
    t.forward(4*pixel_size)
    t.right(90)
    usefull.low_traverse(t, pixel_size)
    t.right(90)
    t.forward(pixel_size)
    t.right(90)
    usefull.low_traverse(t, pixel_size)
    usefull.walk_along_up_square_left(t, pixel_size)
    usefull.low_traverse(t, pixel_size)
    usefull.from_above(t, pixel_size)
    usefull.low_traverse(t, pixel_size)
    t.end_fill()

    # Pupilles
    t.left(180)
    t.forward(4*pixel_size)
    t.left(90)
    t.forward(2*pixel_size)
    t.color("#000000")
    usefull.row_left_squares(t, 2, pixel_size)
    t.up()
    usefull.double_right_linear_traverse(t, pixel_size)
    t.down()
    usefull.row_left_squares(t, 2, pixel_size)