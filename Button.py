import turtle
import turtle_helper
class Button:
    '''Constructor for the button class'''

    def __init__(self, button, x, y) -> None:

        self.x = x
        self.y = y
        self.button = button

        if self.button == 'quit':
            screen = turtle.Screen()
            # register quit button
            screen.register_shape('quit_button.gif')
            self.quit_button = turtle.Turtle()
            self.quit_button.penup()
            self.quit_button.shape('quit_button.gif')
            self.quit_button.setpos(x, y)

            self.quit_button.onrelease(lambda x, y: self.quit_game(x, y))

        if self.button == 'load':
            screen = turtle.Screen()
            # register quit button
            screen.register_shape('load_button.gif')
            self.quit_button = turtle.Turtle()
            self.quit_button.penup()
            self.quit_button.shape('load_button.gif')
            self.quit_button.setpos(x, y)
            self.quit_button.onrelease(lambda x, y: self.load_cards(x, y))


    def quit_game(self, x, y):
        turtle.bye()
        # ADD QUIT MESSAGE


    def load_cards(self, x, y):
        pass