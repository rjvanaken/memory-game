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
    card_dir = handler.set_card_path('config.cfg')
    handler.cards = game_helpers.create_cards(handler.card_count, handler, 'config.cfg', card_dir)
    turtle.tracer(0)
    turtle_helper.transition()

    turtle.tracer(1)

    turtle.Screen().mainloop()

if __name__ == '__main__':
    main()

    # dialog for specifying config file - DONE
    # make new method for resetting game values - DONE
    # add appropriate messages on reload about cards being reloaded and game restarted
    # when cards called have try except and manually set folder name to boston_places if cannot find folder - DONE