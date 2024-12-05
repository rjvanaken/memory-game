import turtle_helper
import game_helpers
import turtle
from GameHandler import GameHandler
from Button import Button


def main():
    turtle.tracer(0)
    turtle_helper.setup_game_space()
    turtle_helper.splash_screen()
    # Initialize the handler
    handler = GameHandler()
    Button(button='quit', x=330, y=-310, handler=handler)
    Button(button='load', x=330, y=-255, handler=handler)
    handler.cards = game_helpers.create_cards(handler.card_count, handler)
    turtle.tracer(0)
    turtle_helper.transition()

    turtle.tracer(1)

    turtle.Screen().mainloop()

if __name__ == '__main__':
    main()


    # could just make the load part a general error to say that the default cards are loaded instead
    # that way this happens whenever the user tries to get to that directory

    # but in this case, the writing to config would need to work properly and right now it isn't.
    # unless I have a way to just run it as though the value is just boston_places without modifying config.

    # I guess would take doing a conditional for when it's run

    # like on_failed_reload or something for card creation - which I guess means it would be in all cases if it can't find it... so again we are back to the original comment...grrr