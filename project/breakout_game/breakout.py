"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120  # 120 frames per second
NUM_LIVES = 3			 # Number of attempts


def main():
    graphics = BreakoutGraphics()
    num_lives = NUM_LIVES

    # Add the animation loop here!
    while True:
        if graphics.start == 1:  # initiates the movement of the ball
            graphics.ball.move(graphics.vx, graphics.vy)  # the ball's moving speed
            # if the ball bumps the left or right side of the window
            if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window_width:
                graphics.vx = -graphics.vx  # its horizontal speed will change reversely
            # if the ball bumps the upper side of the window
            if graphics.ball.y <= 0:
                graphics.vy = -graphics.vy  # its vertical speed will change reversely
            graphics.bump_paddle()  # execute the bump_paddle method defined in breakoutgraphic class
            graphics.bump_brick()  # execute the bump_brick method defined in breakoutgraphic class
            if graphics.brick_number == 0: # when there is no brick left
                graphics.reset_ball()  # make the ball still in the center
                break  # break the loop to stop the game
            if graphics.ball.y >= graphics.window_height:  # if the ball exceeds the bottom side of the window
                num_lives -= 1  # the number of chance user plays will minus one
                if num_lives == 0:  # when the number of chance the user plays is zero
                    graphics.reset_ball() # make the ball still in the center
                    break # break the loop to stop the game
                graphics.reset_ball() # reset the ball in the center when the number of chance minus one
        pause(FRAME_RATE)  # pause the while loop to prevent the program execute too fast


if __name__ == '__main__':
    main()
