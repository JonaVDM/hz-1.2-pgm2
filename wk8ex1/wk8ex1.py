# wk8ex1.py
# Practicum 8
#
# Naam:
#

# laat deze importregel staan...
import png


#
# een testfunctie...
#
def test_fun():
    """ algorithmic image-creation one pixel at a time...
        this is a test function: it should output
        an image named test.png in the same directory
    """
    im = png.PNGImage(300, 200)

    for r in range(200):
        for c in range(300):
            if c == r:
                im.plot_point(c, r, (255, 0, 0))
            # else:
            #    im.plot_point( c, r, (255,0,0))

    im.save_file()

#
# zet je functies van Practicum 8 hieronder neer:
#


def mult(c, n):
    """ Return the multiplier of c and n
    """
    res = 0
    for _ in range(n):
        res += c
    return res


assert mult(3, 5) == 15
assert mult(6, 7) == 42
assert mult(1.5, 28) == 42.0


def update(c, n):
    """Update starts with z = 0 and runs z = z**2 + c
       for a total of n times. It returns the final z.
    """
    z = 0
    for _ in range(n):
        z = z ** 2 + c
    return z


assert update(1, 3) == 5
assert update(-1, 3) == -1
assert update(
    1, 10) == 3791862310265926082868235028027893277370233152247388584761734150717768254410341175325352026
assert update(-1, 10) == 0


def in_mset(c, n):
    """in_mset accepts
            c for the update step of z = z**2+c
            n, the maximum number of times to run that step
       Then, it returns
            False as soon as abs(z) gets larger than 2
            True if abs(z) never gets larger than 2 (for n iterations)
    """
    z = 0
    for _ in range(n):
        z = z ** 2 + c

        if abs(z) > 2:
            return False
    return True


assert in_mset(0 + 0j, 25) == True
assert in_mset(3 + 4j, 25) == False
assert in_mset(0.3 + -0.5j, 25) == True
assert in_mset(-0.7 + 0.3j, 25) == False
assert in_mset(0.42 + 0.2j, 25) == True
assert in_mset(0.42 + 0.2j, 50) == False


def we_want_this_pixel(col, row):
    """This function returns True if we want to show
       the pixel at col, row and False otherwise.
    """
    if col % 10 == 0 and row % 10 == 0:
        return True
    else:
        return False


def test():
    """This function demonstrates how
       to create and save a PNG image.
    """
    width = 300
    height = 200
    image = png.PNGImage(width, height)

    for col in range(width):
        for row in range(height):
            if we_want_this_pixel(col, row):
                image.plot_point(col, row)

    image.save_file()
# als je de line in de we_want_this_pixel veranderd de image van alleen punten
# naar ook lijnen tussen de punten.


def scale(pix, pix_max, float_min, float_max):
    """scale accepts
           pix, the CURRENT pixel column (or row)
           pix_max, the total # of pixel columns
           float_min, the min floating-point value
           float_max, the max floating-point value
       scale returns the floating-point value that
           corresponds to pix
    """
    f = pix / pix_max
    ss = float_max - float_min
    return ss * f + float_min


assert scale(100, 200, -2.0, 1.0) == -0.5
assert scale(100, 200, -1.5, 1.5) == 0.0
assert scale(100, 300, -2.0, 1.0) == -1.0
assert scale(25, 300, -2.0, 1.0) == -1.75


def mset():
    """Creates a 300x200 image of the Mandelbrot set
    """
    width = 300
    height = 200
    image = png.PNGImage(width, height)

    for col in range(width):
        for row in range(height):
            # Gebruik scale twee keer:
            #   één keer om het reële deel van c te bepalen (x)
            x = scale(col, width, -2.0, 1.0)
            #   één keer om het imaginaire deel van c te bepalen (y)
            y = scale(row, height, -1.0, 1.0)
            # DAARNA ken je c toe, kies je n en test je:
            c = x + y*1j
            n = 25
            if in_mset(c, n):
                image.plot_point(col, row, (247, 128, 2))
            else:
                image.plot_point(col, row, (12, 35, 150))
    # we hebben door alle pixels gelust; nu schrijven we het bestand
    image.save_file()
