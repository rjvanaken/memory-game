import turtle_helper
import game_helpers
import turtle
from GameHandler import GameHandler

def main():
    turtle.tracer(0)
    turtle_helper.setup_game_space()
    turtle.update()
    # splash screen
    turtle.tracer(1)
    turtle.update()
    turtle.tracer(0)
    turtle_helper.setup_title()
    # Initialize the handler
    handler = GameHandler()
    handler.cards = game_helpers.create_cards(handler.card_count, handler)
    turtle.update()
    # turtle_helper.quit_button()
    turtle.tracer(1)

    turtle.Screen().mainloop()

if __name__ == '__main__':
    main()