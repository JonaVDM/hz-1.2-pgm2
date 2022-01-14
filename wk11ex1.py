GlowScript 2.8 VPython
#
# game_starter.py
#
# Een interactie met 3D graphics bouwen met Python
#   Documentatie: https://www.glowscript.org/docs/VPythonDocs/index.html
#   Voorbeelden:  https://www.glowscript.org/#/user/GlowScriptDemos/folder/Examples/
#

scene.bind('keydown', keydown_fun)
scene.bind('click', click_fun)
scene.background = 0.8 * vector(1, 1, 1)
scene.width = 640
scene.height = 480


def make_alien(starting_position, starting_vel=vector(0, 0, 0)):
    """The lines below make a new "frame", which is a container with a
       local coordinate system.
       The arguments to make_alien allow for any initial starting position
       and initial starting velocity, with a default starting velocity
       of vector(0, 0, 0).

       Compounds can have any number of components.  Here are the
       alien's components:
    """
    alien_body = sphere(size=1.0 * vector(1, 1, 1),
                        pos=vector(0, 0, 0), color=color.green)
    alien_eye1 = sphere(size=0.3 * vector(1, 1, 1), pos=.42 *
                        vector(.7, .5, .2), color=color.white)
    alien_eye2 = sphere(size=0.3 * vector(1, 1, 1), pos=.42 *
                        vector(.2, .5, .7), color=color.white)
    alien_hat = cylinder(pos=0.42 * vector(0, .9, -.2), axis=vector(.02, .2, -.02),
                         size=vector(0.2, 0.7, 0.7), color=color.magenta)
    alien_objects = [alien_body, alien_eye1, alien_eye2, alien_hat]
    com_alien = compound(alien_objects, pos=starting_position)
    com_alien.vel = starting_vel
    return com_alien


ground = box(size=vector(20, 1, 20), pos=vector(
    0, -1, 0), color=.4*vector(1, 1, 1))

# Create walls
wall_a = box(pos=vector(0, 0, -10), axis=vector(1, 0, 0),
             size=vector(20, 1, .2), color=vector(1.0, 0.7, 0.3))
wall_b = box(pos=vector(-10, 0, 0), axis=vector(0, 0, 1),
             size=vector(20, 1, .2), color=color.blue)
wall_c = box(pos=vector(0, 0, 10), axis=vector(1, 0, 0),
             size=vector(20, 1, .2), color=color.green)
wall_d = box(pos=vector(10, 0, 0), axis=vector(0, 0, 1),
             size=vector(20, 1, .2), color=color.red)

# Crate objects
ball = sphere(size=1.0*vector(1, 1, 1), color=randcolor())
ball.vel = vector(0, 0, 0)

alien = make_alien(starting_position=vector(
    6, 0, -6), starting_vel=vector(0, 0, -1))

color_ball_1 = sphere(pos=vector(0, 0, 3), size=1.0 *
                      vector(1, 1, 1), color=randcolor())
color_ball_2 = sphere(pos=vector(0, 0, -10), size=1.0 *
                      vector(1, 1, 1), color=randcolor())
color_ball_2.vel = vector(-5, 0, 5)

RATE = 60
dt = 1.0/RATE
scene.autoscale = False
scene.forward = vector(0, -3, -2)

while True:
    rate(RATE)

    alien.pos = alien.pos + alien.vel*dt
    ball.pos = ball.pos + ball.vel*dt
    color_ball_2.pos = color_ball_2.pos + color_ball_2.vel*dt

    arena_collide(ball)
    arena_collide(alien)
    arena_collide(color_ball_2)

    # Change the color if you touch the color balls
    if mag(ball.pos - color_ball_1.pos) < 1.0 or mag(ball.pos - color_ball_2.pos) < 1.0:
        color_ball_1.color = randcolor()
        color_ball_2.color = randcolor()
        ball.color = randcolor()

    # Geef de alien verticale snelheid als de bal de alien raakt
    if mag(ball.pos - alien.pos) < 1.0:
        print("Op naar de sterren, en daar voorbij!")
        alien.color = color.gray(.8)
        alien.vel = vector(0, 1, 0)


def keydown_fun(event):
    """This function is called each time a key is pressed."""
    # ball.color = randcolor() # just no
    key = event.key
    ri = randint(0, 10)
    # print("toets:", key, ri)

    amt = 0.42
    if key == 'up' or key in 'wWiI':
        ball.vel = ball.vel + vector(0, 0, -amt)
    elif key == 'left' or key in 'aAjJ':
        ball.vel = ball.vel + vector(-amt, 0, 0)
    elif key == 'down' or key in 'sSkK':
        ball.vel = ball.vel + vector(0, 0, amt)
    elif key == 'right' or key in "dDlL":
        ball.vel = ball.vel + vector(amt, 0, 0)
    elif key in ' rR':
        ball.vel = vector(0, 0, 0)  # Opnieuw beginne! via de spatiebalk, " "
        ball.pos = vector(0, 0, 0)


def click_fun(event):
    """This function is called each time the mouse is clicked."""
    print("event is", event.event, event.which)


# +++ Einde van het AFHANDELEN van EVENTS


# +++ Andere functies kan je hier neerzetten...


def choice(L):
    """Implements Python's choice using the random() function."""
    length = len(L)
    random_index = int(length * random())
    return L[random_index]


def randint(low, hi):
    """Implements Python's randint using the random() function.
       returns an int from low to hi _inclusive_ (so, it's not 100% Pythonic)
    """
    if hi < low:
        low, hi = hi, low
    length = int(hi) - int(low) + 1.0
    rand_value = length * random() + int(low)
    return int(rand_value)


def randcolor():
    """Returns a vector of (r, g, b) random from 0.0 to 1.0."""
    r = random(0.0, 1.0)
    g = random(0.0, 1.0)
    b = random(0.0, 1.0)
    return vector(r, g, b)


def arena_collide(obj):
    """ Arena collisions
    """
    if obj.pos.z < wall_a.pos.z:
        obj.pos.z = wall_a.pos.z
        obj.vel.z *= -1.0

    if obj.pos.x < wall_b.pos.x:
        obj.pos.x = wall_b.pos.x
        obj.vel.x *= -1.0

    if obj.pos.z > wall_c.pos.z:
        obj.pos.z = wall_c.pos.z
        obj.vel.z *= -1.0

    if obj.pos.x > wall_d.pos.x:
        obj.pos.x = wall_d.pos.x
        obj.vel.x *= -1.0
