import turtle

from writing import writer

writer_help = writer()

screen = turtle.Screen()
screen.title("U.S. STATES GAME")
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

guessed = 0
guessed_list = []


import pandas
data = pandas.read_csv("50_states.csv")
states_list = data["state"].tolist()



game = True

while game:
    answer_state = screen.textinput(title=f"{guessed}/50 guessed", prompt="What's another state's name?")
    cap_ans = answer_state.title()

    if cap_ans in states_list:
        place = states_list.index(cap_ans)
        # rowy = data[data.state == answer_state]
        x_cor = data.x[place]
        y_cor = data.y[place]
        guessed += 1
        guessed_list.append(cap_ans)
        writer_help.writer(note=cap_ans, x_cor=x_cor, y_cor=y_cor)
        if guessed == 50:
            game = False
        else:
            pass


    elif answer_state == "exit":
        game = False

    else:
        pass


turtle.mainloop()

need_to_learn = []
for i in states_list:
    if i in guessed_list:
        pass
    else:
        need_to_learn.append(i)

dicty = {
    "States to Learn": need_to_learn
}

missing = pandas.DataFrame(dicty)
missing.to_csv("Improve.csv")
