from tkinter import *
import pandas
from random import choice

# CONSTANTS
BACKGROUND_COLOR = "#B1DDC6"
DELAY_MS = 3000
card = {}
timer = ''
data = {}

# create a list of dictionaries from the csv file
try:
    df_to_learn = pandas.read_csv('./data/words_to_learn.csv')
except FileNotFoundError:
    df = pandas.read_csv('./data/french_words.csv')
    data = df.to_dict(orient='records')
else:
    data = df_to_learn.to_dict(orient='records')


def count_down():
    global timer
    timer = window.after(DELAY_MS, flip_card)


def flip_card():
    window.after_cancel(timer)
    canvas.itemconfig(card_background, image=card_back_img)
    canvas.itemconfig(card_title, text='English', fill='white')
    canvas.itemconfig(card_word, text=card['English'], fill='white')


def next_card():
    global card
    card = choice(data)

    canvas.itemconfig(card_title, text='French', fill='black')
    canvas.itemconfig(card_word, text=card['French'], fill='black')
    canvas.itemconfig(card_background, image=card_front_img)

    count_down()


def remove_word():
    words_to_learn = data.remove(card)
    data_frame = pandas.DataFrame(words_to_learn)
    data_frame.to_csv('./data/words_to_learn.csv', index=False)

    next_card()


# UI Setup
window = Tk()
window.title('Flash Card App')
# window.minsize(height=526, width=800)
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file='./images/card_front.png')
card_back_img = PhotoImage(file='./images/card_back.png')
card_background = canvas.create_image(400, 263, image=card_front_img)
canvas.config(highlightthickness=0, bg=BACKGROUND_COLOR)
card_title = canvas.create_text(400, 150, text='', fill='black', font=('Arial', 40, 'italic'))
card_word = canvas.create_text(400, 263, text='', fill='black', font=('Arial', 60, 'bold'))
canvas.grid(column=0, row=0, columnspan=2)

right_img = PhotoImage(file='./images/right.png')
right_button = Button(image=right_img, highlightthickness=0, command=remove_word)
right_button.grid(column=1, row=1)

wrong_img = PhotoImage(file='./images/wrong.png')
wrong_button = Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

next_card()
window.mainloop()
