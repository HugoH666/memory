import usefull

def oeuf(t, egg_color, dots_color, pixel_size):
    t.speed(100)

    # Contour noir
    usefull.row_right_squares(t, 4, pixel_size)
    usefull.row_left_squares(t, 2, pixel_size)
    t.left(90)
    t.forward(pixel_size)
    usefull.right_square(t, pixel_size)
    usefull.double_high_traverse(t, pixel_size)
    usefull.row_left_squares(t, 2, pixel_size)
    usefull.row_right_squares(t, 4, pixel_size)
    usefull.row_left_squares(t, 2, pixel_size)
    usefull.double_walk_along_up_square_left(t, pixel_size)
    usefull.row_right_squares(t, 2, pixel_size)
    usefull.left_square(t, pixel_size)
    t.forward(pixel_size)
    usefull.double_walk_along_up_square_left(t, pixel_size)
    usefull.right_square(t, pixel_size)
    t.forward(pixel_size)
    t.left(90)
    usefull.row_right_squares(t, 4, pixel_size)
    usefull.left_square(t, pixel_size)
    t.forward(pixel_size)
    usefull.double_walk_along_up_square_left(t, pixel_size)
    usefull.right_square(t, pixel_size)
    t.forward(2*pixel_size)
    t.left(90)
    usefull.row_left_squares(t, 2, pixel_size)
    usefull.row_right_squares(t, 2, pixel_size)
    usefull.walk_along_up_square_right(t, pixel_size)
    usefull.row_right_squares(t, 4, pixel_size)
    usefull.row_left_squares(t, 2, pixel_size)
    t.left(90)
    t.forward(pixel_size)
    usefull.right_square(t, pixel_size)
    t.forward(pixel_size)
    usefull.walk_along_up_square_right(t, pixel_size)
    usefull.row_right_squares(t, 2, pixel_size)

    # Encrage
    t.color(egg_color)
    t.begin_fill()
    usefull.walk_along_up_square_right(t, pixel_size)
    t.forward(4*pixel_size)
    usefull.long_left_diagonal(t, pixel_size)
    t.left(90)
    t.forward(pixel_size)
    usefull.walk_along_up_square_right(t, pixel_size)
    t.forward(2*pixel_size)
    usefull.walk_along_up_square_right(t, pixel_size)
    t.forward(4*pixel_size)
    usefull.long_left_diagonal(t, pixel_size)
    usefull.long_left_diagonal(t, pixel_size)
    usefull.walk_along_up_square_left(t, pixel_size)
    usefull.low_traverse(t, pixel_size)
    usefull.walk_along_up_square_right(t, pixel_size)
    t.forward(4*pixel_size)
    usefull.walk_along_up_square_left(t, pixel_size)
    usefull.low_traverse(t, pixel_size)
    usefull.walk_along_up_square_right(t, pixel_size)
    t.forward(2*pixel_size)
    usefull.walk_along_up_square_right(t, pixel_size)
    t.forward(2*pixel_size)
    usefull.walk_along_up_square_right(t, pixel_size)
    t.forward(4*pixel_size)
    usefull.long_left_diagonal(t, pixel_size)
    t.left(90)
    t.forward(pixel_size)
    usefull.walk_along_up_square_right(t, pixel_size)
    t.forward(2*pixel_size)
    t.end_fill()

    # Pois inférieur gauche
    t.up()
    t.color(dots_color)
    t.backward(2*pixel_size)
    t.left(90)
    t.down()
    usefull.row_right_squares(t, 3, pixel_size)
    t.left(90)
    usefull.row_right_squares(t, 2, pixel_size)
    t.backward(pixel_size)
    t.left(90)
    usefull.row_left_squares(t, 2, pixel_size)

    # Pois inférieur droit
    t.up()
    t.left(90)
    t.forward(9*pixel_size)
    t.left(90)
    t.down()
    usefull.row_left_squares(t, 3, pixel_size)
    t.backward(3*pixel_size)
    usefull.row_right_squares(t, 4, pixel_size)
    t.right(90)
    t.forward(pixel_size)
    t.right(90)
    usefull.row_left_squares(t, 2, pixel_size)

    # Pois supérieur droit
    t.up()
    t.left(180)
    t.forward(4*pixel_size)
    t.down()
    usefull.row_left_squares(t, 2, pixel_size)
    t.backward(2*pixel_size)
    usefull.double_walk_along_up_square_left(t, pixel_size)
    usefull.row_right_squares(t, 4, pixel_size)
    t.left(180)
    usefull.row_right_squares(t, 3, pixel_size)

    # Pois supérieur gauche
    t.up()
    t.right(90)
    t.forward(5*pixel_size)
    t.down()
    usefull.row_right_squares(t, 2, pixel_size)
    t.right(90)
    usefull.row_right_squares(t, 3, pixel_size)
    t.right(90)
    t.forward(2*pixel_size)
    t.left(90)
    t.forward(pixel_size)
    t.left(180)
    usefull.row_right_squares(t, 4, pixel_size)
    t.left(180)
    t.forward(pixel_size)
    usefull.row_right_squares(t, 3, pixel_size)

    # Pois central
    t.up()
    t.left(180)
    t.forward(6*pixel_size)
    t.down()
    usefull.row_right_squares(t, 3, pixel_size)
    usefull.low_traverse(t, pixel_size)
    t.left(90)
    usefull.row_left_squares(t, 5, pixel_size)
    t.backward(5*pixel_size)
    usefull.row_right_squares(t, 5, pixel_size)
    usefull.double_right_linear_traverse(t, pixel_size)
    usefull.row_right_squares(t, 5, pixel_size)
    t.backward(4*pixel_size)
    usefull.row_left_squares(t, 3, pixel_size)