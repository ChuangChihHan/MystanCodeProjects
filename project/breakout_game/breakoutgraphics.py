"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Height of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:
    # constructor
    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        self.window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        self.window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=self.window_width, height=self.window_height, title=title)

        # Create a paddle
        self.paddle = GRect(width=paddle_width, height=paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, x=(self.window_width - paddle_width)/2,
                        y=(self.window_height-paddle_offset-paddle_height))

        # Center a filled ball in the graphical window
        self.ball = GOval(width=ball_radius*2, height=ball_radius*2)
        self.ball.filled = True
        self.window.add(self.ball, x=(self.window_width - ball_radius*2)/2, y=(self.window_height-ball_radius*2)/2)
        self.ball_radius = ball_radius

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # Initialize our mouse listeners
        self.start = 0
        onmousemoved(self.paddle_move)
        onmouseclicked(self.ball_move)

        # Draw bricks
        for row in range(brick_rows):
            for column in range(brick_cols):
                if row < 2:
                    self.brick = GRect(width=BRICK_WIDTH, height=BRICK_HEIGHT, x=(BRICK_SPACING + BRICK_WIDTH) * column, y=BRICK_OFFSET+(BRICK_SPACING+BRICK_HEIGHT)*row)
                    self.brick.filled = True
                    self.brick.fill_color = 'red'
                    self.brick.color = 'red'
                    self.window.add(self.brick)
                elif 2 <= row < 4:
                    self.brick = GRect(width=BRICK_WIDTH, height=BRICK_HEIGHT, x=(BRICK_SPACING + BRICK_WIDTH) * column, y=BRICK_OFFSET+(BRICK_SPACING+BRICK_HEIGHT)*row)
                    self.brick.filled = True
                    self.brick.fill_color = 'orange'
                    self.brick.color = 'orange'
                    self.window.add(self.brick)
                elif 4 <= row < 6:
                    self.brick = GRect(width=BRICK_WIDTH, height=BRICK_HEIGHT, x=(BRICK_SPACING + BRICK_WIDTH) * column, y=BRICK_OFFSET+(BRICK_SPACING+BRICK_HEIGHT)*row)
                    self.brick.filled = True
                    self.brick.fill_color = 'yellow'
                    self.brick.color = 'yellow'
                    self.window.add(self.brick)
                elif 6 <= row < 8:
                    self.brick = GRect(width=BRICK_WIDTH, height=BRICK_HEIGHT, x=(BRICK_SPACING + BRICK_WIDTH) * column, y=BRICK_OFFSET+(BRICK_SPACING+BRICK_HEIGHT)*row)
                    self.brick.filled = True
                    self.brick.fill_color = 'green'
                    self.brick.color = 'green'
                    self.window.add(self.brick)
                else:
                    self.brick = GRect(width=BRICK_WIDTH, height=BRICK_HEIGHT, x=(BRICK_SPACING + BRICK_WIDTH) * column, y=BRICK_OFFSET+(BRICK_SPACING+BRICK_HEIGHT)*row)
                    self.brick.filled = True
                    self.brick.fill_color = 'blue'
                    self.brick.color = 'blue'
                    self.window.add(self.brick)

        # check for collisions
        self.brick_number = brick_cols * brick_rows

    def paddle_move(self, mouse):
        """
        This method is used to control the movement of the paddle.
        The paddle will only move horizontally when the mouse move.
        Note that the paddle is at a fixed distance(PADDLE_OFFSIDE) from the bottom of the window.
        :param mouse: mouse event
        :return:
        """
        self.paddle.y = (self.window.height - PADDLE_OFFSET - self.paddle.height)
        self.paddle.x = mouse.x - self.paddle.width/2  # the mouse's x coordination is the same as the paddle's central.
        # the condition when the mouse moves outside the window.
        if self.paddle.x < 0:  # the mouse exceeds the windows horizontally
            self.paddle.x = 0  # the paddle will stays at the border of left side of the window
        elif self.paddle.x > (self.window.width - self.paddle.width):
            self.paddle.x = self.window.width - self.paddle.width # the paddle will stays at the border of right side of the window

    def ball_move(self, mouse):
        """
        This method is used to control the movement of the ball and make sure it only moves when the mouse clicks
        the first time.
        :param mouse: mouse event
        :return: start variable to initiate the movement of the ball once the mouse clicks.
        """
        # below if-else statement prevent the ball from changing its current movement when it is moving.
        if self.__dx and self.__dy != 0:  # if ball is moving
            pass  # no action should be done
        else:  # if ball is still (meaning its at the starting point)
            self.__dx = random.randint(1, MAX_X_SPEED)  # assign ball speed
            self.__dy = INITIAL_Y_SPEED
            if random.random() > 0.5:  # change the ball's horizontal speed
                self.__dx = - self.__dx
        # initiates the movement of the ball once the user clicks
        self.start = 1
        return self.start

    # setter
    @property # getter
    def vx(self):
        return self.__dx  # get the private variable so the user side can see this variable

    @vx.setter  # the user can change the speed or direction horizontally
    def vx(self, new_vx):
        self.__dx = new_vx

    # setter
    @property
    def vy(self):
        return self.__dy

    @vy.setter # the user can change the speed or direction vertically
    def vy(self, new_vy):
        self.__dy = new_vy

    def bump_brick(self):
        """
        This method is used to make sure the ball return reversely and remove the brick once it collides with the brick.
        """
        # get the coordination of the ball's four vertexes
        vertex_1 = self.window.get_object_at(self.ball.x, self.ball.y)
        vertex_2 = self.window.get_object_at(self.ball.x, self.ball.y+self.ball.height)
        vertex_3 = self.window.get_object_at(self.ball.x+self.ball.width, self.ball.y)
        vertex_4 = self.window.get_object_at(self.ball.x+self.ball.width, self.ball.y+self.ball.height)
        # if the coordination of the ball's vertexes meets with an object and that object is not paddle
        # (meaning the object is brick)
        if vertex_1 is not None and vertex_1 is not self.paddle:
            self.__dy = - self.__dy  # make sure the ball moves vertically in reverse direction
            self.window.remove(vertex_1)  # remove the brick
            self.brick_number -= 1  # count the number of brick removal
        elif vertex_2 is not None and vertex_2 is not self.paddle:
            self.__dy = - self.__dy
            self.window.remove(vertex_2)
            self.brick_number -= 1
        elif vertex_3 is not None and vertex_3 is not self.paddle:
            self.__dy = - self.__dy
            self.window.remove(vertex_3)
            self.brick_number -= 1
        elif vertex_4 is not None and vertex_4 is not self.paddle:
            self.__dy = - self.__dy
            self.window.remove(vertex_4)
            self.brick_number -= 1

    def bump_paddle(self):
        """
        This method is used to make sure when the ball hits the paddle it will move in a reverse direction vertically
        :return:
        """
        vertex_1 = self.window.get_object_at(self.ball.x, self.ball.y)
        vertex_2 = self.window.get_object_at(self.ball.x, self.ball.y + self.ball.height)
        vertex_3 = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y)
        vertex_4 = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y + self.ball.height)
        # if any of the vertex of the ball collides with the paddle
        if vertex_1 == self.paddle or vertex_2 == self.paddle or vertex_3 == self.paddle or vertex_4 == self.paddle:
            if self.__dy > 0:  # if the ball falls down vertically
                self.__dy = - self.__dy  # it will be in a reverse direction vertically

    def reset_ball(self):
        """
        This method is used to make sure the ball will appear in the center of the window and stay still.
        :return:
        """
        self.window.add(self.ball, x=(self.window_width - self.ball_radius * 2) / 2,
                        y=(self.window_height - self.ball_radius * 2) / 2)
        self.start = 0  # stop the ball from moving (it will only moves when the start == 1)
        return self.start







