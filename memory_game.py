import turtle_helper
import game_helpers
import turtle
from GameHandler import GameHandler
from Button import Button


def main():
    turtle.tracer(0)
    turtle_helper.setup_game_space()
    turtle.update()
    turtle_helper.splash_screen()
    # turtle.tracer(1)
    # turtle.update()
    turtle.tracer(0)
    turtle_helper.background()
    Button(button='quit', x=330, y=-310)
    Button(button='load', x=330, y=-255)
    # Initialize the handler
    handler = GameHandler()
    handler.cards = game_helpers.create_cards(handler.card_count, handler)
    turtle_helper.transition()
    turtle.tracer(1)

    turtle.Screen().mainloop()

if __name__ == '__main__':
    main()