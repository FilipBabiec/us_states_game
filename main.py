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
df = pandas.read_csv("50_states.csv")

while score < 50:
    answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state name?").title()

    if answer_state == "Exit":
        break

    if answer_state in df.values:
        print("You guessed correct")
        x_cor = df[df.state == answer_state].x.item()
        y_cor = df[df.state == answer_state].y.item()
        tim.goto(x_cor,y_cor)
        tim.write(answer_state)
        score += 1
        df = df.drop(df[df.state == answer_state].index)

df.to_csv("states_missed")