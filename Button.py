import turtle

class Button:
    '''Constructor for the button class'''

    def __init__(self) -> None:

        screen = turtle.Screen()

        # register quit button
        screen.register_shape('quit_button.gif')
        self.quit_button = turtle.Turtle()
        self.quit_button.penup()
        self.quit_button.shape('quit_button.gif')
        self.quit_button.setpos(87, -189)
        self.quit_button.speed(0)