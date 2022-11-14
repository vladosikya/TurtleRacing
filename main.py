import turtle, random

screen = turtle.Screen()
GAME = True

while GAME:
    turtles = ["red", "blue", "yellow", "orange", "green"]
    turtles_obj = {}
    y = -200

    while True:
        bid = screen.textinput(title='Place your bets.', prompt="What color turtle will win? Red, Blue, Yellow, Orange, Green? ").lower()
        if bid == "red" or bid == "blue" or bid == "yellow" or bid == "orange" or bid == "green":
            break
        else:
            print("Unknown command")

    for turt in turtles:
        turtlizz = turtle.Turtle()
        turtlizz.penup()
        turtlizz.shape("turtle")
        turtlizz.color(turt)
        turtlizz.goto(-250, y)
        y+=100
        turtles_obj[turt] = turtlizz

    WINNER = True

    while WINNER:
        for turt in turtles:
            turtles_obj[turt].forward(random.randint(5, 15))
            if turtles_obj[turt].xcor() >= 315:
                if turt == bid:
                    print(f"You won. The {turt} turtle won :)")
                else:
                    print(f"You lose. The {turt} turtle won :(")
                WINNER = False
                break

    while True:
        choose = screen.textinput(title="Again?", prompt="Do you want to play again? 'y' or 'n' ").lower()
        if choose == 'y':
            screen.clearscreen()
            break
        elif choose == 'n':
            print("Buy!")
            GAME = False
            screen.bye()
            break
        else:
            print('Unknown command!')
