from tkinter import *
# import pandas

# CONSTANTS
BACKGROUND_COLOR = "#B1DDC6"

# UI Setup
window = Tk()
window.title('Flash Card App')
# window.minsize(height=526, width=800)
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file='./images/card_front.png')
canvas.create_image(400, 263, image=card_front_img)
canvas.config(highlightthickness=0, bg=BACKGROUND_COLOR)
title_text = canvas.create_text(400, 150, text='Title', fill='black', font=('Arial', 40, 'italic'))
word_text = canvas.create_text(400, 263, text='Word', fill='black', font=('Arial', 60, 'bold'))
canvas.grid(column=0, row=0, columnspan=2)

right_img = PhotoImage(file='./images/right.png')
right_button = Button(image=right_img, highlightthickness=0)
right_button.grid(column=1, row=1)

wrong_img = PhotoImage(file='./images/wrong.png')
wrong_button = Button(image=wrong_img, highlightthickness=0)
wrong_button.grid(column=0, row=1)

window.mainloop()
