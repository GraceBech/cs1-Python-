## Author  : Grace Bech
## Date    : 3th February 2023
## Purpose : Creating a pong game
from cs1lib import *

from cs1lib import *
img = False
# Constants
WINDOW_X = 400
WINDOW_Y = 400
WIDTH = 20
HEIGHT = 80
RADIUS = 10

# Paddles
right_paddle_y = 320
right_paddle_x = 380
left_paddle_x = 0
left_paddle_y = 0
paddle_speed_controller = 5 # controls the speed of the paddles up and down


# Ball's coordinates
ball_x_position = 200
ball_y_position = 200

start = False
restart = False
x_velocity = 3
y_velocity = 3
positive_x_velocity = 3
positive_y_velocity = 3
negative_y_velocity = -3
negative_x_velocity = -3


a_pressed = False
z_pressed = False
m_pressed = False
k_pressed = False
s_pressed = False
q_pressed = False

ball_ceiling_floor_move = False
score = False
def background():
    set_clear_color(0.4, 1, 1) # Sets background to sky blue
    clear()


def key_pressed(key):
    global a_pressed, z_pressed, k_pressed, m_pressed, start, s_pressed,  pressed, ball_x_position, ball_y_position, x_velocity, y_velocity, restart, ball_move
    if key == "a":  # move left paddle up
        a_pressed = True
    if key == "z":  # move left paddle down
        z_pressed = True
    if key == "m":  # move right paddle down
        m_pressed = True
    if key == "k":  # move right paddle up
        k_pressed = True
    if key == "q":  # Quits and restarts the game
        cs1_quit()
    if key == " ":   # Restart

        if x_velocity != 0 and y_velocity != 0: # Initialize the conditons for the game to restart when the space is clicked
            ball_x_position = 200
            ball_y_position = 200

            x_velocity = 0
            y_velocity = 0
        else:
            x_velocity = 3
            y_velocity = 3



def key_release(key):
    global a_pressed, z_pressed, k_pressed, m_pressed, start, ball_x_position, ball_y_position, ball_move
    if key == "a":
        a_pressed = False
    if key == "z":
        z_pressed = False
    if key == "m":
        m_pressed = False
    if key == "k":
        k_pressed = False


def restart_game(): # Restart's the game after the ball leaves the window frame
    global positive_x_velocity, negative_x_velocity, right_paddle_x, right_paddle_y, ball_x_position, ball_y_position, left_paddle_x, left_paddle_y, restart, x_velocity, y_velocity, positive_y_velocity, positive_x_velocity, positive_y_velocity, negative_y_velocity, start
    if restart == True:
        positive_x_velocity = 3
        negative_x_velocity = 3

        x_velocity = 3
        y_velocity = 3

        negative_y_velocity = -3
        negative_x_velocity = -3

        right_paddle_y = 320
        right_paddle_x = 380
        ball_x_position = 200
        ball_y_position = 200
        left_paddle_y = 0
        left_paddle_x = 0


def left_paddle():  # this part prevents the left paddle from going outside the window frame
    global left_paddle_x, left_paddle_y, a_pressed, z_pressed
    set_fill_color(1, 1, 0)
    # This part prevents it from going up, outside the window
    if a_pressed:
        if left_paddle_y < 0:
            left_paddle_y = 0
        left_paddle_y = left_paddle_y - paddle_speed_controller
    # prevents the left paddle from going outside the paddle when z is pressed.
    if z_pressed:
        if left_paddle_y > 320:
            left_paddle_y = 320
        left_paddle_y = left_paddle_y + paddle_speed_controller
    draw_rectangle(left_paddle_x, left_paddle_y, WIDTH, HEIGHT)


# This part of the code, prevents the right paddle from living the window
def right_paddle():
    global right_paddle_x, right_paddle_y, m_pressed, k_pressed
    set_fill_color(1, 1, 0)
    if k_pressed:  # prevents it from going up passed the window frame
        if right_paddle_y < 0:
            right_paddle_y = 0
        right_paddle_y = right_paddle_y - paddle_speed_controller
    if m_pressed:  # prevents the ball from going down past the window frame
        if right_paddle_y > 320:
            right_paddle_y = 320
        right_paddle_y = right_paddle_y + paddle_speed_controller
    draw_rectangle(right_paddle_x, right_paddle_y, WIDTH, HEIGHT)

def ball_move():
    global ball_x_position, ball_y_position, x_velocity, y_velocity, start, negative_y_velocity, negative_x_velocity, ball_move
    draw_circle(ball_x_position, ball_y_position, RADIUS)

    if ball_move:
        # function for when the ball hits the ceiling and floor
        if ball_y_position + RADIUS > 400:  # enables the ball to bounce back when it hits the floor
            y_velocity = -y_velocity

        if ball_y_position - RADIUS < 0:  # prevents the ball from leaving the window from the ceiling
            y_velocity = -y_velocity


        # function for when the game is paused
        ball_y_position = ball_y_position - y_velocity
        ball_x_position = ball_x_position - x_velocity
        set_stroke_color(0, 0, 0)


def ball_hit_paddles():
    # function for when the ball hits the paddle. Makes the ball bounce back when the ball hits the left paddle
    global ball_x_position, ball_y_position, x_velocity, y_velocity, start, negative_y_velocity, negative_x_velocity, s_pressed, img, goal, restart, right_paddle_x, right_paddle_y, left_paddle_x, left_paddle_y, positive_x_velocity

    if ball_x_position - RADIUS <= left_paddle_x + WIDTH and left_paddle_y <= ball_y_position <= left_paddle_y + HEIGHT:
        x_velocity = negative_x_velocity

# makes the ball to bounce back, when it hits the right paddle
    elif ball_x_position + RADIUS >= right_paddle_x and right_paddle_y <= ball_y_position <= right_paddle_y + HEIGHT:
        x_velocity = positive_x_velocity


    elif ball_x_position > 400 or ball_x_position < 0:  # Ensures that the ball is back to its initial position, when it leaves the frame
        # initial position and velocities
        ball_x_position = 200
        ball_y_position = 200

        x_velocity = 0
        y_velocity = 0


# Quits the game when "q" is pressed
def quit():
    global ball_x_position, ball_y_position, x_velocity, y_velocity, start, negative_y_velocity, negative_x_velocity, s_pressed
    s_pressed = True
    if s_pressed == True:  # Keeps track of when the quit is called
        draw_rectangle(right_paddle_x, right_paddle_y, WIDTH, HEIGHT)
        draw_rectangle(left_paddle_x, left_paddle_y, WIDTH, HEIGHT)


# This part calls all the other variables.
def main_draw():
    background()
    left_paddle()
    right_paddle()

    ball_ceiling_floor_move()
    ball_hit_paddles()
    quit()



start_graphics(main_draw, key_press=key_pressed, key_release=key_release)

