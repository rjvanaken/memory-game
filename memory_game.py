import turtle_helper
import game_helpers
import turtle

def main():
    turtle.tracer(0)
    turtle_helper.setup_game_space()
    game_helpers.game_board()
    turtle.update()
    turtle.tracer(1)

    turtle.Screen().mainloop()



if __name__ == '__main__':
    main()