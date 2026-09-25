import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
tim = turtle.Turtle()
tim.penup()
tim.hideturtle()

score = 0
game_on = 1

while game_on:
    answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state name?").title()

    print(answer_state)

    df = pandas.read_csv("50_states.csv")
    if answer_state in df.values:
        print("You guessed correct")
        x_cor = df[df.state == answer_state].x.to_list()[0]
        y_cor = df[df.state == answer_state].y.to_list()[0]
        tim.goto(x_cor,y_cor)
        tim.write(answer_state)
        score += 1
        df.drop(df[df.state == answer_state].index)


screen.mainloop()